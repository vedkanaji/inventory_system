from tkinter import *
import tkinter.messagebox
import sqlite3

class product:

    def __init__(self,root):
        # Create object references of database
        p = database()
        p.conn()
        self.root = root
        self.root.title('Inventory Control System')
        self.root.geometry('1350x800+0+0')
        self.root.config(bg='light grey')

        pID = StringVar()
        pName = StringVar()
        pPrice = StringVar()
        pQuantity = StringVar()
        pStocks = StringVar()
        pContact = StringVar()

        ''''database class methods to perform operations'''

        def close():
            print('product: close method called')
            Close = tkinter.messagebox.askyesno('Inventory Control System','Really want to close?')
            if Close > 0:
                root.destroy()
            print('product: close method finished')
            return

        ''''function for clear or reset the widgets'''

        def clear():
            print('product: clear method called')
            self.txtpID.delete(0,END)
            self.txtpName.delete(0,END)
            self.txtpPrice.delete(0,END)
            self.txtpQuantity.delete(0,END)
            self.txtpStocks.delete(0,END)
            self.txtpContact.delete(0,END)
            print('product: clear method finished')


        ''''function to save in database table'''

        def insert():
            print('product: insert method called')
            if (len(pID.get()) != 0):
                p.insert(pID.get(),pName.get(),pPrice.get(),pQuantity.get(),pStocks.get(),pContact.get())
                ProductList.delete(0,END)
                ProductList.insert(END,pID.get(),pName.get(),pPrice.get(),pQuantity.get(),pStocks.get(),pContact.get())
                showinproductlist() # called showinproductlist  after inserting data inti database table
            else:
                tkinter.messagebox.askyesno('Inventory Control System','Fill the items')
            print('product: insert method finished')

        # fn responsible to show product data to scroll productList

        def showinproductlist():
            print('product: show method called')
            ProductList.delete(0,END)
            for row in p.Show():
                ProductList.insert(END,row,str(""))
            print('product: show method finished')


        # add to scroll bar
        # function to be called from scroll productList
        def productrec(event):
            print('product:productrec method called')
            global pd

            searchPD = ProductList.curselection()[0]
            pd = ProductList.get(searchPD)

            self.txtpID.delete(0,END)
            self.txtpID.insert(END,pd[0])
            self.txtpName.delete(0,END)
            self.txtpName.insert(END,pd[1])
            self.txtpPrice.delete(0,END)
            self.txtpPrice.insert(END,pd[2])
            self.txtpQuantity.delete(0,END)
            self.txtpQuantity.insert(END,pd[3])
            self.txtpStocks.delete(0,END)
            self.txtpStocks.insert(END,pd[4])
            self.txtpContact.delete(0,END)
            self.txtpContact.insert(END,pd[5])
            print('product: productrec method finished')

        # fuction to delete records from database table
        def delete():
            print('product:delete function called')
            global pd

            searchPD = ProductList.curselection()[0]
            pd = ProductList.get(searchPD)
            if (len(pID.get()) != 0):
                p.Delete(pd[0])
                clear()
                showinproductlist()
            print('product:delete method finished')

        #search the records from database table
        def search():
            print("product:search method called")
            ProductList.delete(0,END)
            for row in p.search(pID.get(),pName.get(),pPrice.get(),pQuantity.get(),pStocks.get(),pContact.get()):
                ProductList.insert(END,row,str(""))
            print("product:search method finished")

        def update():
            print('product: update method called')
            if (len(pID.get()) !=0):
                print('pd[0]',pd[p])
                p.Delete(pd[0])
            if (len(pID.get()) != 0):
                p.insert(pID.get(),pName.get(),pPrice.get(),pQuantity.get(),pStocks.get(),pContact.get())
                ProductList.delete(0,END)
            ProductList.insert(END,(pName.get(),pPrice.get(),pQuantity.get(),pStocks.get(),pContact.get()))
            print('product: update method finished')










        ''''Create the frames'''

        MainFrame = Frame(self.root, bg='light grey')
        MainFrame.grid()

        HedaFrame = Frame(MainFrame,bd= 3 ,padx =5,pady= 5,relief=RIDGE)
        HedaFrame.pack(side=TOP)

        self.ITitle =Label(HedaFrame,font=('arial','30','bold'),text='Inventory Control System')
        self.ITitle.grid()

        OperationFrame = Frame(MainFrame,bd= 1 ,width=1350,height=90,padx = 5,pady=5,relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)

        BodyFrame = Frame(MainFrame,bd =1,width = 1300,height=500,padx=5,pady =5,relief=RIDGE)
        BodyFrame.pack(side =BOTTOM)

        LeftBodyFrame = LabelFrame(BodyFrame,bd =1,width = 850,height=400,padx=5,pady =5,relief=RIDGE,font =('arial',20,'bold'),text='Product Item Details')
        LeftBodyFrame.pack(side =LEFT)

        RightBodyFrame = LabelFrame(BodyFrame,bd =1,width = 550,height=500,padx=5,pady =5,relief=RIDGE,font =('arial',20,'bold'),text='Product Item Information')
        RightBodyFrame.pack(side = RIGHT)

        ''''add widgets to left bodyframe'''

        self.labelpID = Label(LeftBodyFrame,font=('arial',15,'bold'),text ='Product ID',padx = 2,pady=2,bg='light grey')
        self.labelpID.grid(row = 0,column=0 ,sticky=W)

        self.txtpID =Entry(LeftBodyFrame,font= ('arial',15,'bold'),textvariable =pID,width = 35)
        self.txtpID.grid(row=0,column=1)

        self.labelpName = Label(LeftBodyFrame,font=('arial',15,'bold'),text ='Product Name:',padx = 2,pady=2,bg='light grey')
        self.labelpName.grid(row = 1,column=0 ,sticky=W)
        self.txtpName =Entry(LeftBodyFrame,font= ('arial',15,'bold'),textvariable =pName,width = 35)
        self.txtpName.grid(row=1,column=1)
        self.labelpPrice = Label(LeftBodyFrame,font=('arial',15,'bold'), text ='Product Price:',padx = 2,pady=2,bg='light grey')
        self.labelpPrice.grid(row = 2,column=0 ,sticky=W)
        self.txtpPrice =Entry(LeftBodyFrame,font= ('arial',15,'bold'),textvariable =pPrice,width = 35)
        self.txtpPrice.grid(row=2,column=1)
        self.labelpQuantity = Label(LeftBodyFrame,font=('arial',15,'bold'), text ='Product Qty: ',padx = 2,pady=2,bg='light grey')
        self.labelpQuantity.grid(row = 3,column=0 ,sticky=W)
        self.txtpQuantity =Entry(LeftBodyFrame,font= ('arial',15,'bold'),textvariable =pQuantity,width = 35)
        self.txtpQuantity.grid(row=3,column=1)
        self.labelpStocks = Label(LeftBodyFrame,font=('arial',15,'bold'),   text ='Stock Avail:  ',padx = 2,pady=2,bg='light grey')
        self.labelpStocks.grid(row = 4,column=0 ,sticky=W)
        self.txtpStocks =Entry(LeftBodyFrame,font= ('arial',15,'bold'),textvariable =pStocks,width = 35)
        self.txtpStocks.grid(row=4,column=1)
        self.labelpContact = Label(LeftBodyFrame,font=('arial',15,'bold'),  text ='contact info: ',padx = 2,pady=2,bg='light grey')
        self.labelpContact.grid(row = 5,column=0 ,sticky=W)
        self.txtpContact =Entry(LeftBodyFrame,font= ('arial',15,'bold'),textvariable =pContact,width = 35)
        self.txtpContact.grid(row=5,column=1)


        ''''add scroll bar'''

        scroll = Scrollbar(RightBodyFrame)
        scroll.grid(row =0,column =1,sticky ='ns')

        ProductList = Listbox(RightBodyFrame,width=40,height =25,font= ('arial',12,'bold'),yscrollcommand =scroll.set)
        ProductList.bind("<<ListboxSelect>>",productrec)       # call productrec fuction from __init__ method
        ProductList.grid(row=0,column=0)
        scroll.config(command = ProductList.yview)

        ''''add the buttons to operationFrame'''

        self.Buttonsave= Button(OperationFrame,text= 'Save',font =('arial',20,'bold'),height=1, width=7,bd = 2,command=insert)
        self.Buttonsave.grid(row= 0,column = 0)
        self.Buttonshow= Button(OperationFrame,text= 'Show',font =('arial',20,'bold'),height=1, width=7,bd = 2,command=showinproductlist)
        self.Buttonshow.grid(row= 0,column = 1)
        self.ButtonClear= Button(OperationFrame,text= 'Clear',font =('arial',20,'bold'),height=1, width=7,bd = 2,command=clear)
        self.ButtonClear.grid(row= 0,column =2)
        self.Buttondelete= Button(OperationFrame,text= 'Delete',font =('arial',20,'bold'),height=1, width=7,bd = 2,command = delete)
        self.Buttondelete.grid(row= 0,column = 3)
        self.ButtonSearch= Button(OperationFrame,text= 'Search',font =('arial',20,'bold'),height=1, width=7,bd = 2,command=search)
        self.ButtonSearch.grid(row= 0,column = 4)
        self.Buttonupdate= Button(OperationFrame,text= 'update',font =('arial',20,'bold'),height=1, width=7,bd = 2,command=update)
        self.Buttonupdate.grid(row= 0,column = 5)
        self.Buttonclose= Button(OperationFrame,text= 'close',font =('arial',20,'bold'),height=1, width=7,bd = 2,command =close)
        self.Buttonclose.grid(row= 0,column = 6)

