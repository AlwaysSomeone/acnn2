from collections import Counter
def build_dict(sentences):
    word_count = Counter()
    for sent in sentences:
        for w in sent:
            word_count[w] += 1

    ls = word_count.most_common()

    # leave 0 to PAD
    return {w[0]: index + 1 for (index, w) in enumerate(ls)}

sentences = [['The', 'most', 'common', 'audits', 'were', 'about', 'waste', 'and', 'recycling'],
             ['The', 'company', 'waste','fabricates','were', 'plastic', 'chairs','were']]
w = build_dict(sentences)
print(w)
print(len(w))
'''
{'were': 1, 'The': 2, 'waste': 3, 'most': 4, 'common': 5, 'audits': 6, 'about': 7, 'and': 8, 'recycling': 9, 'company': 10, 'fabricates': 11, 'plastic': 12, 'chairs': 13}
13
即返回一个字典，按照单词出现频率从高到低排列，并依次编号
'''