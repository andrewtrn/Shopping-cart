from tkinter import *
from tkinter import ttk
import pprint
from PIL import ImageTk, Image
root = Tk()
root.title("Glamping World Order Processing")
w = Label(root, text="Welcome.",fg="IndianRed3")
w.pack()
c = Canvas(root,width = 300, height = 10)
img = ImageTk.PhotoImage(Image.open("GW logo.png"))
imglabel = Label(root, image=img)
imglabel.pack()
c.pack()

class shoppingcart:
    def __init__(self):
        window = Toplevel(root)
        window.title("Shopping Cart")
        
        #create quanity field
        Label(window, text = 'Quanity').grid(row = 2, column = 1, sticky = W)
        self.quantityVar = StringVar()
        Entry(window, textvariable = self.quantityVar, justify = RIGHT).grid(
            row = 2, column = 2, sticky = E)

        #create compute total price button
        Label(window, text = "Total Cost").grid(row = 4, column = 1, sticky = W)
        self.totalcostVar = StringVar()
        Label(window, textvariable = self.totalcostVar).grid(row = 4, column = 2, sticky = E)
        Button(window, text = "Add to cart", command = self.computeprice).grid(row= 5, column = 1, sticky = W)

        self.tkvar = StringVar(window)
        choices = { 'Tent': 100,'Hammocks': 120 ,'Gas Stove': 50,'Flash Light': 40,'Lantern': 40}
        self.tkvar.set('Hammocks') # set the default option
        
        popupMenu = OptionMenu(window, self.tkvar, *choices)
        Label(window, text="Choose Product").grid(row = 1, column = 1, sticky = W)
        popupMenu.grid(row = 1, column =2, sticky = E)

        # on change dropdown value
        def change_dropdown(*args):
            print( self.tkvar.get() )
        
        # link function to change dropdown
        self.tkvar.trace('w', change_dropdown)
        #Create colors list
        tkvar3 = StringVar(window)
        color = {'Red', 'Dark Orange', 'Light Blue', 'Green', 'Sky BLue', 'Gray'}
        tkvar3.set('Dark Orange')
        popupColor = OptionMenu(window, tkvar3, *color)
        Label(window, text = 'Choose Color').grid(row = 3, column = 1, sticky = W)
        popupColor.grid(row = 3, column = 2, sticky = E)
        def change_dropdown3(*args):
            print( tkvar3.get() )
        
        tkvar3.trace('w', change_dropdown3)
        checkout = Button(window, text = "Check Out").grid(row = 6, column = 2, sticky = E)
        
        #create menu and Help section

        menubar = Menu(window)
        window.config(menu=menubar)
        file = Menu(menubar)
        file.add_command(label ="Exit")
        menubar.add_cascade(label="Help")
    
        window.mainloop()

    def computeprice(self):
        total_price = self.getTotalprice(self.tkvar.get(), int(self.quantityVar.get()))
        self.totalcostVar.set(total_price)
    def getTotalprice(self, tkvar, quanity):
    
        item_name = self.tkvar.get()
        if item_name == 'Tent':
            total_price = quanity * 100
        if item_name == 'Hammocks':
            total_price = quanity * 120
        if item_name == 'Gas Stove':
            total_price = quanity * 50
        else:
            total_price = quanity * 40
        return total_price
        
    

button = Button(root, text = "Start Shopping", command=shoppingcart)
button.pack()
root.mainloop()