# backed database
class database:
    def conn(self):
        print('connection method called')
        con =sqlite3.connect('Inventory.db')
        cur = con.cursor()
        query = "Create table if not exists product(pID primary key,pName text,pPrice text,pQuantity text,pStocks text,pContact text)"
        cur.execute(query)
        con.commit()
        con.close()
        print('connection method finished')

    def insert(self,pID,pName,pPrice,pQuantity,pStocks,pContact):
        print('INSERT method called')
        con =sqlite3.connect('Inventory.db')
        cur = con.cursor()
        query = "INSERT INTO product VALUES (?,?,?,?,?,?)"
        cur.execute(query,(pID,pName,pPrice,pQuantity,pStocks,pContact))
        con.commit()
        con.close()
        print('INSERT method finished')

    def Show(self):
        print('show method called')
        con =sqlite3.connect('Inventory.db')
        cur =con.cursor()
        query ="SELECT * FROM product"
        cur.execute(query)
        rows = cur.fetchall()
        print('Show method finished')
        return rows

    def Delete(self,pID):
        print('delete method called',pID)
        con = sqlite3.connect('Inventory.db')
        cur = con.cursor()
        cur.execute("DELETE FROM product WHERE pID =?",(pID,))
        con.commit()
        con.close()
        print(pID,'delete method finished')

    def search(self, pID="", pName="", pPrice="",pQuantity="",pStocks="",pContact=""):
        print('search method called')
        con = sqlite3.connect('Inventory.db')
        cur = con.cursor()
        cur.execute( "SELECT * FROM product WHERE pID = ? or pName=? or pPrice=? or pQuantity=? or pStocks=? or pContact=?",(pID,pName,pPrice,pQuantity,pStocks,pContact))
        row = cur.fetchall()
        con.close()
        print("search method finished")
        return row

    def update(self,pID="", pName="", pPrice="",pQuantity="",pStocks="",pContact=""):
        print('update method called')
        con = sqlite3.connect('Inventory.db')
        cur = con.cursor()
        cur.execute("UPDATE product SET pid = ? or pName=? or pPrice=? or pQuantity=? or pStocks=? or pContact=? WHERE pID=?",(pID,pName,pPrice,pQuantity,pStocks,pContact,pID))
        con.commit()
        con.close()
        print('update method finished')

    






if __name__ == '__main__':

    root = Tk()
    application=product(root)
    root.mainloop()
