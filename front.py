from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mannu
window=Tk(className="GOVERMENT POLYTECHNIC COLLEGE")
from tkinter import messagebox
window.geometry('600x600+200+50')
#window.state('zoomed')
window.attributes('-fullscreen',True)
window.resizable(False,False)
window.configure()
img = ImageTk.PhotoImage(Image.open("forest.jpg"))
f1=("Times", 22, 'overstrike')
lbltop=Label(window,text="User Login Area",font=f1)
lbltop.grid(row=0,column=0,padx=550,pady=50)

frm=Frame(window,height=300,width=700,bd=2)
frm.grid(row=1,column=0)
frm.grid_propagate(0)

#user values are defined.......
txtid_value=StringVar()
txtpass_value=StringVar()


lblid=Label(frm,text='Login ID',font=('bold',14),fg='Red')
lblid.grid(row=0,column=0,padx=6)
txtid=Entry(frm,font=('bold',15),textvariable=txtid_value)
txtid.grid(row=0,column=1,padx=30,pady=20)


lblpass=Label(frm,text='Password',font=('bold',14),fg='Red')
lblpass.grid(row=1,column=0,padx=6,pady=20)
txtpass=Entry(frm,font=('bold',15),show="%",textvariable=txtpass_value)
txtpass.grid(row=1,column=1,padx=30,pady=20)



def book_window():
    bw=Toplevel(window)
    bw.title("LIBRARY MANAGEMENT SYSTEM")
    from tkinter import messagebox
    #bw.geometry('500x500=+300+100')
    bw.state('zoomed')
    bw.configure(bg='green')
    s = ttk.Style()
    s.theme_use('clam')

# Configure the style of Heading in Treeview widget

    menubar=Menu(bw)
    bw.configure(menu=menubar)

    book=Menu(menubar)


    menubar.add_cascade(label='Library',menu=book)




    book.add_command(label='Book Registration',command=book_window)
    book.add_command(label='Exit',command=bw.destroy)




    s.configure('Treeview.Heading', background="green3")
    lbltop=Label(bw,text="BOOK REGISTRATION",font=('bold',40))
    lbltop.grid(row=0,column=0,padx=450,pady=40)
    frm=Frame(bw,height=600,width=1000,bd=2)
    frm.grid(row=1,column=0)
    frm.grid_propagate(0)

    txtid_value=StringVar()
    txtbn_value=StringVar()
    txtcat_value=StringVar()
    txtath_value=StringVar()
    txtprc_value=StringVar()
    txtisbn_value=StringVar()


    lblid=Label(frm,text='BOOK ID',font=('bold',14),fg='Red')
    lblid.grid(row=0,column=0,padx=5,pady=30)
    txtid=Entry(frm,font=('bold',15),textvariable=txtid_value)
    txtid.grid(row=0,column=1,padx=30)

    lblbn=Label(frm,text='BOOK NAME',font=('bold',14),fg='Red')
    lblbn.grid(row=0,column=2,padx=5,pady=30)
    txtbn=Entry(frm,font=('bold',15),textvariable=txtbn_value)
    txtbn.grid(row=0,column=3,padx=30)





    lblcat=Label(frm,text='BOOK CATEGORY',font=('bold',14),fg='black')
    lblcat.grid(row=1,column=0,padx=5,pady=30)
    txtcat=ttk.Combobox(frm,font=('bold',15),textvariable=txtcat_value)
    txtcat.grid(row=1,column=1,padx=30)
    txtcat['values']=('Select','Programming Books','MS office',"Accounting Book","Management Book","science book")
    txtcat.current()

    lblath=Label(frm,text='AUTHOR',font=('bold',14),fg='black')
    lblath.grid(row=1,column=2,padx=5,pady=30)
    txtath=Entry(frm,font=('bold',15),textvariable=txtath_value)
    txtath.grid(row=1,column=3,padx=30)




    lblprc=Label(frm,text='PRICE',font=('bold',14),fg='red')
    lblprc.grid(row=2,column=0,padx=5,pady=30)
    txtprc=Entry(frm,font=('bold',15),textvariable=txtprc_value)
    txtprc.grid(row=2,column=1,padx=30)

    lblisbn=Label(frm,text='ISBN',font=('bold',14),fg='Red')
    lblisbn.grid(row=2,column=2,padx=5,pady=30)
    txtisbn=Entry(frm,font=('bold',15),textvariable=txtisbn_value)
    txtisbn.grid(row=2,column=3,padx=30)







    def submit_book():
        mannu.insert_book(txtid_value.get(),txtbn_value.get(),txtcat_value.get(),txtath_value.get(),txtprc_value.get(),txtisbn_value.get(),'AV')
        messagebox.showinfo('Success!',"Data Inserted Successfully..",parent=bw)

    def update_book():
        mannu.update_book(txtbn_value.get(),txtcat_value.get(),txtath_value.get(),txtprc_value.get(),txtisbn_value.get(),'AV',txtid_value.get())
        messagebox.showinfo('success',"data updation successfully....",parent=bw)

    def delete_book():
        mannu.delete_book(txtid_value.get(),)
        messagebox.showinfo('Success',"data deleted successfully.....)",parent=bw)










    btn=Button(frm,text="SUBMIT",command=submit_book)
    btn.grid(row=3,column=0)
    btn1=Button(frm,text="UPDATE",command=update_book)
    btn1.grid(row=3,column=1)
    btn2=Button(frm,text="DELETE",command=delete_book)
    btn2.grid(row=3,column=2)
    btn3=Button(frm,text="CLOSE",command=bw.destroy)
    btn3.grid(row=3,column=3)



    #events are called

    def selectbookfield(event):
            txtid.delete(0,END)
            txtbn.delete(0,END)
            txtcat.delete(0,END)
            txtath.delete(0,END)
            txtprc.delete(0,END)
            txtisbn.delete(0,END)
            index=trv.focus()
            r =trv.item(index,'values')

            txtid.insert(END,r[0])
            txtbn.insert(END,r[1])
            txtcat.insert(END,r[2])
            txtath.insert(END,r[3])
            txtprc.insert(END,r[4])
            txtisbn.insert(END,r[5])

    def getlibrary(event):
        for item in trv.get_children():
            trv.delete(item)
        for row in mannu.show_book():
            trv.insert('',END,values=row)
    trv=ttk.Treeview(frm,columns=('bookid','bookname','bookcategory','author','price','isbn'))


    #treeview_column
    trv.column('#0',minwidth=0,width=0)
    trv.column('bookid',width=50,anchor=CENTER)
    trv.column('bookname',width=100,anchor=CENTER)
    trv.column('bookcategory',width=200,anchor=CENTER)
    trv.column('author',width=200,anchor=CENTER)
    trv.column('price',width=50,anchor=CENTER)
    trv.column('isbn',width=100,anchor=CENTER)




    #treeview_heading
    trv.heading('#0',text='')
    trv.heading('bookid',text='Book ID')
    trv.heading('bookname',text='Name')
    trv.heading('bookcategory',text='Category')
    trv.heading('author',text='Author')
    trv.heading('price',text='Price')
    trv.heading('isbn',text='ISBN')
    trv.grid(row=4,columnspan=4)
    trv.bind('<Enter>',getlibrary)
    trv.bind('<<TreeviewSelect>>',selectbookfield)












