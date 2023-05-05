from huffman_tree import (build_huffman_tree, 
                          encode_huffman_text, 
                          decode_huffman_text, 
                          print_huffman_tree)


text = "hello world"
huffman_tree = build_huffman_tree(text)
encoded_text = encode_huffman_text(text, huffman_tree)
decoded_text = decode_huffman_text(encoded_text, huffman_tree)

print("Original text:", text)
print("Encoded text:", encoded_text)
print("Decoded text:", decoded_text) 

print_huffman_tree(huffman_tree)
