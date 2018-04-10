def load_data(file):
    sentences = []
    relations = []
    e1_pos = []
    e2_pos = []

    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.strip().lower().split()
            relations.append(int(line[0]))
            e1_pos.append((int(line[1]), int(line[2])))  # (start_pos, end_pos)
            e2_pos.append((int(line[3]), int(line[4])))  # (start_pos, end_pos)
            sentences.append(line[5:])

    return sentences, relations, e1_pos, e2_pos

train_data = load_data('../data/train.txt')
print(type(train_data))#<class 'tuple'>
print(len(train_data))#4
print(type(train_data[0]))#<class 'list'>
print(len(train_data[0]))#8000
print(len(train_data[0][0]))#17每个句子也是列表形式，即单词的列表