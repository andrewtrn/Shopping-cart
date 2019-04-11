from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image # has to install PILLOW using command pallate, this comment allows to display image.
root = Tk()
root.title("Glamping World Order Processing")
w = Label(root, text="Welcome.",fg="light salmon")
w.pack()
c = Canvas(root,width = 600, height = 20)
img = ImageTk.PhotoImage(Image.open("GW logo.png"))
imglabel = Label(root, image=img)
imglabel.pack()
c.pack()

def donothing():
        x = 0

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Profile", command=donothing)
filemenu.add_command(label="Order", command=donothing)
filemenu.add_command(label="Setting", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Log out", command=root.quit)
menubar.add_cascade(label="Your Account", menu=filemenu)
 
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Contact our IT support", command=donothing)
helpmenu.add_command(label="FAQ", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)
 
root.config(menu=menubar)

class shoppingcart:
    def __init__(self):
        window = Toplevel(root)
        window.title("Shopping Cart")
        frame = Frame(window, width = 1000, height = 100, bg = "powder blue")
        frame.pack()
                
        
        #create quanity field
        Label(frame, text = 'Quanity', bg = "powder blue").grid(row = 2, column = 1, sticky = W)
        self.quantityVar = StringVar()
        Entry(frame, textvariable = self.quantityVar, justify = RIGHT,).grid(
            row = 2, column = 2, sticky = E)
       

        #create discount field
        Label(frame, text = 'Discount(2% for item in stock over 120 days)', bg = "powder blue").grid(row = 4, column = 1, sticky = W)
        self.discountVar = StringVar()
        Label(frame, textvariable = self.discountVar, bg = "powder blue").grid (row = 4, column = 2, sticky = E)


        #create compute total price button
        Label(frame, text = "Total Cost ($)",bg = "powder blue").grid(row = 7, column = 1, sticky = W)
        self.totalcostVar = StringVar()
        Label(frame, textvariable = self.totalcostVar,bg = "powder blue").grid(row = 7, column = 2, sticky = E)
        Button(frame, text = "Add to cart", fg = "light salmon", command = self.computeprice).grid(row= 8, column = 1, sticky = W)

        self.tkvar = StringVar(frame)
        choices = { 'Tent': 100,'Hammocks': 120 ,'Gas Stove': 50,'Flash Light': 40,'Lantern': 40}
        self.tkvar.set('Hammocks') # set the default option
        
        popupMenu = OptionMenu(frame, self.tkvar, *choices)
        Label(frame, text="Choose Product", bg = "powder blue").grid(row = 1, column = 1, sticky = W)
        popupMenu.grid(row = 1, column =2, sticky = E)

        # on change dropdown value
        def change_dropdown(*args):
            print( self.tkvar.get() )
        
        # link function to change dropdown
        self.tkvar.trace('w', change_dropdown)
        #Create colors list
        self.tkvar3 = StringVar(frame)
        color = {'Red', 'Dark Orange', 'Light Blue', 'Green', 'Sky BLue', 'Gray'}
        self.tkvar3.set('Dark Orange')
        popupColor = OptionMenu(frame, self.tkvar3, *color)
        Label(frame, text = 'Choose Color', bg = "powder blue").grid(row = 3, column = 1, sticky = W)
        popupColor.grid(row = 3, column = 2, sticky = E)
        def change_dropdown3(*args):
            print( self.tkvar3.get() )
        self.tkvar3.trace('w', change_dropdown3)
        
        #create checkout button
        checkout = Button(frame, text = "Check Out", fg ="light salmon", command = shipping).grid(row = 9, column = 2, sticky = E)
        
        #create tax field
        Label(frame, text = "Tax (13%)", bg = "powder blue").grid(row = 6, column = 1, sticky = W)
        self.taxVar = StringVar()
        Label(frame, textvariable = self.taxVar, bg = "powder blue").grid (row = 6, column = 2, sticky = E)

        #create subtotal field 
        Label(frame, text = "Subtotal", bg = "powder blue").grid(row = 5, column = 1, sticky = W)
        self.subtotalVAR = StringVar()
        Label(frame, textvariable = self.subtotalVAR, bg = "powder blue").grid (row = 5, column = 2, sticky = E)
        #summary
        self.summaryVar = StringVar()
        Label(frame, textvariable = self.summaryVar,bg = "powder blue").grid(row = 11, column = 1, sticky = E)
        logo = Canvas(frame,width = 300, height = 10)
        imgpng = ImageTk.PhotoImage(Image.open("GW logo.png"))
        imgpnglabel = Label(frame, image=imgpng, bg="powder blue").grid(row = 0, column = 1)
        
        
        window.mainloop()

    def computeprice(self):
        total_price = self.getTotalprice(self.tkvar.get(), int(self.quantityVar.get()))
        self.totalcostVar.set(total_price) # assign value of total price to totalprice calculated field
        
        discount_price = self.getdiscountprice(self.tkvar.get(), int(self.quantityVar.get()))
        self.discountVar.set(discount_price) # assign value of discount to calculated discount field
        
        tax_price = self.getTaxPrice(self.tkvar.get(), int(self.quantityVar.get()))
        self.taxVar.set(tax_price) # assign value of tax to calculated tax field
        
        subtotal_price = self.getSubtotal(self.tkvar.get(), int(self.quantityVar.get()))
        self.subtotalVAR.set(subtotal_price) # assign value of subtotal to calculated subtotal field. 
        item = 'Product Summary: ' + self.tkvar.get() +','+' '+'Quantity: ' + self.quantityVar.get() + ','+' '+ 'Color: '+ self.tkvar3.get()+','+' '+'Total Price: '+ '$'+ self.totalcostVar.get()
        self.summaryVar.set(item)
    def getTotalprice(self, tkvar, quantityVar):
    
        item_name = self.tkvar.get()
        if item_name == 'Tent':
            total_price = ((quantityVar * 100) - (quantityVar *100 *0.02)) + ((quantityVar * 100) - (quantityVar *100 *0.02))*0.13
        if item_name == 'Hammocks':
            total_price = ((quantityVar * 120) - (quantityVar *120 *0.02)) + ((quantityVar * 120) - (quantityVar *120 *0.02))*0.13
        if item_name == 'Gas Stove':
            total_price = ((quantityVar * 50) - (quantityVar *50 *0.02)) + ((quantityVar * 50) - (quantityVar *50 *0.02))*0.13
        if item_name == 'Lantern':
            total_price = ((quantityVar * 40) - (quantityVar *40 *0.02)) + ((quantityVar * 40) - (quantityVar *40 *0.02))*0.13
        if item_name == 'Flashlight':
            total_price = ((quantityVar * 40) - (quantityVar *40 *0.02)) + ((quantityVar * 40) - (quantityVar *40 *0.02))*0.13

        return round(total_price,2)
    def getdiscountprice(self, tkvar, quantityVar):
        item_name = self.tkvar.get()
        if item_name == 'Tent':
            discount_price = quantityVar * 100 * 0.02
        if item_name == 'Hammocks':
            discount_price = quantityVar * 120 * 0.02
        if item_name == 'Gas Stove':
            discount_price = quantityVar * 50 * 0.02
        if item_name == 'Lantern':
            discount_price = quantityVar * 40 * 0.02
        if item_name == 'Flashlight':
            discount_price = quantityVar * 40 * 0.02
        return round(discount_price,2)
    def getTaxPrice(self, tkvar, quantityVar):
        item_name = self.tkvar.get()
        if item_name == 'Tent':
            tax_price = ((quantityVar * 100) - (quantityVar *100 *0.02))*0.13
        if item_name == 'Hammocks':
            tax_price = ((quantityVar * 120) - (quantityVar *120 *0.02))*0.13
        if item_name == 'Gas Stove':
            tax_price = ((quantityVar * 50) - (quantityVar *50 *0.02))*0.13
        if item_name == 'Lantern':
            tax_price = ((quantityVar * 40) - (quantityVar *40 *0.02))*0.13
        if item_name == 'Flashlight':
            tax_price = ((quantityVar * 40) - (quantityVar *40 *0.02))*0.13
        return round(tax_price,2)
    def getSubtotal(self, tkvar, quantityVar):
        item_name = self.tkvar.get()
        if item_name == 'Tent':
            subtotal_price = (quantityVar * 100) - (quantityVar *100 *0.02)
        if item_name == 'Hammocks':
            subtotal_price = (quantityVar * 120) - (quantityVar * 120 * 0.02)
        if item_name == 'Gas Stove':
            subtotal_price = (quantityVar * 50) - (quantityVar * 50 * 0.02)
        if item_name == 'Lantern':
            subtotal_price = (quantityVar * 40) - (quantityVar * 40 * 0.02)
        if item_name == 'Flashlight':
            subtotal_price = (quantityVar * 40) - (quantityVar * 40 * 0.02)
        return round(subtotal_price,2)


class shipping:
        
    def __init__(self): 
        messagebox.showinfo("Check Out","You will now go to Shipping.")
        layer = Toplevel(root, bg ="dark sea green")
        layer.title("Shipping")
        Button(layer, text = "Place Order", command = placeorder, fg = "light salmon" ).grid(row=7, column = 2, sticky = E)
        Label(layer, text = 'Where should we send your order?', bg = "dark sea green").grid(
            row = 1, column = 0, sticky = W)
        #Entry for address
        Label(layer, text = 'Address', bg = "dark sea green").grid(
            row = 3, column = 0, stick = W)
        self.addressVar = StringVar()
        Entry(layer, textvariable = self.addressVar, justify = RIGHT,).grid(
            row = 3, column = 2, sticky = E)
        Label(layer, text = 'City', bg = "dark sea green").grid(
            row = 4, column = 0, stick = W)
        self.cityVar = StringVar()
        Entry(layer, textvariable = self.cityVar, justify = RIGHT,).grid(
            row = 4, column = 2, sticky = E)
        Label(layer, text = 'Postal Code', bg = "dark sea green").grid(
            row = 6, column = 0, stick = W)
        self.zipcodeVar = StringVar()
        Entry(layer, textvariable = self.zipcodeVar, justify = RIGHT,).grid(
            row = 6, column = 2, sticky = E)
        Label(layer, text = 'State/Province', bg = "dark sea green").grid(
            row = 5, column = 0, stick = W)
        self.zipcodeVar = StringVar()
        Entry(layer, textvariable = self.zipcodeVar, justify = RIGHT,).grid(
            row = 5, column = 2, sticky = E)
        
       
        #dropdown list for Country/Region
        tkvar4 = StringVar(layer)
        country = {'United States', 'Mexico', 'Japan', 'Australia'}
        tkvar4.set('United States')
        popupCountry = OptionMenu(layer, tkvar4, *country)
        Label(layer, text = 'Country/Region', bg = "dark sea green").grid(row = 2, column = 0, sticky = W)
        popupCountry.grid(row = 2, column = 2, sticky = E)
        def change_dropdown4(*args):
            print( tkvar4.get() )
        tkvar4.trace('w', change_dropdown4)
        logo1 = Canvas(layer,width = 300, height = 10)
        imgpng1 = ImageTk.PhotoImage(Image.open("GW logo.png"))
        imgpnglabel1 = Label(layer, image=imgpng1, bg="dark sea green").grid(row = 0, column=0, sticky = W)
        
        layer.mainloop()
class placeorder:
    def __init__(self):   
        final = Toplevel(root, bg = "dark sea green")
        final.title("Place Order")
        Label(final, text = 'Thank you for your order.',bg = "dark sea green" ).grid(row = 1, column = 0, sticky = W)
        Label(final, text = "You will be notified when the item is shipped!", bg="dark sea green").grid(row = 2, column = 0, sticky = W)
        Button(final, text = 'Close', command = root.destroy, bg = "dark sea green", fg = "light salmon").grid(row=3)
        logo2 = Canvas(final,width = 300, height = 10)
        imgpng2 = ImageTk.PhotoImage(Image.open("GW logo.png"))
        imgpnglabel2 = Label(final, image=imgpng2, bg="dark sea green").grid(row = 0, column=0, sticky = W)
        
        final.mainloop()
        
button = Button(root, text = "Start Shopping", fg = "light salmon", command=shoppingcart)
button.pack()
root.mainloop()
