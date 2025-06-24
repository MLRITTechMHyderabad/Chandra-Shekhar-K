def sort_anagrams(words):
    dict={}
    for i in words:
        word=''.join(sorted(i))
        if word in dict:
            dict[word].append(i)
        else:
            dict[word]= [i]
    return list(dict.values())


input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = sort_anagrams(input_words)
print("Grouped Anagrams:",result)
