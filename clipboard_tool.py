import os

def cut_copy_paste():
    # get the file path from user input
    file_path = input("Enter the file path: ")

    # read the file contents
    with open(file_path, 'r') as file:
        contents = file.readlines()

    # display the file contents to the user
    print("File contents:\n")
    for i, line in enumerate(contents):
        print(f"{i+1}. {line.strip()}")

    # get the operation from the user
    operation = input("Enter the operation to perform (cut, copy, or paste): ")

    # perform the selected operation
    if operation == "cut":
        # get the start and end positions for the cut operation
        start_line = int(input("Enter the start line number: "))
        start_index = int(input("Enter the start index: "))
        end_line = int(input("Enter the end line number: "))
        end_index = int(input("Enter the end index: "))

        # perform the cut operation
        cut_text = ""
        for i in range(start_line-1, end_line):
            line = contents[i]
            if i == start_line-1:
                cut_text += line[:start_index]
            elif i == end_line-1:
                cut_text += line[end_index:]
            else:
                cut_text += line
            contents[i] = ""

        file = open("cut.txt", 'w')
        file.write(f"{cut_text}")
        file.close()
        # display the cut text to the user
        print(f"Cut text: {cut_text}")

    elif operation == "copy":
        # get the start and end positions for the copy operation
        start_line = int(input("Enter the start line number: "))
        start_index = int(input("Enter the start index: "))
        end_line = int(input("Enter the end line number: "))
        end_index = int(input("Enter the end index: "))

        # perform the copy operation
        copy_text = ""
        for i in range(start_line-1, end_line):
            line = contents[i]
            if i == start_line-1:
                copy_text += line[start_index:]
            elif i == end_line-1:
                copy_text += line[:end_index]
            else:
                copy_text += line
                
        file = open("cut.txt", 'w')
        file.write(f"{copy_text}")
        file.close()
        # display the copied text to the user
        print(f"Copied text: {copy_text}")

    elif operation == "paste":
        # get the line and index where the copied/cut text should be pasted
        paste_line = int(input("Enter the line number to paste the text: "))
        paste_index = int(input("Enter the index to paste the text: "))

        # perform the paste operation
        f = open("cut.txt", 'r')
        paste_text = f.read()
        
        contents[paste_line-1] = contents[paste_line-1][:paste_index] + paste_text + contents[paste_line-1][paste_index:]
        
        f.close()
        os.remove("cut.txt")

        # display the updated file contents to the user
        print("Updated file contents:\n")
        for i, line in enumerate(contents):
            if line != "":
                print(f"{i+1}.{line.strip()}")

    else:
        print("Invalid operation. Please try again.")

    # write the updated contents back to the file
    with open(file_path, 'w') as file:
        file.writelines(contents)

# run the program
cut_copy_paste()
