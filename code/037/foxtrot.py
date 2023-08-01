import pdb

def compress(data):
    dictionary = {}
    prefix = data[0]
    dictionary[prefix] = 1
    for symbol in data[1:]:
        prefix += symbol
        try:
            count = dictionary[prefix]
        except KeyError:
            dictionary[prefix] = 1
        else:
            dictionary[prefix] += 1

    return dictionary

def main():
    data = "ABABABACBACBACDD"
    dictionary = compress(data)
    for key, value in dictionary.items():
        print(key, ':', value)


if __name__ == '__main__':
    main()
