import random


words = ["computer", "software", "huawei", "scifor", "scifor", "user", "mouse", "keyboard", "error"]
word = random.choice(words)
chosen_word = list(word)
random.shuffle(chosen_word)
shuffled_word = "".join(chosen_word)
print(shuffled_word)
user_answer = str(input("TYPE HERE TO WIN:"))
if user_answer == word:
    print("THAT'S DAMN GOOD ANSWER!!!")
else:
    print("BETTER LUCK NEXT TIME")