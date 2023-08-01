import os
import sys


def remove_files_with_word(word, path="."):
    """
    Removes files containing the given word in their name from the specified directory.

    Args:
        word (str): Word to search for in the file name.
        path (str, optional): Path to the directory to be searched. Defaults to ".".

    Returns:
        list: List of removed files.
    """
    if not os.path.isdir(path):
        raise ValueError(f"The provided path '{path}' is not a valid directory.")

    files = os.listdir(path)
    deleted_files = []

    for file in files:
        file_path = os.path.join(path, file)
        if word in file and os.path.isfile(file_path):
            os.remove(file_path)
            deleted_files.append(file)

    return deleted_files


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python remove_files_with_word.py <word> <path>")
        print("\nArguments:")
        print("  <word>       Word to search for in the file name.")
        print("  <path>       Path to the directory to be searched.")
    else:
        word = sys.argv[1]
        path = " ".join(sys.argv[2:])
        try:
            deleted_files = remove_files_with_word(word, path)
            if deleted_files:
                print(f"Removed files with '{word}' in the name:")
                for deleted_file in deleted_files:
                    print(f" - {deleted_file}")
            else:
                print(f"No files found with '{word}' in the name.")
        except ValueError as e:
            print(f"Error: {str(e)}")
