import os
import sys


def remove_files_with_word(word, path="."):
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
        print("Użycie: python remove_files_with_word.py <słowo> <ścieżka>")
    else:
        word = sys.argv[1]
        path = " ".join(sys.argv[2:])
        if os.path.isdir(path):
            deleted_files = remove_files_with_word(word, path)
            if deleted_files:
                print(f"Usunięte pliki z '{word}' w nazwie:")
                for deleted_file in deleted_files:
                    print(f" - {deleted_file}")
            else:
                print(f"Nie znaleziono plików z '{word}' w nazwie.")
        else:
            print(f"Podana ścieżka '{path}' nie jest prawidłowym katalogiem.")