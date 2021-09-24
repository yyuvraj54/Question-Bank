from tkinter import *
from bank import banks
from tkinter.ttk import *
import tkinter
import random
from threading import Thread
import time
#from multiprocessing import Process
def interface(sub):
    global pd
    pd=0
    oldq=[]
    point=[]
    def bank_data():
        global ques ,pa
        pa=banks.bank(f"bank//{sub}")
        ques=[]
        for x in pa:
            q=x[0]
            ques.append(q)
        random.shuffle(ques)
    def options(q):
        global opt1,opt2,opt3,opt4,question,ans
        question=q
        for x in pa:
            if x[0]==q:
                opt1=x[1]
                opt2=x[2]
                opt3=x[3]
                opt4=x[4]
                ans=x[5]
        
        

    bank_data()


    def problem():
        global pd 
        
        if pd==10:
            s=("Your Score:",len(point)*10)
            timer.pack_forget()
            lblques.pack_forget()
            opt10.pack_forget()
            opt20.pack_forget()
            opt30.pack_forget()
            opt40.pack_forget()
            lblwar.pack_forget()
            total_score.pack(pady=50)
            
            total_score.config(text=f"Your Score:{len(point)*10}")
            
            
        else:
            #print(ques)
            for x in ques:
                if len(ques)==0:
                    print("questions done")
                    break
                else:   
                    if x not in oldq:
                        options(x)
                        oldq.append(x)
                        ques.remove(x)
                        
                        lblques.config(text=question)
                        opt10.config(text=opt1)
                        opt20.config(text=opt2)
                        opt30.config(text=opt3)
                        opt40.config(text=opt4)
                        break
                        
                    
                    else:
                        lblques.config(text="No DaTA")
                        opt10.config(text="No DaTA")
                        opt20.config(text="No DaTA")
                        opt30.config(text="No DaTA")
                        opt40.config(text="No DaTA")

            pd=pd+1
                        
                
                        
                
            
    def ans_match(anss):
        global sel_ans
        
        if anss==1:
            sel_ans=opt1
        if anss==2:
            sel_ans=opt2
        if anss==3:
            sel_ans=opt3
        if anss==4:
            sel_ans=opt4
        if ans== sel_ans:
            #print("corrrect")
            point.append("1")      
            problem()
            
        else:
      
            problem()
            #print("incorrect")
            
            

    scie=Tk()
    scie.geometry("1300x600+20+30")
    scie.title(" Question Bank Management system")
    scie.config(background="#73b1bc")
    scie.resizable(0,0)
    global quiz
    quiz=PhotoImage(file="thum//quiz.png")
    back_quiz=Label(scie,image=quiz)
    back_quiz.place(relx=0,rely=0)

    total_score=Label(scie,font = ("Consolas", 60, "bold"), background = "#73b1bc")



    timer=tkinter.Label(scie,text="10",bg="#73b1bc",font='50')
    timer.pack(pady=10)

    lblques = Label(scie, text = "This is QUESTION space!", font = ("Consolas", 24, "bold"), background = "#73b1bc")
    lblques.pack(pady=10)


    def ans_get():
        global ans_c
        ans_c=var.get()
        ans_match(ans_c)
        
        
        
        

        
        
        

    def timeing():
        i=16
        
        while i!=0:
            try:
                if var.get()==1:
                    
                    break
                
                elif var.get()==2:
                    
                    break
                
                elif var.get()==3:
                    
                    break
                
                elif var.get()==4:
                    
                    break
                
                else:pass
            except NameError:
                pass
                
            
            timer.config(text=i-1,font=("Arial", 44))
            time.sleep(1)
            i=i-1
        
        if i==0:
            time.sleep(1)
            problem()
            timeing()
        else:
            var.set(3850)
            timeing()
            
            
         
                
               
    


    var =IntVar()
    var.set(3850)

    opt10 =tkinter.Radiobutton(scie, text = "option 1",value=1,variable =var,tristatevalue=0, font = ("Cooper Black", 16, "bold") ,command=ans_get,background = "#73b1bc")
    opt10.pack(pady = (20,20))

    opt20 =tkinter.Radiobutton(scie, text = "option 2",value=2,variable =var,tristatevalue=0, font = ("Cooper Black", 16, "bold"),command=ans_get,background = "#73b1bc")
    opt20.pack(pady = (20,20))

    opt30 =tkinter.Radiobutton(scie, text = "option 3",value=3,variable =var,tristatevalue=0, font = ("Cooper Black", 16, "bold"),command=ans_get,background = "#73b1bc")
    opt30.pack(pady = (20,20))

    opt40 =tkinter.Radiobutton(scie, text = "option 4",value=4,variable =var,tristatevalue=0,font = ("Cooper Black", 16, "bold"),command=ans_get,background = "#73b1bc")
    opt40.pack(pady = (20,20))

    problem()
    lblwar = Label(scie, text = "Hurry! TIME IS TICKING...", font = ("Times", 24, "bold"), background = "#73b1bc", foreground = "red")
    lblwar.pack(pady = (50,50))


    th=Thread(target = timeing)
    th.start()
    scie.mainloop()


