def open_file():
    with open("sample_string.txt") as file:
        data = file.readline()
        return list(data)


def check_char(input_char, check_character):
    global WORD_COUNT, WORD
    ### check backspace ###
    if input_char == "\b":
        WORD = -1
        return False
    elif check_character == input_char:
        if input_char == " ":
            WORD_COUNT += 1
    elif check_character != input_char:
        print("wrong")


WORD_COUNT = 1
WORD = 0
string_list = open_file()
given_text = input("gimme text")
entered_list = list(given_text)
for char in range(len(entered_list)):
    if check_char(entered_list[char], string_list[char]):
        WORD += 1
    else:
        ### check word_count, without this space and backspace will multiply word_count var. ###
        if char == " ":
            WORD_COUNT -= 1
print(WORD_COUNT)
