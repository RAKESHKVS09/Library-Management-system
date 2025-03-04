
from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
# Add your own database name and password here to reflect in the code
mypass = ""
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=1.5
# Adding a background image
background_image =Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(765,400,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to INVIGA Library\n"+chr(34)+"Today a Reader, Tomorrow a Leader"+chr(34), fg='black', font=('Times new roman',20))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Books", fg='black',font=('times new roman',15), command=addBook)
btn1.place(relx=0.35,rely=0.4, relwidth=0.3,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white',font=('times new roman',15), command=delete)
btn2.place(relx=0.35,rely=0.5, relwidth=0.3,relheight=0.1)
    
btn3 = Button(root,text="View Book List", fg='black',font=('times new roman',15), command=View)
btn3.place(relx=0.35,rely=0.6, relwidth=0.3,relheight=0.1)
    
btn4 = Button(root,text="Return Book",bg='black', fg='white',font=('times new roman',15), command = returnBook)
btn4.place(relx=0.35,rely=0.7, relwidth=0.3,relheight=0.1)
    
btn5 = Button(root,text="Issue Book to Student", fg='black',font=('times new roman',15), command = issueBook)
btn5.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.1)

root.mainloop()
