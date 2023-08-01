import pdb

def compress_lz77(data):
    pdb.set_trace()
    compressed_data = []
    i = 0
    while i < len(data):
        length = 0
        offset = 0
        for j in range(i):
            k = 0
            while i + k < len(data) and data[i + k] == data[j + k]:
                k += 1
            if k > length:
                length = k
                offset = i - j

        if length > 0:
            compressed_data.append((offset, length, data[i + length]))
            i += length + 1
        else:
            compressed_data.append((0, 0, data[i]))
            i += 1

    return compressed_data


def decompress_lz77(compressed_data):
    decompressed_data = ""
    for entry in compressed_data:
        offset, length, char = entry
        if length > 0:
            start = len(decompressed_data) - offset
            for _ in range(length):
                decompressed_data += decompressed_data[start]
                start += 1
        decompressed_data += char

    return decompressed_data
 
# Example usage:
original_data = "abababab"
compressed_data = compress_lz77(original_data)
print("Compressed:", compressed_data)
decompressed_data = decompress_lz77(compressed_data)
print("Decompressed:", decompressed_data)
