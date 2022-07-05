def open_file():
    with open("sample_string.txt") as file:
        data = file.readline()
        string_list = list(data)
        return string_list


WORD_COUNT = 1

given_text = input("gimme text")
entered_list = list(given_text)

word = 0
for _ in range(len(entered_list)):
    if string_list[word] == entered_list[word]:
        if entered_list[word] == " ":
            WORD_COUNT += 1
    elif string_list[word] != entered_list[word]:
        print("wrong")
    else:
        print("check")

    word += 1
print(WORD_COUNT)