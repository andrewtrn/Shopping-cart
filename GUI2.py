from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter import messagebox
from PIL import ImageTk, Image # has to install PILLOW using command pallate, this comment allows to display image.
root = Tk()
root.title("Glamping World Order Processing")
w = Label(root, text="Welcome! Please choose a language",fg="light salmon")
w.pack()
w1 = Label(root, text = "Bienvenido! Por favor elija un idioma.", fg = "light salmon")
w1.pack()
c = Canvas(root,width = 600, height = 20)
img = ImageTk.PhotoImage(Image.open("GW logo.png"))
imglabel = Label(root, image=img)
imglabel.pack()
c.pack()

def donothing():
        x = 0
def callit():
    messagebox.showinfo('Contact IT', 'You are contacting out IT support at (817) 180 - 0886')

#re-direct FAQ? button to website.
def redirect():
    webbrowser.open_new(r"https://andrewtrn.wixsite.com/chromecruises/news-feed")
class profile:
    def __init__(self):
        info = Toplevel(root, bg ="dark sea green")
        info.title("Profile")
        #Entry for address
        Label(info, text = 'First Name', bg = "dark sea green").grid(
            row = 1, column = 0, stick = W) 
        self.firstnameVar = StringVar()
        Entry(info, textvariable = self.firstnameVar, justify = RIGHT,).grid(
            row = 1, column = 2, sticky = E)
        Label(info, text = 'Last Name', bg = "dark sea green").grid(
            row = 2, column = 0, stick = W)
        self.lastnameVar = StringVar()
        Entry(info, textvariable = self.lastnameVar, justify = RIGHT,).grid(
            row = 2, column = 2, sticky = E)
        Label(info, text = 'E-mail', bg = "dark sea green").grid(
            row = 3, column = 0, stick = W)
        self.emailVar = StringVar()
        Entry(info, textvariable = self.emailVar, justify = RIGHT,).grid(
            row = 3, column = 2, sticky = E)
        Label(info, text = 'Phone Number', bg = "dark sea green").grid(
            row = 4, column = 0, stick = W)
        self.phoneVar = StringVar()
        Entry(info, textvariable = self.phoneVar, justify = RIGHT,).grid(
            row = 4, column = 2, sticky = E)
        Button(info, text = "save", command = save, fg = "light salmon" ).grid(row=5, column = 2, sticky = E)
        
        info.mainloop()
class save:
    def __init__(self):
        messagebox.showinfo('Profile', 'Your information has been saved. You may close the window.')

