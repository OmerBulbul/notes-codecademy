my_list = [i**2 for i in range(1, 11)]

with open("text.txt", "r+") as my_file:
    for i in my_list:
        my_file.write(str(i) + "\n")
