# data
words = ["ai", "ml", "ai", "data", "ml", "ai", "data", "ml", "data", "data"] 

# Traditional Way
def top_k_traditional(words, k):
    word_counter = {}
    for word in words:
        # use dicitionary, supply default value
        word_counter[word] = word_counter.get(word, 0) + 1
    sorted_words = sorted(word_counter.items(), key=lambda x:x[1], reverse = True)
    final_list = []
    for i in range(k):
        final_list.append(sorted_words[i][0])
    return final_list

# Pythonic Way
from collections import Counter
def top_k_pythonic(words, k):
    return [word for word, _ in Counter(words).most_common(k)]

# output
print(top_k_traditional(words, 2))
print(top_k_pythonic(words, 2))