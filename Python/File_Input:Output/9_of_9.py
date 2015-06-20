my_list = [i**2 for i in range(1, 11)]

with open("text.txt", "r+") as my_file:
    for i in my_list:
        my_file.write(str(i) + "\n")

    print my_file.closed    # Check if the file is closed while inside the with-as open() function  ==> False

    if my_file.closed == False:
        """Check if the file is closed, if not, close it"""
        my_file.close()     # Close the file

    print my_file.closed    # Double-check if the file is closed after calling .close() funciton while inside the with-as open() function  ==> True

print my_file.closed        # Since this line is outside the with-as open() function, the file is automatically closed  ==> True
