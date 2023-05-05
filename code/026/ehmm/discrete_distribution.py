import numpy as np
import pandas as pd
from typing import Dict, List, Union

class HMMException(Exception):
    pass

class ProbabilityVector: # Probability Distribution
    def __init__(self, state_frequency: Dict[str, float]) -> None:
        states = [s for s in state_frequency.keys()]
        frequencies = [f for f in state_frequency.values()]
        total = sum(frequencies)
        
        assert len(states) == len(frequencies), "number of frequencies must match number of states."
        
        assert len(states) == len(set(states)), "states must be unique."
        
        assert all(map(lambda x: 0 <= x, frequencies)), "frequencies must be >= 0"

        assert total > 0, "must be sum(frequencies) > 0"
        
        self._states = states
        probabilities = np.array(frequencies, dtype=float) / total
        self._probabilities = probabilities

    @property
    def states(self) -> List[str]:
        return self._states
    
    @property
    def probabilities(self) -> np.ndarray:
        return self._probabilities
    
    @staticmethod
    def random_initialize(states: List[str], max_frequency: int = 10) -> 'ProbabilityVector':
        size = len(states)
        frequencies = np.random.randint(0, high=max_frequency, size=size)
        frequency_per_state = dict(((k, v) for k, v in zip(states, frequencies)))
        return ProbabilityVector(frequency_per_state)

    @property
    def df(self):
        return pd.DataFrame(data=[self.probabilities], 
                            columns=self.states,
                            index=['probability'])
    
    def __getitem__(self, state: str) -> float:
        try:
            index = self.states.index(state)
            return self.probabilities[index]
        except ValueError:
            raise HMMException(f'unknown state {state:s}')
        
    def __mul__(self, other: Union['ProbabilityVector', int, float]) -> np.ndarray:
        if isinstance(other, ProbabilityVector):
            return self.probabilities * other.probabilities
        elif isinstance(other, (int, float)):
            return self.probabilities * other
        else:
            raise HMMException(f'__mul__({other.__class.__name__:s}) not implemented')
        
    def __rmul__(self, other: Union['ProbabilityVector', int, float]) -> np.ndarray:
        return self.__mul__(other)
    
    def argmax(self):
        index = self.probabilities.argmax()
        return self.states[index]


class ProbabilityMatrix:
    def __init__(self):
        self._states: List[str] = []
        self._observables: List[str] = []
        self._frequencies: Dict[str, int] = {}
        
        
from itertools import product
from functools import reduce
        
class HiddenMarkovChain:
    def __init__(self, T, E, pi):
        self._T = T # transmission matrix A
        self._E = E # emission matrix B
        self._pi = pi
        self._states = pi.states
        self._observables = E.observables
        
    @staticmethod
    def random_initialize(states: List[str], observables: List[str]) -> 'HiddenMarkovChain':
        T = ProbabilityMatrix.random_initialize(states, states)
        E = ProbabilityMatrix.random_initialize(states, observables)
        pi = ProbabilityVector.random_initialize(states)
        return HiddenMarkovChain(T, E, pi)
    
    def _create_all_chains(self, chain_length):
        return list(product(*(self.states,) * chain_length))
    
    def score(self, observations: list) -> float:
        def mul(x, y): return x * y
        
        score = 0
        all_chains = self._create_all_chains(len(observations))
        for idx, chain in enumerate(all_chains):
            expanded_chain = list(zip(chain, [self.T.states[0]] + list(chain)))
            expanded_obser = list(zip(observations, chain))
            
            p_observations = list(map(lambda x: self.E.df.loc[x[1], x[0]], expanded_obser))
            p_hidden_state = list(map(lambda x: self.T.df.loc[x[1], x[0]], expanded_chain))
            p_hidden_state[0] = self.pi[chain[0]]
            
            score += reduce(mul, p_observations) * reduce(mul, p_hidden_state)
        return score


class HiddenMarkovChain_FP(HiddenMarkovChain):
    def _alphas(self, observations: list) -> np.ndarray:
        alphas = np.zeros((len(observations), len(self.states)))
        alphas[0, :] = self.pi.values * self.E[observations[0]].T
        for t in range(1, len(observations)):
            alphas[t, :] = (alphas[t - 1, :].reshape(1, -1) 
                         @ self.T.values) * self.E[observations[t]].T
        return alphas
    
    def score(self, observations: list) -> float:
        alphas = self._alphas(observations)
        return float(alphas[-1].sum())


class HiddenMarkovChain_Simulation(HiddenMarkovChain):
    def run(self, length: int) -> (list, list):
        assert length >= 0, "The chain needs to be a non-negative number."
        s_history = [0] * (length + 1)
        o_history = [0] * (length + 1)
        
        prb = self.pi.values
        obs = prb @ self.E.values
        s_history[0] = np.random.choice(self.states, p=prb.flatten())
        o_history[0] = np.random.choice(self.observables, p=obs.flatten())
        
        for t in range(1, length + 1):
            prb = prb @ self.T.values
            obs = prb @ self.E.values
            s_history[t] = np.random.choice(self.states, p=prb.flatten())
            o_history[t] = np.random.choice(self.observables, p=obs.flatten())
        
        return o_history, s_history


class HiddenMarkovChain_Uncover(HiddenMarkovChain_Simulation):
    def _alphas(self, observations: list) -> np.ndarray:
        alphas = np.zeros((len(observations), len(self.states)))
        alphas[0, :] = self.pi.values * self.E[observations[0]].T
        for t in range(1, len(observations)):
            alphas[t, :] = (alphas[t - 1, :].reshape(1, -1) @ self.T.values) \
                         * self.E[observations[t]].T
        return alphas
    
    def _betas(self, observations: list) -> np.ndarray:
        betas = np.zeros((len(observations), len(self.states)))
        betas[-1, :] = 1
        for t in range(len(observations) - 2, -1, -1):
            betas[t, :] = (self.T.values @ (self.E[observations[t + 1]] \
                        * betas[t + 1, :].reshape(-1, 1))).reshape(1, -1)
        return betas
    
    def uncover(self, observations: list) -> list:
        alphas = self._alphas(observations)
        betas = self._betas(observations)
        maxargs = (alphas * betas).argmax(axis=1)
        return list(map(lambda x: self.states[x], maxargs))    
