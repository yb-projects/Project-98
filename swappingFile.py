# PRO C98 - Project - Swapping Files
file1_data, file2_data, file1_data_new = "", "", "" # Initalizing the variables to an empty string.

print("Welcome to File Swapper! Give us files and we will swap the content! 😀")
print() # This is for leaving a line, so that it would not look conjusted.

def swapFileData ():
    file1 = input("Enter the directory/name of the first file: ")
    file2 = input("Enter the directory/name of the second file: ")

    with open(file1, "r") as file1_content: # Opening as read mode
        file1_data = file1_content.read()

    with open(file2, "r") as file2_content:
        file2_data = file2_content.read()

    # Swapping the files:
    """
    => How it works: 
        1. We get the content of File 1, let that be x. (file1_data)
        2. We get the content of File 2, let that be y. (file2_data)
        3. We store the original content of x into a variable called x, for instance. (file1_data_new)
        4. We write into x as the content of y. (File 1 = File 2)
        5. We write into y as the content of z.
    => Thus, the files are swapped.
    """

    file1_data_new = file1_data

    with open(file1, "w") as file1_write: # Opening as write mode
        file1_write.write(file2_data)

    with open(file2, "w") as file2_write: 
        file2_write.write(file1_data_new)

    print("File Swapping has successfully completed. ")
    print()

    print("Original content of File 1:", file1_data_new)
    print("Original content of File 2:", file2_data)

    print()

    print("New content of File 1:", file2_data)
    print("New content of File 2:", file1_data_new) 

swapFileData() # Calling the above function.