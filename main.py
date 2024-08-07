file_path = "books/frankenstein.txt"


def read_contents():
    with open(file_path) as f:
        file_contents = f.read()

        return file_contents


def conv_str_list(string_to_convert):
    word_list = string_to_convert.split()
    return word_list


def len_of_txt(split_text):
    word_cnt = len(split_text)
    return word_cnt


def letter_cnt(input_str):
    lowered_string = input_str.lower()
    my_dict = {}
    alphurbet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    for item in alphurbet:
        cnt_str = lowered_string.count(item)
        my_dict[item] = cnt_str
    return my_dict


def convert_dict_to_list(dictionary):
    dict_to_list = [{"key": key, "value": value} for key, value in dictionary.items()]
    return dict_to_list


def sort_on(dictionary):
    return dictionary["value"]


def report_gen(list_of_dicts, word_count, book_title):
    print(f"=== Begin report of {book_title}===")
    print(f"{word_count} words found in the document")
    for item in list_of_dicts:
        letter = item["key"]
        value = item["value"]
        print(f"The {letter} character was found {value} times")
    return print("=== End Report ===")


def main():
    file_path = "books/frankenstein.txt"
    file_conts = read_contents()
    word_dict = letter_cnt(file_conts)
    str_list = conv_str_list(file_conts)
    word_cnt = len_of_txt(str_list)
    list_dict = convert_dict_to_list(word_dict)
    list_dict.sort(reverse=True, key=sort_on)
    report_gen(list_dict, word_cnt, file_path)


if __name__ == "__main__":
    main()
