file_path = "books/frankenstein.txt"

def read_contents():
    with open(file_path) as f:
        file_contents = f.read()
        print(file_contents)

def main():
    read_contents()

if __name__ == '__main__':
    main()

