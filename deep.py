question = input("what is the answer to the greatest question of life,the universe and everything? ")
if question.strip() == "42":
    print("Yes")
elif question.lower().strip() == "forty-two" or question.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")