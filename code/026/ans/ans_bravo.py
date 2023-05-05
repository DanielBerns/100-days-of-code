''' Heavily inspired by https://github.com/j-towns/ans-notes
'''

from math import log2
from functools import reduce
from collections import Counter

def push(state, symbol, cdf_func, prec):
    cdf_low, cdf_high = cdf_func(symbol)
    freq = cdf_high - cdf_low
    return prec*(state // freq) + (state % freq) + cdf_low

def pop(state, icdf_func, cdf_func, prec):
    cdf_value = state % prec
    symbol, cdf_low, cdf_high = icdf_func(cdf_value)
    freq = cdf_high - cdf_low
    return symbol, freq*(state // prec) + cdf_value - cdf_low

initial_state = 1
precision = 8

# Some symbols to compress
sequence = 5*[2, 3, 4, 1, 4, 0, 4, 4, 4]

alphabet = list(set(sequence))
counter = Counter(sequence)
freqs = [counter[k] for k in alphabet]
sum_freqs = sum(freqs)
pmf = [f / sum_freqs for f in freqs]
entropy = sum(p*log2(1/p) for p in pmf)

cdf = reduce(lambda acc,el: acc + [acc[-1] + round(el*precision)], pmf, [0])
print(str(cdf))

# ANS requires these 2 functions.
def cdf_func(symbol):
    ''' Function signature is symbol -> (cdf_low, cdf_high).
    This can be substituted for a more complex model like a neural network'''
    return cdf[symbol], cdf[symbol+1]

def icdf_func(cdf_value):
    ''' Function signature is cdf_value -> (symbol, cdf_low, cdf_high).
    Finds the symbol where cdf_func(symbol) <= cdf_value < cdf_func(symbol+1)
    This can be substituted for a more complex model like a neural network'''
    for symbol in alphabet:
        cdf_low, cdf_high = cdf_func(symbol)
        if cdf_low <= cdf_value < cdf_high:
            return symbol, cdf_low, cdf_high


# Encode
state = initial_state
print('initial_state', state)
for symbol in reversed(sequence):
    state = push(state, symbol, cdf_func, precision)
    print('state', state, '-', symbol)

rate = state.bit_length()/len(sequence)

# Decode
decoded_sequence = len(sequence)*[None]
for i in range(len(sequence)):
    decoded_sequence[i], state = pop(state, icdf_func, cdf_func, precision)

# Sanity checks
assert decoded_sequence == sequence

print(f'''
- Encoded {len(sequence)} symbols
- Rate: {rate} bits/symbol
- Entropy: {entropy} bits
''')

