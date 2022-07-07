import tkinter as tk


def check_char(input_char, check_character):
    global WORD_COUNT, WORD
    if check_character == input_char:
        WORD += 1
        textbox.config(background="white")
        if input_char == "space":
            WORD_COUNT += 1
    elif check_character != input_char:
        print(check_character, input_char)
        WORD += 1
        return textbox.config(background="red")


def key_press(event):
    global WORD
### To Do -> this line should check list with special char as a if statment ###
    if event.keysym != "Shift_L":
        if event.keysym == "BackSpace":
            WORD -= 1
        elif event.keysym:
            check_char(event.keysym, string_list[WORD])


def update_label():
    # get the time from the global var.
    global TIME
    TIME += 1
    speed_label.set(f"{round((WORD_COUNT / TIME) * 60, 2)} word per sec")

    # calling this function again 1000ms later, which will call this again 1000ms later, ...
    main.after(1000, update_label)


with open("sample_string.txt") as file:
    data = file.read()

TIME = 1
WORD_COUNT = 1
WORD = 0
string_list = list(data)
for space in range(len(string_list)):
    if string_list[space] == " ":
        string_list[space] = "space"


main = tk.Tk()
main.title("Typing Speed App")
main.resizable(600, 800)

tk.Label(main, text=data, font=['Consoles', 16]).grid(row=0, column=0)
textbox = tk.Text(main, font=['Consoles', 20], height=1, width=27)
textbox.grid(row=1, column=0)

timer_frame = tk.Frame(main).grid(row=2, column=0)

speed_label = tk.StringVar()
speed_label.set("0.0s")

tk.Label(timer_frame, textvariable=speed_label, font=['Consolas', 20, 'bold'], pady=25).grid(row=2, column=0)

exit_button = tk.Button(main, text="Exit", font=['Consoles', 16], command=main.destroy, pady=20, padx=50)
exit_button.grid(row=3, column=0)

start_button = tk.Button(main, text="Start",font=['Consoles', 16], command=main.bind("<KeyPress>", key_press))
start_button.grid(row=3, column=1)
# bind keypress to the functions
# main.bind("<KeyPress>", key_press)

# call update label function for the first time
update_label()
main.mainloop()
