# Please, debug this lempel ziv implementation

def lempel_ziv_compress(data):
    dictionary = {}
    result = []
    prefix = ''
    
    for symbol in data:
        if prefix + symbol in dictionary:
            prefix += symbol
        else:
            dictionary[prefix + symbol] = len(dictionary) + 1
            prefix += symbol
            result.append(dictionary[prefix])
    
    if prefix:
        result.append(dictionary[prefix])
    
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
 
