def load_labels(file_path):
    result = []
    with open(file_path) as keywords:
        for word in keywords:
            result.append(word.rstrip('\n'))
    return result
