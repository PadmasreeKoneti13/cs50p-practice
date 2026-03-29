sentence = input()
capitalized = []
for word in sentence.split(" "):
    new_word = word[0].upper() + word[1:]
    capitalized.append(new_word)
print(" ".join(capitalized))

print(sentence.title())

#output = " ".join([word.capitalize() for word in sentence.split()])

#problem 2
# for word in sentence.split():
    # if word[0] in "aeiou":
    #     capitalized.append(word)
# result = [word for word in sentence.split() if word[0] in "aeiou"]
result = sum(1 for word in sentence.split() if word[0] in "aeiou")


# print(len(result))
print(result)