def member_window():
    mw=Toplevel(window)
    mw.title("Member login page")
    from tkinter import messagebox
    mw.state('zoomed')
    mw.configure(bg='grey')
    s = ttk.Style()
    s.theme_use('clam')

    #Configure the style of Heading in Treeview widget

    menubar=Menu(mw)
    mw.configure(menu=menubar)

    member=Menu(menubar)


    menubar.add_cascade(label='member registration',menu=member)




    member.add_command(label='member Registration',command=member_window)
    member.add_command(label='Exit',command=mw.destroy)




    s.configure('Treeview.Heading', background="grey3")
    lbltop=Label(mw,text="member registration page",font=('bold',40))
    lbltop.grid(row=0,column=0,padx=450,pady=40)

    frm=Frame(mw,height=600,width=1000,bd=2)
    frm.grid(row=1,column=0)
    frm.grid_propagate(0)

    txtmid_value=StringVar()
    txtname_value=StringVar()
    txtemail_value=StringVar()
    txtmobile_value=StringVar()
    txtaddress_value=StringVar()
    txtpassword_value=StringVar()


    lblmid=Label(frm,text='MEMBER ID',font=('bold',14),fg='BLACK')
    lblmid.grid(row=0,column=0,padx=5,pady=30)
    txtmid=Entry(frm,font=('bold',15),textvariable=txtmid_value)
    txtmid.grid(row=0,column=1,padx=30)

    lblname=Label(frm,text='NAME',font=('bold',14),fg='black')
    lblname.grid(row=0,column=2,padx=5,pady=30)
    txtname=Entry(frm,font=('bold',15),textvariable=txtname_value)
    txtname.grid(row=0,column=3,padx=30)





    lblemail=Label(frm,text='EMAIL',font=('bold',14),fg='black')
    lblemail.grid(row=1,column=0,padx=5,pady=30)
    txtemail=Entry(frm,font=('bold',15),textvariable=txtemail_value)
    txtemail.grid(row=1,column=1,padx=30)


    lblmobile=Label(frm,text='MOBILE',font=('bold',14),fg='black')
    lblmobile.grid(row=1,column=2,padx=5,pady=30)
    txtmobile=Entry(frm,font=('bold',15),textvariable=txtmobile_value)
    txtmobile.grid(row=1,column=3,padx=30)




    lbladdress=Label(frm,text='ADDRESS',font=('bold',14),fg='black')
    lbladdress.grid(row=2,column=0,padx=5,pady=30)
    txtaddress=Entry(frm,font=('bold',15),textvariable=txtaddress_value)
    txtaddress.grid(row=2,column=1,padx=30)

    lblpassword=Label(frm,text='PASSWORD',font=('bold',14),fg='black')
    lblpassword.grid(row=2,column=2,padx=5,pady=30)
    txtpassword=Entry(frm,font=('bold',15),textvariable=txtpassword_value)
    txtpassword.grid(row=2,column=3,padx=30)



    def submit_member():

        mannu.insert_member(txtmid_value.get(),txtname_value.get(),txtemail_value.get(),txtpassword_value.get(),txtmobile_value.get(),txtaddress_value.get(),)
        messagebox.showinfo('Success!',"Data Inserted Successfully..",parent=mw)
        txtmid.delete(0)
    def update_member():
        mannu.update_member(txtname_value.get(),txtemail_value.get(),txtpassword_value.get(),txtmobile_value.get(),txtaddress_value.get(),txtmid_value.get())
        messagebox.showinfo('success',"data updation successfully....",parent=mw)

    def delete_member():
        mannu.delete_member(txtmid_value.get(),)
        messagebox.showinfo('Success',"data deleted successfully.....)",parent=mw)


    def getregistration():
        result=mannu.show_member(txtmid_value.get(),txtname_value.get(),txtemail_value.get(),txtpassword_value.get(),txtmobile_value.get(),txtaddress_value.get())
        if result:
            messagebox.showinfo('Info',"Login Successfully")
            member_window()
        else:
            messagebox.showerror('Error',"Invalid User")


    btn=Button(frm,text="SUBMIT",command=submit_member)
    btn.grid(row=3,column=0)

    btn=Button(frm,text="UPDATE",command=update_member)
    btn.grid(row=3,column=1)

    btn=Button(frm,text="close",command=mw.destroy)
    btn.grid(row=3,column=3)

    btn=Button(frm,text="delete",command=delete_member)
    btn.grid(row=3,column=2)

    def selectmemberfield(event):
            txtmid.delete(0,END)
            txtname.delete(0,END)
            txtemail.delete(0,END)
            txtpassword.delete(0,END)
            txtmobile.delete(0,END)
            txtaddress.delete(0,END)
            index=trv.focus()
            r =trv.item(index,'values')

            txtmid.insert(END,r[0])
            txtname.insert(END,r[1])
            txtemail.insert(END,r[2])
            txtpassword.insert(END,r[3])
            txtmobile.insert(END,r[4])
            txtaddress.insert(END,r[5])

    def getmembers(event):
        for item in trv.get_children():
            trv.delete(item)
        for row in mannu.show_member():
            trv.insert('',END,values=row)
    trv=ttk.Treeview(frm,columns=('memberid','membername','email','password','mobile','address'))


    #treeview_column
    trv.column('#0',minwidth=0,width=0)
    trv.column('memberid',width=50,anchor=CENTER)
    trv.column('membername',width=100,anchor=CENTER)
    trv.column('email',width=200,anchor=CENTER)
    trv.column('password',width=200,anchor=CENTER)
    trv.column('mobile',width=50,anchor=CENTER)
    trv.column('address',width=100,anchor=CENTER)




    #treeview_heading
    trv.heading('#0',text='')
    trv.heading('memberid',text='Member ID')
    trv.heading('membername',text='Name')
    trv.heading('email',text='Email')
    trv.heading('password',text='password')
    trv.heading('mobile',text='Mobile')
    trv.heading('address',text='address')
    trv.grid(row=4,columnspan=4)
    trv.bind('<Enter>',getmembers)
    trv.bind('<<TreeviewSelect>>',selectmemberfield)







