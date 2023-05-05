# https://en.wikipedia.org/wiki/Hidden_Markov_model
# https://en.wikipedia.org/wiki/Viterbi_algorithm
# https://towardsdatascience.com/hidden-markov-model-implemented-from-scratch-72865bda430e

import numpy as np

class HMM:
    def __init__(self, A, B, pi):
        self.A = A  # Transition matrix
        self.B = B  # Emission matrix
        self.pi = pi  # Initial state probability distribution

        self.N = A.shape[0]  # Number of states
        self.M = B.shape[1]  # Number of observable symbols

    def forward(self, observations: np.ndarray) -> np.ndarray:
        T = len(observations)
        alpha = np.zeros((T, self.N))

        # Initialization
        alpha[0] = self.pi * self.B[:, observations[0]]

        # Recursion
        for t in range(1, T):
            alpha[t] = np.dot(alpha[t-1], self.A) * self.B[:, observations[t]]

        return alpha

    def backward(self, observations: np.ndarray) -> np.ndarray:
        T = len(observations)
        beta = np.zeros((T, self.N))

        # Initialization
        beta[T-1] = 1

        # Recursion
        for t in range(T-2, -1, -1):
            beta[t] = np.dot(self.A, self.B[:, observations[t+1]] * beta[t+1])

        return beta

    def compute_gamma(self, 
                      observations: np.ndarray, 
                      alpha: np.ndarray, 
                      beta: np.ndarray) -> np.ndarray:
        T = len(observations)
        gamma = np.zeros((T, self.N))

        for t in range(T):
            gamma[t] = (alpha[t] * beta[t]) / np.sum(alpha[t] * beta[t])

        return gamma

    def compute_xi(self,  
                      observations: np.ndarray, 
                      alpha: np.ndarray, 
                      beta: np.ndarray) -> np.ndarray:
        T = len(observations)
        xi = np.zeros((T-1, self.N, self.N))

        for t in range(T-1):
            numerator = alpha[t].reshape(-1, 1) * self.A * self.B[:, observations[t+1]] * beta[t+1]
            denominator = np.sum(alpha[t] * beta[t])
            xi[t] = numerator / denominator

        return xi

    def train(self, observations, tol=1e-6, max_iter=100):
        T = len(observations)

        for i in range(max_iter):
            alpha = self.forward(observations)
            beta = self.backward(observations)
            gamma = self.compute_gamma(observations, alpha, beta)
            xi = self.compute_xi(observations, alpha, beta)

            # Update A
            self.A = np.sum(xi, axis=0) / np.sum(gamma[:-1], axis=0).reshape(-1, 1)

            # Update B
            gamma_sum = np.sum(gamma, axis=0)
            for j in range(self.M):
                self.B[:, j] = np.sum(gamma[observations == j], axis=0) / gamma_sum

            # Update pi
            self.pi = gamma[0] / np.sum(gamma[0])

            # Check for convergence
            if np.max(np.abs(alpha - beta)) < tol:
                break

    def viterbi(self, observations):
        T = len(observations)
        delta = np.zeros((T, self.N))
        phi = np.zeros((T, self.N))

        # Initialization
        delta[0] = self.pi * self.B[:, observations[0]]

        # Recursion
        for t in range(1, T):
            for j in range(self.N):
                delta[t, j] = np.max(delta[t-1] * self.A[:, j]) * self.B[j, observations[t]]
                phi[t, j] = np.argmax(delta[t-1] * self
 
        best_path = list()

https://en.wikipedia.org/wiki/Viterbi_algorithm#:~:text=The%20Viterbi%20algorithm%20is%20a,hidden%20Markov%20models%20(HMM).


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    for st in states:
        V[0] [st] = {"prob": start_p[st] * emit_p[st] [obs[0]], "prev": None}
    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        for st in states:
            max_tr_prob = V[t - 1] [states[0]] ["prob"] * trans_p[states[0]] [st] * emit_p[st] [obs[t]]
            prev_st_selected = states[0]
            for prev_st in states[1:]:
                tr_prob = V[t - 1] [prev_st] ["prob"] * trans_p[prev_st] [st] * emit_p[st] [obs[t]]
                if tr_prob > max_tr_prob:
                    max_tr_prob = tr_prob
                    prev_st_selected = prev_st

            max_prob = max_tr_prob
            V[t] [st] = {"prob": max_prob, "prev": prev_st_selected}

    for line in dptable(V):
        print(line)

    opt = []
    max_prob = 0.0
    best_st = None
    # Get most probable state and its backtrack
    for st, data in V[-1].items():
        if data["prob"] > max_prob:
            max_prob = data["prob"]
            best_st = st
    opt.append(best_st)
    previous = best_st

    # Follow the backtrack till the first observation
    for t in range(len(V) - 2, -1, -1):
        opt.insert(0, V[t + 1] [previous] ["prev"])
        previous = V[t + 1] [previous] ["prev"]

    print ("The steps of states are " + " ".join(opt) + " with highest probability of %s" % max_prob)

def dptable(V):
    # Print a table of steps from dictionary
    yield " " * 5 + "     ".join(("%3d" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%lf" % v[state] ["prob"]) for v in V)
