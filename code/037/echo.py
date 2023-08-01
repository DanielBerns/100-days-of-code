def lempel_ziv_compress(data):
    dictionary = {}
    result = []
    prefix = ''
    
    for symbol in data:
        prefix += symbol
        if prefix in dictionary:
            pass
        else:
            dictionary[prefix] = len(dictionary) + 1
            result.append(dictionary[prefix])
    
    result.append(dictionary.get(prefix, ''))
    
    return result, dictionary


def lempel_ziv_decompress(compressed_data):
    dictionary = {1: ''}
    result = ''
    prefix = ''
    
    for code in compressed_data:
        if code in dictionary:
            entry = dictionary[code]
        else:
            entry = prefix + prefix[0]
        result += entry
        dictionary[len(dictionary) + 1] = prefix + entry[0]
        prefix = entry[1:]
    
    return result
 
# Example usage
input_data = "ABABABAABABAAB"
compressed_data, dictionary = lempel_ziv_compress(input_data)
print("Compressed data:", compressed_data)
print("dictionary:")
for key, value in dictionary.items():
    print(key, ':', value)

decompressed_data = lempel_ziv_decompress(compressed_data)
print("Decompressed data:", decompressed_data)
 
