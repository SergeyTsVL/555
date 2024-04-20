def all_variants(text):
    for start in range(len(text)):
        for end in range(start+1, len(text)+1):
            yield text[start:end]

for substr in all_variants('abc'):
    print(substr)
