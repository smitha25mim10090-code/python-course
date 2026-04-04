word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word=random.choice(word_list)
print(chosen_word)
placeholder=""
for position in range(len(chosen_word)):
    placeholder+="_"
print(placeholder)
lives=5
while lives>=0:
    guess=str.lower((input("Guess a letter:")))
    display=""
    for i in range(0,len(chosen_word)):
        if guess==chosen_word[i]:
            display+=guess
        else:
            display+="_"
            lives-=1
    print(display)

