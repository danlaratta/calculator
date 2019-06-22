
import tkinter as tk

# creates window and window size
window = tk.Tk()
window.geometry("225x425")

# titles the window
window.title("Calculator App")

# entry field to display numbers
entry1 = tk.Entry(width=17)
entry1.grid(row=0, column=0, columnspan=3, pady=5)


# function to do addition
def on_click(number):
    # gets the clicked buttons number
    current = entry1.get()
    # deletes what is currently stored
    entry1.delete(0, "end")
    # concatenates the numbers presses one after another
    entry1.insert(0, str(current) + str(number))


# function adds numbers when add btn is clicked
def add_click():
    # gets the first number to be added
    first_number = entry1.get()
    # global variable is set to the first number(s) that are clicked
    global f_num
    f_num = float(first_number)
    # set to addition operation
    global math
    math = "add"
    # deletes the first number when the plus button is clicked
    entry1.delete(0, "end")


# function subtracts numbers when add btn is clicked
def sub_click():
    # gets the first number to be subtracted
    first_number = entry1.get()
    # global variable is set to the first number(s) that are clicked
    global f_num
    f_num = float(first_number)
    # set to subtraction operation
    global math
    math = "subtract"
    # deletes the first number when the subtract button is clicked
    entry1.delete(0, "end")


# function multiplies numbers when add btn is clicked
def multi_click():
    # gets the first number to be multiplied
    first_number = entry1.get()
    # global variable is set to the first number(s) that are clicked
    global f_num
    f_num = float(first_number)
    # set to subtraction operation
    global math
    math = "multiply"
    # deletes the first number when the multiply button is clicked
    entry1.delete(0, "end")


# function divides numbers when add btn is clicked
def div_click():
    # gets the first number to be divided
    first_number = entry1.get()
    # global variable is set to the first number(s) that are clicked
    global f_num
    f_num = float(first_number)
    # set to subtraction operation
    global math
    math = "divide"
    # deletes the first number when the division button is clicked
    entry1.delete(0, "end")


# function clears the stored value when clear button is clicked
def clear_click():
    entry1.delete(0, "end")


# noinspection PyRedundantParentheses
def equal_click():
    # grabs whats sitting in the entry field after numbers are pressed
    second_number = entry1.get()
    # deletes the second number when the equal sign is clicked
    entry1.delete(0, "end")

    # conditional statement to determine which mathematical operation will be performed
    if(math == "add"):
        # inserts sum of first and second number into the entry field
        entry1.insert(0, f_num + float(second_number))
    elif(math == "subtract"):
        # inserts difference of first and second number into the entry field
        entry1.insert(0, f_num - float(second_number))
    elif (math == "multiply"):
        # inserts difference of first and second number into the entry field
        entry1.insert(0, f_num * float(second_number))
    elif (math == "divide"):
        # inserts difference of first and second number into the entry field
        entry1.insert(0, f_num / float(second_number))


# calculator buttons 0 - 9
btn0 = tk.Button(text="0", padx=20, pady=20, command=lambda: on_click(0)).grid(row=4, column=0)

btn1 = tk.Button(text="1", padx=20, pady=20, command=lambda: on_click(1)).grid(row=3, column=0)
btn2 = tk.Button(text="2", padx=20, pady=20, command=lambda: on_click(2)).grid(row=3, column=1)
btn3 = tk.Button(text="3", padx=20, pady=20, command=lambda: on_click(3)).grid(row=3, column=2)

btn4 = tk.Button(text="4", padx=20, pady=20, command=lambda: on_click(4)).grid(row=2, column=0)
btn5 = tk.Button(text="5", padx=20, pady=20, command=lambda: on_click(5)).grid(row=2, column=2)
btn6 = tk.Button(text="6", padx=20, pady=20, command=lambda: on_click(6)).grid(row=2, column=1)

btn7 = tk.Button(text="7", padx=20, pady=20, command=lambda: on_click(7)).grid(row=1, column=0)
btn8 = tk.Button(text="8", padx=20, pady=20, command=lambda: on_click(8)).grid(row=1, column=1)
btn9 = tk.Button(text="9", padx=20, pady=20, command=lambda: on_click(9)).grid(row=1, column=2)

# other calculator buttons
add_btn = tk.Button(text="+", padx=20, pady=20, command=add_click).grid(row=1, column=3)
sub_btn = tk.Button(text="-", padx=20, pady=20, command=sub_click).grid(row=2, column=3)
mult_btn = tk.Button(text="x", padx=20, pady=20, command=multi_click).grid(row=3, column=3)
div_btn = tk.Button(text="÷", padx=20, pady=20, command=div_click).grid(row=4, column=3)
clear_btn = tk.Button(text="C", padx=20, pady=20, command=clear_click).grid(row=4, column=1)
equal_btn = tk.Button(text="=", padx=20, pady=20, command=equal_click).grid(row=4, column=2)


window.mainloop()
