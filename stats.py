def get_num_words(arr: list[str]):
    num_words = len(arr)
    # print(f"{num_words} words found in the document")
    return num_words


def get_num_characters(text: str):
    lowercase_text = text.lower()
    result = {}
    for char in lowercase_text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    # print(result)
    return result


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def create_report(characters, book_address, num_words, num_characters):
    sorted_result = chars_dict_to_sorted_list(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_address}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_result:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