def bissue_window():
    biw=Toplevel(window)
    biw.title("BOOK ISSUE PAGE")
    from tkinter import messagebox
    biw.state('zoomed')
    biw.configure(bg='grey')
    s = ttk.Style()
    s.theme_use('clam')

        # Configure the style of Heading in Treeview widget

    menubar=Menu(biw)

    biw.configure(menu=menubar)
    i_r=Menu(menubar)

    menubar.add_cascade(label="Book Issue & Return",menu=i_r)


    i_r.add_command(label='book entries',command=bissue_window)
    i_r.add_separator()
    i_r.add_command(label='Exit',command=biw.destroy)






    s.configure('Treeview.Heading', background="pink")
    lbltop=Label(biw,text="BOOK ISSUE PAGE",font=('bold',20))
    lbltop.grid(row=0,column=0,padx=10,pady=10)

    frm=Frame(biw,height=900,width=2000,bd=2)
    frm.grid(row=1,column=0)
    frm.grid_propagate(0)



    txtmemid_value=StringVar()
    txtmname_value=StringVar()
    txtbkid_value=StringVar()
    txtbn_value=StringVar()
    txtprc_value=StringVar()
    txtmobile_value=StringVar()
    txtemail_value=StringVar()
    txtath_value=StringVar()
    txtisdt_value=StringVar()
    txtdt_value=StringVar()



