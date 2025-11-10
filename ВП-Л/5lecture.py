# Functions
# fibonatchi

import tkinter as tk

# 1,1
# n = (n-1) + (n-2)

# def fib():
#     n1 = n2 = 1
#     print(n1, n2, end=" ")
#     for i in range(10 - 2):
#         n1, n2 = n1 + n2, n1
#         print(n1, end=" ")


    
# def fib1(n):
#     n1 = n2 = 1
#     for i in range(n):
#         print(n2, end=" ")
#         n1, n2 = n1 + n2, n1


# def fib11(count):
#     n1=n2=1
#     fiblist = []
#     for i in range(count):
#         fiblist.append(2)
        
        
# def fib22(limit):
    


# fib()
# fib1(20)
# fib1(25)
# fib1(type(fib),fib,fib())
# fib2(100)
# fib2(13)

# my own way of the fibonacci:
# def fibonacci(n):
#     n1, n2 = 0, 1

# def BGNtoEUR(bgn=100):
#     return round(bgn/1.95583,2)
def clear(event):
    outputText.config(state="normal")
    outputText.delete(0, tk.END)
    outputText.config(state="readonly")
    inputText.select_range(0,tk.END)
    inputText.focus()
    
    
def BGNtoEURGUI():
    value = float(inputText.get())
    outputText.config(state="normal")
    outputText.delete(0, tk.END)
    outputText.insert(0, str(round(value / 1.95583,2)))
    outputText.config(state="readonly")
    inputText.focus()
    
    
    
    
# if __name__ == "__main__":
#     inputValue = int(input("BGN = "))
#     print("%g"%BGNtoEUR(inputValue))
#     print(f"{inputValue} BGN = {BGNtoEUR(inputValue)} EUR")
#     print(f"{inputValue} BGN = {BGNtoEUR(inputValue)} \N{EURO SIGN}")
#     print(f"100 BGN = {BGNtoEUR()} \N{EURO SIGN}")

window = tk.Tk()  # create a window
window.title("BGN TO EUR") 
window.minsize(width=400, height=100)
window.resizable(width=False, height=False) # zabranqvam prozoreca da se resize-va

inputLabel = tk.Label(text="BGN") # statichen text
inputLabel.grid(row=0, column=0, padx=10, pady=10)


inputText = tk.Entry()
inputText.grid(row=0, column=1, padx=10, pady=10)
inputText.bind("<Return>",
               lambda event: convert.invoke())
inputText.bind("<Key>", clear)
inputText.focus()

convert = tk.Button(text="Convert", command=BGNtoEURGUI)
convert.grid(row=0, column=2, padx=10, pady=10)

outputLabel = tk.Label(text="EUR") 
outputLabel.grid(row=1, column=0, padx=10, pady=10)

outputText = tk.Entry(state="readonly")
outputText.grid(row=1, column=1, padx=10, pady=10)
window.mainloop() # show the window