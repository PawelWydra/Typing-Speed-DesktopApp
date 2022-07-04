with open("sample_string.txt") as file:
    data = file.readline()

count_list = data.split(" ")
count_start = (len(count_list))
given_text = input("gimme text")

entered_list = given_text.split(" ")

for word in entered_list:
    if word in count_list:
        count_list.pop(count_list.index(word))

count_stop = count_start - (len(count_list))