########
    def get_member(event):

        txtmname.delete(0,END)
        txtmobile.delete(0,END)
        txtemail.delete(0,END)


        result=mannu.getmemberdetail(txtmemid_value.get(),)
        for r in result:
            txtmname.insert(END,r[1])
            txtemail.insert(END,r[2])
            txtmobile.insert(END,r[4])
#bookdeatail function starts from here

    def get_book(event):

        txtbn.delete(0,END)
        txtprc.delete(0,END)
        txtath.delete(0,END)

        result=mannu.getbookdetail(txtbkid_value.get(),)
        for r in result:
            txtbn.insert(END,r[1])
            txtath.insert(END,r[3])
            txtprc.insert(END,r[4])
##################
    lblmemid=Label(frm,text='MEMBER ID',font=('bold',10),fg='BLACK')
    lblmemid.grid(row=0,column=0,padx=25,pady=20)
    txtmemid=Entry(frm,font=('bold',10),textvariable=txtmemid_value)
    txtmemid.grid(row=0,column=1)

    #its used in case of above get_member types method
    txtmemid.bind('<KeyRelease>',get_member)
    #its used in case of above get_member types method

    lblmname=Label(frm,text=' MEMBER NAME',font=('bold',10),fg='black')
    lblmname.grid(row=1,column=0,padx=25,pady=20)
    txtmname=Entry(frm,font=('bold',10),textvariable=txtmname_value)
    txtmname.grid(row=1,column=1)



########
    lblbkid=Label(frm,text='BOOK ID',font=('bold',10),fg='Red')
    lblbkid.grid(row=0,column=2,padx=25,pady=20)
    txtbkid=Entry(frm,font=('bold',10),textvariable=txtbkid_value)
    txtbkid.grid(row=0,column=3)
    #its used in case of above get_book types method
    txtbkid.bind('<KeyRelease>',get_book)
    #its used in case of above get_book types method


    lblbn=Label(frm,text='BOOK NAME',font=('bold',10),fg='Red')
    lblbn.grid(row=1,column=2,padx=25,pady=20)
    txtbn=Entry(frm,font=('bold',10),textvariable=txtbn_value)
    txtbn.grid(row=1,column=3)
###############
    lblprc=Label(frm,text='PRICE',font=('bold',10),fg='red')
    lblprc.grid(row=2,column=2,padx=25,pady=20)
    txtprc=Entry(frm,font=('bold',10),textvariable=txtprc_value)
    txtprc.grid(row=2,column=3)


    lblmobile=Label(frm,text='MOBILE',font=('bold',10),fg='black')
    lblmobile.grid(row=2,column=0,padx=25,pady=20)
    txtmobile=Entry(frm,font=('bold',10),textvariable=txtmobile_value)
    txtmobile.grid(row=2,column=1)


###############
    lblemail=Label(frm,text='EMAIL',font=('bold',10),fg='black')
    lblemail.grid(row=3,column=0,padx=25,pady=20)
    txtemail=Entry(frm,font=('bold',10),textvariable=txtemail_value)
    txtemail.grid(row=3,column=1)

    lblath=Label(frm,text='AUTHOR',font=('bold',10),fg='black')
    lblath.grid(row=3,column=2,padx=25,pady=20)
    txtath=Entry(frm,font=('bold',10),textvariable=txtath_value)
    txtath.grid(row=3,column=3)
