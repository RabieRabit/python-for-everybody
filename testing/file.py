#Ask for a sentence

sentence = input("Sentence?")

#Print length of sentince

print(len(sentence))

#Ask for a file name (.txt)

fileName = input("What would you like the file to be named?")

#Write the sentence to the file

with open(f"{fileName}.txt", "w") as f:
    f.write(sentence)
    f.close()

print("Success, I think!")