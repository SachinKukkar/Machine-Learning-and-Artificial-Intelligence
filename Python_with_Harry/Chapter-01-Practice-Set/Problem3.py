# To print the contents of a directory using the os module

import os

def print_directory_contents(path):
    try:
        # Get the list of files and directories in the specified path
        items = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for item in items:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = '.'  # You can change this to any directory path you want to check
print_directory_contents(directory_path)
