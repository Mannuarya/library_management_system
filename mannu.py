import sqlite3
def connection():
    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("create table if not exists user(id int primary key,name text, email text,mobile text,password text)")
    mycursor.execute("create table if not exists book(bookid text primary key,bookname text,bookcategory text,auhthor text,price text,ISBN text,status text)")
    mycursor.execute("create table if not exists member(memberid text primary key, name text,email text,password text,mobile text,address text)")
    mycursor.execute("create table if not exists bookissue(memberid text primary key, membername text,bookid text,bookname text,bookprice text,mobile text,email text,author text,issue date,return date,'status')")
    mycursor.execute("insert or ignore into user values('1','Mannu','admin@gmail.com',9876543211,'Admin1234')")
    conn.commit()
    conn.close()
connection()

def insert_issuedbook(memberid,membername,bookid,bookname,bookprice,mobile,email,author,issuedate,returndate,status):
    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("insert or ignore into bookissue values(?,?,?,?,?,?,?,?,?,?,?)",(memberid,membername,bookid,bookname,bookprice,mobile,email,author,issuedate,returndate,'status'))
    conn.commit()
    conn.close()

#insert_issuedbook(1,'manish',1,'python',1400,'766565876','manish@gmail.com','hhhhh','06/12/2002','07/9/2004')


def show_issuedbook():

    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("select * from bookissue")
    row=mycursor.fetchall()
    return row
    conn.close()





def insert_member(Memberid,name,email,password,mobile,address):
    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("insert or ignore into member values(?,?,?,?,?,?)",(Memberid,name,email,password,mobile,address))
    conn.commit()
    conn.close()
#insert_member(4,'mahesh','mahesh1999@gmail.com',456787590,7568986745,'mayurvihar-62 sector15')



def update_member(name,email,password,mobile,address,memberid):
    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("update member set name=?,email=?,password=?,mobile=?,address=? where memberid=?",(name,email,password,mobile,address,memberid))
    conn.commit()
    conn.close()
#update_member('mannu','mannu@gmail2002.com',732462,1234567890,'helloworld',1)





def show_member():

    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("select * from member")
    row=mycursor.fetchall()
    return row
    conn.close()


def delete_member(memberid,):

    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("delete from member where memberid=?",(memberid,))
    conn.commit()
    conn.close()





def insert_book(bookid,bookname,bookcategory,author,price,ISBN,status):
    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("insert or ignore into book values(?,?,?,?,?,?,?)",(bookid,bookname,bookcategory,author,price,ISBN,status))
    conn.commit()
    conn.close()


#insert_book(6,'c#','programming book','robert lafore',1500,'670976')

def update_book(bookname,bookcategory,author,price,ISBN,status,bookid):
    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("update book set bookname=?,bookcategory=?,author=?,price=?,ISBN=?,status=? where bookid=?",(bookname,bookcategory,author,price,ISBN,status,bookid))
    conn.commit()
    conn.close()
#update_book('python','programmingbook','bjarne',1000,'SSEE4353',3)

def delete_book(bookid,):

    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("delete from book where bookid=?",(bookid,))
    conn.commit()
    conn.close()



#connection()
def show_book():
    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("select * from book")
    row=mycursor.fetchall()
    return row
    conn.close()

##delete_book(2,)


#connection()
#print(show_book())



def insert_user(id,name,email,mobile,password):
    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("insert into user values(?,?,?,?,?)",(id,name,email,mobile,password))
    conn.commit()
    conn.close()


#insert_user(4,'mauu','mauu@gmail.com',6546546798,'gyu564689')


#connection()
def update_user(name,email,mobile,password,id):

    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("update user set name=?,email=?,mobile=?,passwoed=? where id=? ",(name,email,mobile,password,id))
    conn.commit()
    conn.close()


#update_user('manandeep','manandeep@gmnail.com',6576587664,'ad123',2)


def delete_user(id,):

    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("delete from user where id=?",(id,))
    conn.commit()
    conn.close()
connection()

def show_user(e,p):

    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("select * from user where email=? and password=?",(e,p))
    row=mycursor.fetchall()
    return row
    conn.close()




    ###################
def getmemberdetail(i,):
    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("select * from member where memberid=?",(i,))
    row=mycursor.fetchall()
    return row

    conn.close()


def getbookdetail(i,):
    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("select * from book where bookid=?",(i,))
    row=mycursor.fetchall()
    return row
    conn.close()


def upatestatus(status,id):
    conn=sqlite3.connect("abcd.db")
    mycursor=conn.cursor()
    mycursor.execute("update book set status=? where bookid=? ",(status,id))
    conn.commit()
    conn.close()


upatestatus('issued',4)
'''delete_user(2,)
for x in show_user():
    print (x)
print(show_user())'''
