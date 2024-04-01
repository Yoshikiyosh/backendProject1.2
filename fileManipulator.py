import sys
import os

def reverse(inputpath, outputpath):
    try:
        with open(inputpath, 'r') as infile:
            content = infile.read()
        with open(outputpath, 'w') as outfile:
            outfile.write(content[::-1])
        print("Reversal complete.")
    except IOError:
        print("Error: Input file not found or could not be opened.")

def copy(inputpath, outputpath):
    try:
        with open(inputpath, 'rb') as infile:
            with open(outputpath, 'wb') as outfile:
                outfile.write(infile.read())
        print("Copy complete.")
    except IOError:
        print("Error: Input file not found or could not be opened.")

def duplicate_contents(inputpath, n):
    try:
        with open(inputpath, 'r') as infile:
            content = infile.read()
        with open(inputpath, 'a') as outfile:
            for _ in range(n):
                outfile.write(content)
        print("Duplication complete.")
    except IOError:
        print("Error: Input file not found or could not be opened.")

def replace_string(inputpath, needle, newstring):
    try:
        with open(inputpath, 'r') as file:
            content = file.read()
            replaced_content = content.replace(needle, newstring)
        with open(inputpath, 'w') as file:
            file.write(replaced_content)
        print("Replacement complete.")
    except IOError:
        print("Error: Input file not found or could not be opened.")

def validate_args(args):
    if len(args) < 4:
        print("Error: Insufficient arguments.")
        return False
    command = args[1]
    if command not in ['reverse', 'copy', 'duplicate-contents', 'replace-string']:
        print("Error: Invalid command.")
        return False
    if command == 'reverse' or command == 'copy':
        if len(args) != 4:
            print("Error: Invalid number of arguments.")
            return False
    elif command == 'duplicate-contents':
        if len(args) != 5:
            print("Error: Invalid number of arguments.")
            return False
        try:
            n = int(args[4])
            if n <= 0:
                print("Error: Invalid value for n (must be a positive integer).")
                return False
        except ValueError:
            print("Error: n must be an integer.")
            return False
    return True

if __name__ == "__main__":
    if not validate_args(sys.argv):
        sys.exit(1)

    command = sys.argv[1]
    inputpath = sys.argv[2]
    outputpath = sys.argv[3]

    if command == 'reverse':
        reverse(inputpath, outputpath)
    elif command == 'copy':
        copy(inputpath, outputpath)
    elif command == 'duplicate-contents':
        n = int(sys.argv[4])
        duplicate_contents(inputpath, n)
    elif command == 'replace-string':
        needle = sys.argv[3]
        newstring = sys.argv[4]
        replace_string(inputpath, needle, newstring)
