def bank(path):
    global data,all_que
    data=[]                    
    all_e=[]
    all_que=[]
    f=open(path,"r")
    a=f.readlines()
    l1=[]
    for x in a:
        sx=x.split("\n")
        l1.append(sx)

    for y in l1:
        p=y[0]
        all_e.append(p)

    length=len(all_e)

    for q in range(0,length,6):
        all_que.append(all_e[q])
    
    for g in all_que:
        if g in all_e:
            inde=all_e.index(g)

            try:
                op1=all_e[inde+1]
                op2=all_e[inde+2]
                op3=all_e[inde+3]
                op4=all_e[inde+4]
                ans=all_e[inde+5]
                lst=[g,op1,op2,op3,op4,ans]
            except IndexError:
                pass
            data.append(lst)
    

    
    f.close()
    return data














