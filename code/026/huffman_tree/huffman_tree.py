from heapq import heappush, heappop, heapify
from collections import Counter


class HuffmanNode:
    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    # Create a dictionary to count the frequency of each character
    freq_dict = Counter(text)

    # Create a heap to store the Huffman nodes
    heap = []
    for char, freq in freq_dict.items():
        heappush(heap, HuffmanNode(char, freq))

    # Build the Huffman tree
    while len(heap) > 1:
        node1 = heappop(heap)
        node2 = heappop(heap)
        combined_freq = node1.freq + node2.freq
        heappush(heap, HuffmanNode(None, combined_freq, node1, node2))

    # Return the root of the Huffman tree
    return heappop(heap)

def get_code_dict(huffman_tree):
    code_dict = {}

    def traverse(node, code=""):
        if node.char:
            code_dict[node.char] = (code, node)
        else:
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")
    
    traverse(huffman_tree)
    return code_dict
       
def print_huffman_tree(huffman_tree):
    code_dict = get_code_dict(huffman_tree)
    for key, (code, node) in code_dict.items():
        print(f"{key:s}, {code:>5s}: {node.freq:>4d}")

    
def encode_huffman_text(text, huffman_tree):
    # Create a dictionary to store the Huffman codes for each character
    code_dict = {}

    def traverse(node, code=""):
        if node.char:
            code_dict[node.char] = code
        else:
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

    traverse(huffman_tree)

    # Encode the text using the Huffman codes
    encoded_text = ""
    for char in text:
        encoded_text += code_dict[char]

    return encoded_text


def decode_huffman_text(encoded_text, huffman_tree):
    # Decode the text using the Huffman codes
    decoded_text = ""
    node = huffman_tree

    for bit in encoded_text:
        if bit == "0":
            node = node.left
        else:
            node = node.right

        if node.char:
            decoded_text += node.char
            node = huffman_tree

    return decoded_text
 
