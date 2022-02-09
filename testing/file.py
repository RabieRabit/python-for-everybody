#new wrighting to file
with open("../230_files_test.txt", "w") as file:
    file.write("Hello this is my test")
    file.close()

# reading
with open("../230_files_test.txt", "r") as file:
    content = file.read()
    file.close()

print(content)

#Another test

#appending to file
with open("../230_files_test.txt", "a") as file:
    file.write("\nHello I am appending")
    file.close()

#reading new files
with open("../230_files_test.txt", "r") as file:
    content = file.read()
    file.close()

print(content)
