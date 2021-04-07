from tkinter import *

root = Tk();
root.title("Calculator")

result = Entry(root, width=30, borderwidth=5);
result.grid(row=0, column=0, columnspan=5, ipadx=90);
# result.insert(0, "0");



def buttonClickNumber(number):
    temp = result.get();
    result.delete(0, END);
    result.insert(0, str(temp) + str(number));


def buttonClickClear():
    result.delete(0, END);


def buttonClickAdd():
    number = result.get();
    global check;
    check = "addition";
    global calculation
    calculation = int(number);
    result.delete(0, END);


def buttonClickSubt():
    number = result.get();
    global check;
    check = "subtraction";
    global calculation
    calculation = int(number);
    result.delete(0, END);


def buttonClickDivision():
    number = result.get();
    global check
    check = "division";
    global calculation
    calculation = int(number);
    result.delete(0, END);


def buttonClickMult():
    number = result.get();
    global check;
    check = "multiplication";
    global calculation;
    calculation = int(number);
    result.delete(0, END);


def buttonClickEqual():
    operation = result.get();
    result.delete(0, END);
    if check == "addition":
        result.insert(0, calculation + int(operation));
    elif check == "subtraction":
        result.insert(0, calculation - int(operation));
    elif check == "multiplication":
        result.insert(0, calculation * int(operation));
    elif check == "division":
        result.insert(0, calculation / int(operation));


def buttonsAdjustments():
    button1 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClickNumber(7));
    button2 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClickNumber(8));
    button3 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClickNumber(9));
    button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClickNumber(4));
    button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClickNumber(5));
    button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClickNumber(6));
    button7 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClickNumber(1));
    button8 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClickNumber(2));
    button9 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClickNumber(3));
    button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClickNumber(0));
    # pending change
    button_Add = Button(root, text="+", padx=40, pady=20, command=lambda: buttonClickAdd());
    button_Subt = Button(root, text="-", padx=40, pady=20, command=lambda: buttonClickSubt());
    button_Mult = Button(root, text="*", padx=40, pady=20, command=lambda: buttonClickMult());
    button_Division = Button(root, text="/", padx=40, pady=20, command=lambda: buttonClickDivision());

    button_Equal = Button(root, text="=", padx=40, pady=20, command=lambda: buttonClickEqual());
    button_Decimal = Button(root, text=".", padx=41.51, pady=20, command=lambda: buttonClick());
    button_Negative = Button(root, text="+/-", padx=34, pady=20, command=lambda: buttonClick());
    button_Clear = Button(root, text="Clear", padx=125, pady=20, command=lambda: buttonClickClear());

    button1.grid(row=2, column=0);
    button2.grid(row=2, column=1);
    button3.grid(row=2, column=2);

    button4.grid(row=3, column=0);
    button5.grid(row=3, column=1);
    button6.grid(row=3, column=2);

    button7.grid(row=4, column=0);
    button8.grid(row=4, column=1);
    button9.grid(row=4, column=2);

    button0.grid(row=5, column=1);
    button_Add.grid(row=4, column=3);
    button_Subt.grid(row=3, column=3);
    button_Mult.grid(row=2, column=3);
    button_Equal.grid(row=5, column=3);
    button_Decimal.grid(row=5, column=2);
    button_Negative.grid(row=5, column=0);
    button_Division.grid(row=1, column=3);
    button_Clear.grid(row=1, columnspan=3);


# This creates the actual form
buttonsAdjustments();
root.mainloop();
