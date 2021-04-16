from tkinter import *
class CurrencyConverter: #Create Class
    def __init__(self): #special method in python class
        window =Tk() # create application window
        window.title("Currency Converter")  # Add title to application window
        window.configure(bg="yellow") # Add background color to application window
       
       #adding label widgets to application window
        Label(window,font="Halvetica 12 bold", bg="yellow", text="Amount to convert").grid(row=1, column=1,sticky =W)
        Label(window,font="Halvetica 12 bold", bg="yellow", text="Conversion Rate ").grid(row=2, column=1,sticky =W)
        Label(window,font="Halvetica 12 bold", bg="yellow", text="Converted Amount ").grid(row=3, column=1,sticky =W)
        
        #create objects and add entry functions

        self.amounttoConvertVar = StringVar()
        Entry(window, textvariable = self.amounttoConvertVar, justify = RIGHT).grid(row=1,column=2)
        self.conversionRateVar = StringVar()
        Entry(window, textvariable = self.conversionRateVar, justify = RIGHT).grid(row=2,column=2)
        self.convertedAmountVar = StringVar()
        lblConvertedAmount = Label(window, font="Helvetica 12 bold", bg="yellow", textvariable = self.convertedAmountVar).grid(row=3,column=2,sticky = E)

# create covert and clear button. when clicked they call their functions.
        btnConvertedAmount = Button(window, text = "convert", font = "Helvetica 12 bold" , bg="blue", fg="white", command = self.convertedAmount).grid(row = 4, column=2, sticky = E)
        btdelete_all = Button(window, text = "Clear", font="Helvetica 12 bold", bg="red", fg="white", command = self.delete_all).grid(row = 4,column= 6, padx=25,pady=25,sticky = E)

        window.mainloop()

        # functions to do the conversion. Stores inputs and performes conversion.

    def  convertedAmount(self):
        amt = float(self.conversionRateVar.get())
        convertedAmountVar = float(self.amounttoConvertVar.get()) * amt
        self.convertedAmountVar.set(format(convertedAmountVar, '10.2f'))

    # function to clear inputs
    def delete_all(self):
        self.amounttoConvertVar.set("")
        self.conversionRateVar.set("")
        self.convertedAmountVar.set("")

CurrencyConverter()