#######################
    lblisdt=Label(frm,text="ISSUE DATE",font=('bold',10))
    lblisdt.grid(row=4,column=0,padx=25,pady=20)
    txtisdt=Entry(frm,font=('bold',10),textvariable=txtisdt_value)
    txtisdt.grid(row=4,column=1)

    lbldt=Label(frm,text="RETURN DATE",font=('bold',10))
    lbldt.grid(row=4,column=2,padx=25,pady=20)
    txtdt=Entry(frm,font=('bold',10),textvariable=txtdt_value)
    txtdt.grid(row=4,column=3)
#######################




    def changebookstatus():
        mannu.upatestatus('ISSUED',txtbkid_value.get())

    def submit_issuedbook():
        changebookstatus()
        mannu.insert_issuedbook(txtmemid_value.get(),txtmname_value.get(),txtbkid_value.get(),txtbn_value.get(),txtprc_value.get(),txtmobile_value.get(),txtemail_value.get(),txtath_value.get(),txtisdt_value.get(),txtdt_value.get(),'ISSUED')
        messagebox.showinfo('Success!',"Data Inserted Successfully..",parent=biw)
        txtmemid.delete(0)

    btn=Button(frm,text="SUBMIT",command=submit_issuedbook)
    btn.grid(row=5,column=0)

    def selectissuedbookfield(event):

            txtmemid.delete(0,END)
            txtmname.delete(0,END)
            txtbkid.delete(0,END)
            txtbn.delete(0,END)
            txtprc.delete(0,END)
            txtmobile.delete(0,END)
            txtemail.delete(0,END)
            txtath.delete(0,END)
            txtisdt.delete(0,END)
            txtdt.delete(0,END)
            index=10
            r =trv.item(index,'values')



            txtmemid.insert(END,r[0])
            txtmname.insert(END,r[2])
            txtbkid.insert(END,r[1])
            txtbn.insert(END,r[3])
            txtprc.insert(END,r[5])
            txtmobile.insert(END,r[4])
            txtemail.insert(END,r[6])
            txtath.insert(END,r[7])
            txtisdt.insert(END,r[8])
            txtdt.insert(END,r[9])


    def getissuebook(event):
        for item in trv.get_children():
            trv.delete(item)
        for row in mannu.show_issuedbook():
            trv.insert('',END,values=row)
    trv=ttk.Treeview(frm,columns=('memberid','membername','bookid','bookname','bookprice','mobile','email','author','issuedate','returndate'))


    #treeview_column
    trv.column('#0',minwidth=0,width=0)
    trv.column('memberid',width=70,anchor=CENTER)
    trv.column('membername',width=150,anchor=CENTER)
    trv.column('bookid',width=50,anchor=CENTER)
    trv.column('bookname',width=150,anchor=CENTER)
    trv.column('bookprice',width=70,anchor=CENTER)
    trv.column('mobile',width=100,anchor=CENTER)
    trv.column('email',width=150,anchor=CENTER)
    trv.column('author',width=100,anchor=CENTER)
    trv.column('issuedate',width=100,anchor=CENTER)
    trv.column('returndate',width=100,anchor=CENTER)





    #treeview_heading
    trv.heading('#0',text='')
    trv.heading('memberid',text='Member ID')
    trv.heading('membername',text='Member Name')
    trv.heading('bookid',text='Book ID')
    trv.heading('bookname',text='Book Name')
    trv.heading('bookprice',text='Book Price')
    trv.heading('mobile',text='Mobile')
    trv.heading('email',text='Email')
    trv.heading('author',text='Author')
    trv.heading('issuedate',text='Issue date')
    trv.heading('returndate',text='Return date')

    trv.grid(row=6,columnspan=6,padx=80)
    trv.bind('<Enter>',getissuebook)
    trv.bind('<<TreeviewSelect>>',selectissuedbookfield)













def getlogin():
    result=mannu.show_user(txtid_value.get(),txtpass_value.get())
    if result:
     messagebox.showinfo('Info',"Login Successfully")
     book_window()
    else:
     messagebox.showerror('Error',"Invalid User")


btn=Button(frm,text="Login",command=getlogin,bg='khaki4')
btn.grid(row=2,column=0,pady=20)

btn=Button(frm,text="UPDATE",command=book_window,bg='khaki4')
btn.grid(row=2,column=1,pady=20)

btn=Button(frm,text="NEXT",command=member_window,bg='khaki4')
btn.grid(row=2,column=2,padx=20)

btn=Button(frm,text="issue book",command=bissue_window,bg='khaki4')
btn.grid(row=2,column=3,padx=20)




window.mainloop()
