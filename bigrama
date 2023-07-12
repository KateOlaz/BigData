from collections import defaultdict


def map_func(file_paths):
    inverted_index = defaultdict(lambda: defaultdict(int))

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            line = file.readline().strip()
            parts = line.split('\t')
            doc_id = parts[0]
            text = '\t'.join(parts[1:])

            words = text.split()

            for i in range(len(words) - 1):
                word_pair = (words[i], words[i+1])
                inverted_index[word_pair][doc_id] += 1

    return inverted_index


def reduce_func(inverted_index):
    sorted_index = {}

    for word_pair, doc_counts in inverted_index.items():
        sorted_docs = sorted(doc_counts.items())
        sorted_index[word_pair] = sorted_docs

    return sorted_index


def save_index(index, output_file):
    with open(output_file, 'w') as file:
        for word_pair, doc_counts in index.items():
            line = f"{word_pair}: {doc_counts}\n"
            file.write(line)


input_files = ['5722018101.txt',
               '5722018235.txt',
               '5722018301.txt',
               '5722018496.txt',
               '5722018508.txt']

output_file = 'indice_invertido.txt'
inverted_index = map_func(input_files)
index = reduce_func(inverted_index)
save_index(index, output_file)



