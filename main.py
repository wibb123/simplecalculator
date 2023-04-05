from tkinter import *
from decimal import Decimal

# Initialising window
window = Tk()

# Defining global variables
number1 = 0
number2 = 0
operator = 'none'
notFirstOperationInd = False


# Numeric button click
def b_click(b):
    global notFirstOperationInd
    # Start a new sum if equals has just been pressed or answer is 0
    if answerBox["text"] == '0' or notFirstOperationInd is True:
        b_clear_click(b_c)
        answerBox["text"] = b["text"]
    elif b["text"] == '.' and "." in answerBox["text"]:  # Avoid multiple decimal points
        pass
    else:
        answerBox["text"] = answerBox["text"] + b["text"]


# % button
def b_percent_click():
    global operator, number1, number2
    if operator == 'none':
        answerBox["text"] = '0'
        explanationBox["text"] = '0'
    elif operator == 'add':
        number2 = Decimal(answerBox["text"])
        number2 = number1 * number2 / 100
        answerBox["text"] = str(number2)
        explanationBox["text"] = str(number1) + "+" + str(number2)
    elif operator == 'subtract':
        number2 = Decimal(answerBox["text"])
        number2 = number1 * number2 / 100
        answerBox["text"] = str(number2)
        explanationBox["text"] = str(number1) + "-" + str(number2)
    elif operator == 'times' or operator == 'divide':
        number2 = Decimal(answerBox["text"])
        answerBox["text"] = str(number2 / 100)


# Clear Buttons
def b_clear_click(b):
    global number1, number2, notFirstOperationInd, operator
    answerBox["text"] = ""
    operator = 'none'
    if b["text"] == 'C':
        explanationBox["text"] = ""
        number1 = 0
        number2 = 0
    notFirstOperationInd = False


# Backspace
def b_delete_click():
    if answerBox["text"] == "":
        pass
    else:
        answerBox["text"] = answerBox["text"][0:len(answerBox["text"]) - 1]


# Add, Subtract, Times, Divide
def b_operator_click(b):
    global operator, number1, notFirstOperationInd
    # Solution for multiple operations e.g. 2 x 2 + 4
    if operator != 'none' and notFirstOperationInd is False:
        b_equals_click()
    number1 = Decimal(answerBox["text"])
    if b["text"] == '+':
        operator = "add"
    elif b["text"] == '-':
        operator = "subtract"
    elif b["text"] == '*':
        operator = "times"
    elif b["text"] == '÷':
        operator = "divide"
    explanationBox["text"] = answerBox["text"] + b["text"]
    answerBox["text"] = ""
    notFirstOperationInd = False


# Square, Square Root and Reciprocal
def b_special_click(b):
    global operator, number1, number2, notFirstOperationInd
    if operator == 'none' or notFirstOperationInd is True:  # 1 number calculations
        number1 = Decimal(answerBox["text"])
        if b["text"] == 'x^2':  # SQUARE
            explanationBox["text"] = answerBox["text"] + "^2"
            answerBox["text"] = str(number1 ** 2)
        elif b["text"] == '√x':  # SQUARE ROOT
            explanationBox["text"] = "√(" + answerBox["text"] + ")"
            answerBox["text"] = str(number1.sqrt())
        elif b["text"] == '1/x':  # RECIPROCAL
            explanationBox["text"] = "1/(" + answerBox["text"] + ")"
            answerBox["text"] = str(1 / number1)
    else:  # Combined with an operator
        number2 = Decimal(answerBox["text"])
        if b["text"] == 'x^2':  # SQUARE
            explanationBox["text"] = explanationBox["text"] + answerBox["text"] + "^2"
            answerBox["text"] = str(number2 ** 2)
        elif b["text"] == '√x':  # SQUARE ROOT
            explanationBox["text"] = explanationBox["text"] + "√(" + answerBox["text"] + ")"
            answerBox["text"] = str(number2.sqrt())
        elif b["text"] == '1/x':  # RECIPROCAL
            explanationBox["text"] = explanationBox["text"] + "1/(" + answerBox["text"] + ")"
            answerBox["text"] = str(1 / number2)


# Equals button
def b_equals_click():
    global number1, number2, notFirstOperationInd, operator
    if operator == 'add':
        if notFirstOperationInd is False:
            number2 = Decimal(answerBox["text"])
            notFirstOperationInd = True
        else:
            number1 = Decimal(answerBox["text"])
        explanationBox["text"] = str(number1) + "+" + str(number2) + "="
        answerBox["text"] = str(number1 + number2)
    elif operator == 'subtract':
        if notFirstOperationInd is False:
            number2 = Decimal(answerBox["text"])
            notFirstOperationInd = True
        else:
            number1 = Decimal(answerBox["text"])
        explanationBox["text"] = str(number1) + "-" + str(number2) + "="
        answerBox["text"] = str(number1 - number2)
    elif operator == 'times':
        if notFirstOperationInd is False:
            number2 = Decimal(answerBox["text"])
            notFirstOperationInd = True
        else:
            number1 = Decimal(answerBox["text"])
        explanationBox["text"] = str(number1) + "*" + str(number2) + "="
        answerBox["text"] = str(number1 * number2)
    elif operator == 'divide':
        if notFirstOperationInd is False:
            number2 = Decimal(answerBox["text"])
            notFirstOperationInd = True
        else:
            number1 = Decimal(answerBox["text"])
        explanationBox["text"] = str(number1) + "÷" + str(number2) + "="
        answerBox["text"] = str(number1 / number2)
    else:
        pass


