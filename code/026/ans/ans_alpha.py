class ANS:
    def __init__(self, table):
        self.table = table

    def encode(self, text):
        freqs = {char: text.count(char) for char in set(text)}
        freq_table = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
        state = 1
        for char, freq in freq_table:
            for i in range(freq):
                state = (state << self.table[char][1]) + self.table[char][0]
        return state

    def decode(self, state, length):
        freqs = {char: 0 for char in self.table}
        for char, (code, bits) in self.table.items():
            while state % code == 0 and freqs[char] < length:
                state //= code
                freqs[char] += 1
        if sum(freqs.values()) != length:
            raise ValueError("Decoded length doesn't match input length.")
        return "".join([char * freqs[char] for char in self.table])

# Example usage
table = {
    "a": (2, 1),
    "b": (3, 2),
    "c": (5, 3),
    "d": (7, 4),
    "e": (11, 5),
    "f": (13, 6),
    "g": (17, 7),
}

ans = ANS(table)
text = "abacad"
state = ans.encode(text)
decoded_text = ans.decode(state, len(text))
print("Encoded state:", state)
print("Decoded text:", decoded_text)