#create Menu bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Profile", command=profile)
filemenu.add_command(label="Order", command=donothing)
filemenu.add_command(label="Setting", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Log out", command=root.quit)
menubar.add_cascade(label="Your Account", menu=filemenu)
 
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Contact our IT support", command=callit)
helpmenu.add_command(label="FAQ", command=redirect)
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
        messagebox.showinfo("Check Out","You will now go to Shipping.") #create pop-up message
        layer = Toplevel(root, bg ="dark sea green") #create additional window
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
class shoppingcart2:
    def __init__(self):
        window2 = Toplevel(root)
        window2.title("Carrito de compras")
        frame2 = Frame(window2, width = 1000, height = 100, bg = "powder blue")
        frame2.pack()
                
        
        #create quanity field
        Label(frame2, text = 'La Cantidad', bg = "powder blue").grid(row = 2, column = 1, sticky = W)
        self.quantityVar1 = StringVar()
        Entry(frame2, textvariable = self.quantityVar1, justify = RIGHT,).grid(
            row = 2, column = 2, sticky = E)
       

        #create discount field
        Label(frame2, text = 'Descuento del 2% para el producto de más de 120 días.', bg = "powder blue").grid(row = 4, column = 1, sticky = W)
        self.discountVar1 = StringVar()
        Label(frame2, textvariable = self.discountVar1, bg = "powder blue").grid (row = 4, column = 2, sticky = E)


        #create compute total price button
        Label(frame2, text = "Coste total (Mex$)",bg = "powder blue").grid(row = 7, column = 1, sticky = W)
        self.totalcostVar1 = StringVar()
        Label(frame2, textvariable = self.totalcostVar1,bg = "powder blue").grid(row = 7, column = 2, sticky = E)
        Button(frame2, text = "Agregar al carrito", fg = "light salmon", command = self.computeprice2).grid(row= 8, column = 1, sticky = W)

        self.tkvar1 = StringVar(frame2)
        choices2 = { 'La Tienda': 100,'La Hamaca': 120 ,'Estufa de gas': 50,'La linterna': 40,'El farol': 40}
        self.tkvar1.set('La Hamaca') # set the default option
        
        popupMenu1 = OptionMenu(frame2, self.tkvar1, *choices2)
        Label(frame2, text="Elegir Producto", bg = "powder blue").grid(row = 1, column = 1, sticky = W)
        popupMenu1.grid(row = 1, column =2, sticky = E)

        # on change dropdown value
        def change_dropdown1(*args):
            print( self.tkvar1.get() )
        
        # link function to change dropdown
        self.tkvar1.trace('w', change_dropdown1)
        #Create colors list
        self.tkvar2 = StringVar(frame2)
        color2 = {'El rojo', 'Naranja Oscuro', 'Azul Celeste', 'El Verde', 'El Azul Cielo', 'El Gris'}
        self.tkvar2.set('El rojo')
        popupColor1 = OptionMenu(frame2, self.tkvar2, *color2)
        Label(frame2, text = 'Elegir Color', bg = "powder blue").grid(row = 3, column = 1, sticky = W)
        popupColor1.grid(row = 3, column = 2, sticky = E)
        def change_dropdown2(*args):
            print( self.tkvar2.get() )
        self.tkvar2.trace('w', change_dropdown2)
        
        #create checkout button
        checkout1 = Button(frame2, text = "Pagar", fg ="light salmon", command = shipping2).grid(row = 9, column = 2, sticky = E)
        
        #create tax field
        Label(frame2, text = "13% de impuestos", bg = "powder blue").grid(row = 6, column = 1, sticky = W)
        self.taxVar1 = StringVar()
        Label(frame2, textvariable = self.taxVar1, bg = "powder blue").grid (row = 6, column = 2, sticky = E)

        #create subtotal field 
        Label(frame2, text = "Total parcial (Mex$)", bg = "powder blue").grid(row = 5, column = 1, sticky = W)
        self.subtotalVAR1 = StringVar(window2)
        Label(frame2, textvariable = self.subtotalVAR1, bg = "powder blue").grid (row = 5, column = 2, sticky = E)
        #summary
        self.summaryVar1 = StringVar()
        Label(frame2, textvariable = self.summaryVar1,bg = "powder blue").grid(row = 11, column = 1, sticky = E)
        logo2 = Canvas(frame2,width = 300, height = 10)
        imgpng2 = ImageTk.PhotoImage(Image.open("GW logo.png"))
        imgpnglabel2 = Label(frame2, image=imgpng2, bg="powder blue").grid(row = 0, column = 1)
        
        
        window2.mainloop()

    def computeprice2(self):
        total_price1 = self.getTotalprice1(self.tkvar1.get(), int(self.quantityVar1.get()))
        self.totalcostVar1.set(total_price1) # assign value of total price to totalprice calculated field
        
        discount_price1 = self.getdiscountprice1(self.tkvar1.get(), int(self.quantityVar1.get()))
        self.discountVar1.set(discount_price1) # assign value of discount to calculated discount field
        
        tax_price1 = self.getTaxPrice1(self.tkvar1.get(), int(self.quantityVar1.get()))
        self.taxVar1.set(tax_price1) # assign value of tax to calculated tax field
        
        subtotal_price1 = self.getSubtotal1(self.tkvar1.get(), int(self.quantityVar1.get()))
        self.subtotalVAR1.set(subtotal_price1) # assign value of subtotal to calculated subtotal field. 
        
        item1 = 'Resumen del producto: ' + self.tkvar1.get() +','+' '+'Cantidad: ' + self.quantityVar1.get() + ','+' '+ 'Color: '+ self.tkvar2.get()+','+' '+'Coste Total: '+ 'Mex$'+ self.totalcostVar1.get()
        self.summaryVar1.set(item1)

    def getTotalprice1(self, tkvar1, quantityVar1):
    
        item_name1 = self.tkvar1.get()
        if item_name1 == 'La Tienda':
            total_price1 = ((quantityVar1 * 100) - (quantityVar1 *100 *0.02)) + ((quantityVar1 * 100) - (quantityVar1 *100 *0.02))*0.13
        if item_name1 == 'La Hamaca':
            total_price1 = ((quantityVar1 * 120) - (quantityVar1 *120 *0.02)) + ((quantityVar1 * 120) - (quantityVar1 *120 *0.02))*0.13
        if item_name1== 'Estufa de gas':
            total_price1 = ((quantityVar1 * 50) - (quantityVar1 *50 *0.02)) + ((quantityVar1* 50) - (quantityVar1 *50 *0.02))*0.13
        if item_name1 == 'La linterna':
            total_price1 = ((quantityVar1 * 40) - (quantityVar1 *40 *0.02)) + ((quantityVar1 * 40) - (quantityVar1 *40 *0.02))*0.13
        if item_name1 == 'El farol':
            total_price1 = ((quantityVar1 * 40) - (quantityVar1 *40 *0.02)) + ((quantityVar1 * 40) - (quantityVar1 *40 *0.02))*0.13

        return round(total_price1,2)
    def getdiscountprice1(self, tkvar1, quantityVar1):
        item_name1 = self.tkvar1.get()
        if item_name1 == 'La Tienda':
            discount_price1 = quantityVar1 * 100 * 0.02
        if item_name1 == 'La Hamaca':
            discount_price1 = quantityVar1 * 120 * 0.02
        if item_name1 == 'Estufa de gas':
            discount_price1 = quantityVar1 * 50 * 0.02
        if item_name1 == 'La linterna':
            discount_price1 = quantityVar1 * 40 * 0.02
        if item_name1 == 'El farol':
            discount_price1 = quantityVar1 * 40 * 0.02
        return round(discount_price1, 2)
    def getTaxPrice1(self, tkvar1, quantityVar1):
        item_name1 = self.tkvar1.get()
        if item_name1 == 'La Tienda':
            tax_price1 = ((quantityVar1 * 100) - (quantityVar1 *100 *0.02))*0.13
        if item_name1 == 'La Hamaca':
            tax_price1 = ((quantityVar1 * 120) - (quantityVar1 *120 *0.02))*0.13
        if item_name1 == 'Estufa de gas':
            tax_price1 = ((quantityVar1 * 50) - (quantityVar1 *50 *0.02))*0.13
        if item_name1 == 'La linterna':
            tax_price1 = ((quantityVar1 * 40) - (quantityVar1 *40 *0.02))*0.13
        if item_name1 == 'El farol':
            tax_price1 = ((quantityVar1 * 40) - (quantityVar1 *40 *0.02))*0.13
        return round(tax_price1, 2)
    def getSubtotal1(self, tkvar1, quantityVar1):
        item_name1 = self.tkvar1.get()
        if item_name1 == 'La Tienda':
            subtotal_price1 = (quantityVar1 * 100) - (quantityVar1 *100 *0.02)
        if item_name1 == 'La Hamaca':
            subtotal_price1 = (quantityVar1 * 120) - (quantityVar1 * 120 * 0.02)
        if item_name1 == 'Estufa de gas':
            subtotal_price1 = (quantityVar1 * 50) - (quantityVar1 * 50 * 0.02)
        if item_name1 == 'La linterna':
            subtotal_price1 = (quantityVar1 * 40) - (quantityVar1 * 40 * 0.02)
        if item_name1 == 'El farol':
            subtotal_price1 = (quantityVar1 * 40) - (quantityVar1 * 40 * 0.02)
        return round(subtotal_price1, 2)
class shipping2:
    def __init__(self): 
        messagebox.showinfo("Pagar.","Ahora se trasladará al envío.")
        layer1 = Toplevel(root, bg ="dark sea green")
        layer1.title("El envío ")
        Button(layer1, text = "Orden del lugar", command = placeorder1, fg = "light salmon" ).grid(row=7, column = 2, sticky = E)
        Label(layer1, text = '¿Dónde debemos enviar su pedido', bg = "dark sea green").grid(
            row = 1, column = 0, sticky = W)
        #Entry for address
        Label(layer1, text = 'El domicilio', bg = "dark sea green").grid(
            row = 3, column = 0, stick = W)
        self.addressVar1 = StringVar()
        Entry(layer1, textvariable = self.addressVar1, justify = RIGHT,).grid(
            row = 3, column = 2, sticky = E)
        Label(layer1, text = 'La ciudad', bg = "dark sea green").grid(
            row = 4, column = 0, stick = W)
        self.cityVar1 = StringVar()
        Entry(layer1, textvariable = self.cityVar1, justify = RIGHT,).grid(
            row = 4, column = 2, sticky = E)
        Label(layer1, text = 'El código postal', bg = "dark sea green").grid(
            row = 6, column = 0, stick = W)
        self.zipcodeVar1 = StringVar()
        Entry(layer1, textvariable = self.zipcodeVar1, justify = RIGHT,).grid(
            row = 6, column = 2, sticky = E)
        Label(layer1, text = 'El estado', bg = "dark sea green").grid(
            row = 5, column = 0, stick = W)
        self.zipcodeVar1 = StringVar()
        Entry(layer1, textvariable = self.zipcodeVar1, justify = RIGHT,).grid(
            row = 5, column = 2, sticky = E)
        
       
        #dropdown list for Country/Region
        tkvar5 = StringVar(layer1)
        country1 = {'Los Estados Unidos', 'México', 'Japón'}
        tkvar5.set('México')
        popupCountry1 = OptionMenu(layer1, tkvar5, *country1)
        Label(layer1, text = 'El país', bg = "dark sea green").grid(row = 2, column = 0, sticky = W)
        popupCountry1.grid(row = 2, column = 2, sticky = E)
        def change_dropdown5(*args):
            print( tkvar5.get() )
        tkvar5.trace('w', change_dropdown5)
        logo11 = Canvas(layer1,width = 300, height = 10)
        imgpng11 = ImageTk.PhotoImage(Image.open("GW logo.png"))
        imgpnglabel11 = Label(layer1, image=imgpng11, bg="dark sea green").grid(row = 0, column=0, sticky = W)
        
        layer1.mainloop()
class placeorder1:
    def __init__(self):   
        final1 = Toplevel(root, bg = "dark sea green")
        final1.title("Orden del lugar")
        Label(final1, text = 'Gracias por tu orden.',bg = "dark sea green" ).grid(row = 1, column = 0, sticky = W)
        Label(final1, text = "Te notificaremos cuando hemos enviado tu orden!", bg="dark sea green").grid(row = 2, column = 0, sticky = W)
        Button(final1, text = 'Cerrar', command = root.destroy, bg = "dark sea green", fg = "light salmon").grid(row=3)
        logo21 = Canvas(final1,width = 400, height = 10)
        imgpng21 = ImageTk.PhotoImage(Image.open("GW logo.png"))
        imgpnglabel21 = Label(final1, image=imgpng21, bg="dark sea green").grid(row = 0, column=0, sticky = W)
        
        final1.mainloop()
button = Button(root, text = "English", fg = "light salmon", command=shoppingcart)
button.pack()
button2 = Button(root, text = 'Español', fg = "light salmon", command = shoppingcart2)
button2.pack()
root.mainloop()