# Negation button
def b_plus_minus_click():
    if answerBox["text"][0:1] == "-":
        answerBox["text"] = answerBox["text"][1:len(answerBox["text"])]
    else:
        answerBox["text"] = "-" + answerBox["text"]


# UI CONFIG
# making small answer box
explanationBox = Label(window, text="", height=2, width=60, font=("Arial", 10), bg="#363636", fg="grey", anchor="e")
# making answer box
answerBox = Label(window, text="", height=4, width=30, font=("Arial", 20), bg="#363636", fg="white", anchor="e")

# making buttons
b_percent = Button(window, text="%", height=2, width=7, font=("Arial", 20), bg="#4c4c4d", fg="white",
                   command=b_percent_click)
b_ce = Button(window, text="CE", height=2, width=7, font=("Arial", 20), bg="#4c4c4d", fg="white",
              command=lambda: b_clear_click(b_ce))
b_c = Button(window, text="C", height=2, width=7, font=("Arial", 20), bg="#4c4c4d", fg="white",
             command=lambda: b_clear_click(b_c))
b_delete = Button(window, text="⌫", height=2, width=7, font=("Arial", 20), bg="#4c4c4d", fg="white",
                  command=b_delete_click)

b_recip = Button(window, text="1/x", height=2, width=7, font=("Arial", 20), bg="#4c4c4d", fg="white",
                 command=lambda: b_special_click(b_recip))
b_square = Button(window, text="x^2", height=2, width=7, font=("Arial", 20), bg="#4c4c4d", fg="white",
                  command=lambda: b_special_click(b_square))
b_sqrt = Button(window, text="√x", height=2, width=7, font=("Arial", 20), bg="#4c4c4d", fg="white",
                command=lambda: b_special_click(b_sqrt))
b_divide = Button(window, text="÷", height=2, width=7, font=("Arial", 20), bg="#4c4c4d", fg="white",
                  command=lambda: b_operator_click(b_divide))

b7 = Button(window, text="7", height=2, width=7, font=("Arial", 20), bg="#333333", fg="white",
            command=lambda: b_click(b7))
b8 = Button(window, text="8", height=2, width=7, font=("Arial", 20), bg="#333333", fg="white",
            command=lambda: b_click(b8))
b9 = Button(window, text="9", height=2, width=7, font=("Arial", 20), bg="#333333", fg="white",
            command=lambda: b_click(b9))
b_times = Button(window, text="*", height=2, width=7, font=("Arial", 20), bg="#4c4c4d", fg="white",
                 command=lambda: b_operator_click(b_times))

b4 = Button(window, text="4", height=2, width=7, font=("Arial", 20), bg="#333333", fg="white",
            command=lambda: b_click(b4))
b5 = Button(window, text="5", height=2, width=7, font=("Arial", 20), bg="#333333", fg="white",
            command=lambda: b_click(b5))
b6 = Button(window, text="6", height=2, width=7, font=("Arial", 20), bg="#333333", fg="white",
            command=lambda: b_click(b6))
b_subtract = Button(window, text="-", height=2, width=7, font=("Arial", 20), bg="#4c4c4d", fg="white",
                    command=lambda: b_operator_click(b_subtract))

b1 = Button(window, text="1", height=2, width=7, font=("Arial", 20), bg="#333333", fg="white",
            command=lambda: b_click(b1))
b2 = Button(window, text="2", height=2, width=7, font=("Arial", 20), bg="#333333", fg="white",
            command=lambda: b_click(b2))
b3 = Button(window, text="3", height=2, width=7, font=("Arial", 20), bg="#333333", fg="white",
            command=lambda: b_click(b3))
b_add = Button(window, text="+", height=2, width=7, font=("Arial", 20), bg="#4c4c4d", fg="white",
               command=lambda: b_operator_click(b_add))

b_plus_minus = Button(window, text="+/-", height=2, width=7, font=("Arial", 20), bg="#333333", fg="white",
                      command=b_plus_minus_click)
b0 = Button(window, text="0", height=2, width=7, font=("Arial", 20), bg="#333333", fg="white",
            command=lambda: b_click(b0))
b_dec_point = Button(window, text=".", height=2, width=7, font=("Arial", 20), bg="#333333", fg="white",
                     command=lambda: b_click(b_dec_point))
b_equals = Button(window, text="=", height=2, width=7, font=("Arial", 20), bg="#0250f7", fg="white",
                  command=b_equals_click)

# Grid set up
explanationBox.grid(row=0, column=1, columnspan=4)
answerBox.grid(row=1, column=1, columnspan=4)

b_percent.grid(row=2, column=1)
b_ce.grid(row=2, column=2)
b_c.grid(row=2, column=3)
b_delete.grid(row=2, column=4)

b_recip.grid(row=3, column=1)
b_square.grid(row=3, column=2)
b_sqrt.grid(row=3, column=3)
b_divide.grid(row=3, column=4)

b7.grid(row=4, column=1)
b8.grid(row=4, column=2)
b9.grid(row=4, column=3)
b_times.grid(row=4, column=4)

b4.grid(row=5, column=1)
b5.grid(row=5, column=2)
b6.grid(row=5, column=3)
b_subtract.grid(row=5, column=4)

b1.grid(row=6, column=1)
b2.grid(row=6, column=2)
b3.grid(row=6, column=3)
b_add.grid(row=6, column=4)

b_plus_minus.grid(row=7, column=1)
b0.grid(row=7, column=2)
b_dec_point.grid(row=7, column=3)
b_equals.grid(row=7, column=4)

# main loop
window.mainloop()
