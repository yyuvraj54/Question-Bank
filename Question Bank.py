from tkinter import *
import os
import build

'''
mysql_login=Tk()

mysql_login.geometry("463x200+400+120")
mysql_login.maxsize(463,200)
mysql_login.minsize(463,200)
mysql_login.title("QB")

def Exit():
        mysql_login.destroy()
def Close():
        print(tmsg.showinfo("mysql acess","mysql connection centre closed"))
        mysql_login.destroy()



mysql_login.config(bg="#ffffff")

sqlabel=Label(mysql_login,text="MYSQL LOGIN",font="20",bg="#ffffff",fg="#739cc7").pack()
passpara=Label(mysql_login,text="FILL ALL DETAILS TO PASS MYSQL PARAMETERS",bg="#ffffff").pack(side=TOP)
notify_l=Label(mysql_login,text="Enter Your Password",font="10",bg="#ffffff",fg="#47d3a3").pack(side=BOTTOM,anchor="ne",padx=150)

#FRAMES AND LABELS
mysql_entry_frame=Frame(mysql_login,bg="#ffffff")
mysql_entry_frame.pack(side=LEFT)
passwdlabel=Label(mysql_entry_frame , text="Name :"  ,font="20",bg="#ffffff").grid(row=2,column=0)
hostlabel=Label(mysql_entry_frame , text="HOSTNAME :",font="20",bg="#ffffff").grid(row=0,column=0)
userlabel=Label(mysql_entry_frame , text="USERNAME :" ,font="20",bg="#ffffff").grid(row=1,column=0)
passwdlabel=Label(mysql_entry_frame , text="PASSWORD :"  ,font="20",bg="#ffffff").grid(row=3,column=0)            

#ENTRY FIELD VALUE CLASS
from rule import entrydefault       #default values
global hostvalue,myuservalue,passvalue
hostvalue=entrydefault.StringVar2()
myuservalue=entrydefault.StringVar1()
passvalue=StringVar()

#ENTRY FIELD
name=StringVar()
Name=Entry(mysql_entry_frame , textvariable=name).grid(row=2,column=1)
hostentry=Entry(mysql_entry_frame , textvariable=hostvalue).grid(row=0,column=1)
userentry=Entry(mysql_entry_frame , textvariable=myuservalue).grid(row=1,column=1)
passwdentry=Entry(mysql_entry_frame , show="*",textvariable=passvalue).grid(row=3,column=1)


butframe=Frame(mysql_login,bg="#ffffff")
butframe.pack(side=RIGHT,fill="y")

connect_button=Button(butframe,text="Connect",relief=FLAT,borderwidth=2,highlightthickness=0,highlightbackground="#ffffff",font = ("Parchment Regular", 24, "bold"))
connect_button.pack(side=RIGHT,padx=15)


mysql_login.mainloop()







#==================================Page 1 Start=======================================================================================================================
'''

root = Tk()
start=PhotoImage(file="thum//start.png")
def scifi():
        scimg.destroy()
        playscbutton.destroy()
        root.destroy()
        build.interface("SCIENCE.txt")
        
        
        
        
        

def landfi():
        lnrimg.destroy()
        playlnrbutton.destroy()
        root.destroy()
        build.interface("LOGIC&REASONING.txt")
        
        
        

def gkfi():
        
        playgkbutton.destroy()
        root.destroy()
        build.interface("GK.txt")
        



def csfi():
        csimg.destroy()
        playcsbutton.destroy()
        root.destroy()
        build.interface("COMPUTER_SCIENCE.txt")
        



def profi():
        proimg.destroy()
        playprobutton.destroy()
        root.destroy()
        build.interface("PRO.txt")
        




def science():
        global s_p
        s_p=PhotoImage(file="thum//sci_p.png")
        
        back.destroy()
        autochange.destroy()
        g1.destroy()
        g2.destroy()
        g3.destroy()
        g4.destroy()
        g5.destroy()
        global scimg, playscbutton
        scimg = Label(root, image = s_p, background = "white")
        scimg.pack()
      
        playscbutton =Button(root, image=start,command = scifi,bg="#e9e733",activebackground="#e9e733",relief=FLAT,bd=0)
        playscbutton.place(relx=0.57,rely=0.75)




def landr():
        back.destroy()
        autochange.destroy()
        g1.destroy()
        g2.destroy()
        g3.destroy()
        g4.destroy()
        g5.destroy()
        global playlnrimg
        global lnrimg, lbllnr, playlnrbutton
        playlnrimg = PhotoImage(file = "thum//lr_p.png")
        lnrimg = Label(root, image = playlnrimg,bd=0)
        lnrimg.pack()

        playlnrbutton = Button(root, image=start, command = landfi,bg = "#ec7e01",relief=FLAT,bd=0,activebackground="#ec7e01")
        playlnrbutton.place(relx=0.57,rely=0.75)



        
