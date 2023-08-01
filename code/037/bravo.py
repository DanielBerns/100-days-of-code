import pdb

def lempel_ziv_compress(data):
    dictionary = {}
    result = []
    w = ''
    
    for symbol in data:
        if w + symbol in dictionary:
            w += symbol
        else:
            if w:
                result.append(dictionary[w])
            dictionary[w + symbol] = len(dictionary) + 1
            w = symbol
    
    pdb.set_trace()
    if w:
        result.append(dictionary[w])
    
    return result


def lempel_ziv_decompress(compressed_data):
    dictionary = {1: ''}
    result = ''
    w = ''
    
    for code in compressed_data:
        if code in dictionary:
            entry = dictionary[code]
            result += entry
            if w:
                dictionary[len(dictionary) + 1] = w + entry[0]
                w = entry
        else:
            entry = w + w[0]
            result += entry
            dictionary[len(dictionary) + 1] = entry
            w = entry
    
    return result


# Example usage
input_data = "ABABABAABABAAB"
compressed_data = lempel_ziv_compress(input_data)
print("Compressed data:", compressed_data)

decompressed_data = lempel_ziv_decompress(compressed_data)
print("Decompressed data:", decompressed_data)
 
