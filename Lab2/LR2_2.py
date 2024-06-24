'''
This is the main code for Programming Problem 2
'''

#function for reading and returning the lines of a file
def fileRead(filename):
    with open(filename, 'r') as file:
        line = file.readlines()
    return line

#main function
def main():
    filename = input("Enter file to open: ")

    try:
        line = fileRead(filename)
    except FileNotFoundError:
        print("File not found")
    
    maxLines = len(line)

    print("Extracted ", maxLines, " lines of text from file.")

    while True:
        try:
            extractLine = int(input(f"Enter the line to be extracted [1 - {maxLines}]. Or 0 to Exit: "))
        except ValueError:
            print('Enter a valid number.')
            continue

        if extractLine == 0:
            print("Closing program")
            break
        elif 1 <= extractLine <= maxLines:
            print(line[extractLine - 1])
        else:
            print(f"Invalid number. Enter a number from 1-{maxLines} ONLY")

if __name__ == "__main__":
    main()