def gk():
        back.destroy()
        autochange.destroy()
        g1.destroy()
        g2.destroy()
        g3.destroy()
        g4.destroy()
        g5.destroy()
        global playgkimg
        global playgkbutton ,playgkimg_
        playgkimg = PhotoImage(file = "thum//gk_p.png")
        playgkimg_=Label(root,image=playgkimg,bd=0)
        playgkimg_.pack()
        
        playgkbutton = Button(root,image=start, command = gkfi,bg = "white",relief=FLAT,bd=0,activebackground="white")
        playgkbutton.place(relx=0.57,rely=0.75)


def cs():
        back.destroy()
        autochange.destroy()
        
        g1.destroy()
        g2.destroy()
        g3.destroy()
        g4.destroy()
        g5.destroy()
        global playcsimg
        global csimg, lblcs, playcsbutton
        
        
        playcsimg = PhotoImage(file = "thum//cs_p.png")
        csimg = Label(root, image = playcsimg, bd=0)
        csimg.pack()
        
      
        playcsbutton = Button(root, image=start, command = csfi,bg = "white",relief=FLAT,bd=0,activebackground="white")
        playcsbutton.place(relx=0.57,rely=0.75)


def pro():
        back.destroy()
        autochange.destroy()
        g1.destroy()
        g2.destroy()
        g3.destroy()
        g4.destroy()
        g5.destroy()
        
        global playproimg
        global proimg, genrebg, playprobutton
        playproimg = PhotoImage(file = "thum//pro_p.png")
        proimg = Label(root, image = playproimg )
        proimg.pack()
        playprobutton = Button(root, image=start,command = profi,bg = "#4aafde",relief=FLAT,bd=0,activebackground="#4aafde")
        playprobutton.place(relx=0.57,rely=0.75)



def startquiz():
        global radiovar
       
       
        

        radiovar = IntVar()
        radiovar.set(-1)


        global  g1, g2, g3, g4, g5 ,secl,dinamic,lr,gk_,cs_,pro_,sci ,back ,autochange
        secl=PhotoImage(file="thum//select.png")
        dinamic=PhotoImage(file="thum//local.png")

        sci=PhotoImage(file="thum//sci.png")
        lr=PhotoImage(file="thum//lr.png")
        gk_=PhotoImage(file="thum//gk.png")
        cs_=PhotoImage(file="thum//cs.png")
        pro_=PhotoImage(file="thum//pro.png")
        
        back=Label(root,image=secl,bd=0,bg="white")
        back.pack()

        autochange=Label(root,image=dinamic,bd=0,bg="white")
        autochange.place(relx=0.45,rely=0.4)

        def exit_(e):
                autochange['image']=dinamic
        def Enter1(e):
                autochange['image']=sci
        def Enter2(e):
                autochange['image']=lr
        def Enter3(e):
                autochange['image']=gk_
        def Enter4(e):
                autochange['image']=cs_
        def Enter5(e):
                autochange['image']=pro_

        

            
        g1 = Radiobutton(root,text = "SCIENCE",font = ("Ariel", 16),value = 0,variable = radiovar,command = science,bg="#199aca")
        g1.place(relx=0.03,rely=0.34)

        g2 = Radiobutton(root,text = "LOGIC and REASONING",font = ("Ariel", 16),value = 1,variable = radiovar,command= landr,bg="#199aca")
        g2.place(relx=0.03,rely=0.47)


        g3 = Radiobutton(root,text = "GENRAL KNOWLEDGE",font = ("Ariel", 16),value = 2,variable = radiovar,command= gk,bg="#199aca")
        g3.place(relx=0.03,rely=0.6)
    
        g4 = Radiobutton(root,text = "COMPUTER SCIENCE",font = ("Ariel", 16),value = 3,variable = radiovar,command=cs,bg="#199aca")
        g4.place(relx=0.03,rely=0.74)

      
                           
        g5 = Radiobutton(root,text = "PRO",font = ("Ariel", 16),value = 4,variable = radiovar,command= pro,bg="#199aca")
        g5.place(relx=0.03,rely=0.87)

            
        g1.bind('<Enter>', Enter1)
        g1.bind('<Leave>', exit_)
        g2.bind('<Enter>', Enter2)
        g2.bind('<Leave>', exit_)
        g3.bind('<Enter>', Enter3)
        g3.bind('<Leave>', exit_)
        g4.bind('<Enter>', Enter4)
        g4.bind('<Leave>', exit_)
        g5.bind('<Enter>', Enter5)
        g5.bind('<Leave>', exit_)











def pg_value():
    labelimage.destroy()
    playbutton.destroy()
    startquiz()

    
    

#First page layerout
root.geometry("850x590+190+60")
root.title(" Question Bank anagement system")
root.config(background="white")
root.resizable(0,0)
#------------------

## All images
face=PhotoImage(file="thum//face.png")
go=PhotoImage(file="thum//go.png")
#---------------------



labelimage = Label(root,image = face,background = "white")
labelimage.pack(pady=(0,0))

#----buttonos start
playbutton = Button(root, image = go,command=pg_value, relief = FLAT, border = 0,bd=0,bg="#ffae02",activebackground="#ffae02")
playbutton.place(relx=0.5,rely=0.8)
#------------------



root.mainloop()

#=====================Page 1 End==========================================================================================================================================












