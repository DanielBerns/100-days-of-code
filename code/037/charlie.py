from math import ceil, floor

def compress(data: str) -> bytes:
  """Compresses the given data using the Lempel-Ziv algorithm."""
  keys = {chr(i): i for i in range(256)}
  n_keys = 256
  compressed = []
  start = 0
  n_data = len(data) + 1
  while True:
    if n_keys >= 512:
      keys = {chr(i): i for i in range(256)}
      n_keys = 256
    for i in range(1, n_data - start):
      w = data[start:start + i]
      if w not in keys:
        compressed.append(keys[w[:-1]])
        keys[w] = n_keys
        start += i - 1
        n_keys += 1
        break
    else:
      compressed.append(keys[w])
      break
  bits = ''.join([bin(i)[2:].zfill(9) for i in compressed])
  return int(bits, 2).to_bytes(ceil(len(bits) / 8), 'big'), compressed

def decompress(data: bytes) -> str:
  """Decompresses the given data using the Lempel-Ziv algorithm."""
  keys = {i: chr(i) for i in range(256)}
  bits = bin(int.from_bytes(data, 'big'))[2:].zfill(len(data) * 8)
  n_extended_bytes = floor(len(bits) / 9)
  bits = bits[-n_extended_bytes * 9:]
  data_list = [int(bits[i * 9:(i + 1) * 9], 2) for i in range(n_extended_bytes)]
  previous = keys[data_list[0]]
  uncompressed = [previous]
  n_keys = 256
  for i in data_list[1:]:
    if n_keys >= 512:
      keys = {i: chr(i) for i in range(256)}
      n_keys = 256
    try:
      current = keys[i]
    except KeyError:
      current = previous + previous[:1]
    uncompressed.append(current)
    keys[n_keys] = previous + current[:1]
    previous = current
    n_keys += 1
  return ''.join(uncompressed)

if __name__ == '__main__':
  data = 'AAAABBCDEABCDABCAAABCDEEEEEECBBBBBBDDAAE'
  compressed, auxiliar = compress(data)
  decompressed = decompress(compressed)
  print(f'Original: {data}')
  print(f'Original: {auxiliar}')  
  print(f'Compressed: {compressed}')
  print(f'Decompressed: {decompressed}')
 
