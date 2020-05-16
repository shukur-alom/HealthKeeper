import datetime
saw=int(input('\n\nDo you want to add \n\nAdd  -- 1\nRead -- 2\nDelete Deta -- 3\n\ninformation ?\nChosse a number: '))
User=int(input("\n\nWhose information do you want to work with?\nNaima -- 1\nMaria -- 2\nSafwan  -- 3\nChoise a number: ")) # Input Your 3 name
user1=int(input("\n\nDo you want to add \n\nFood     -- 1\nExersise -- 2\n\ninformation?\nchosse a number: "))
k= datetime.datetime.now()
def ser():
    print('\n\t\t\t\t\tSuccessfully Added\n\n')
def rty():
    print('\n\t\t\t\t\tSuccessfully Deleted\n\n')
if saw==1:
    write=input('\n\nAdd something:\n')
    if User==1 and user1 ==1:
        n=open('naima.txt','a') 
        n.write('Date: '+str(k.date())+' Time: '+str(k.time())+' :- '+write+'\n')
        n.close()
        ser()
    elif User==1 and user1==2:
        ne=open('naimae.txt','a')
        ne.write('Date: '+str(k.date())+' Time: '+str(k.time())+' :- '+write+'\n')
        ne.close()    
        ser()
    elif User==2 and user1 ==1:
        m=open('maria.txt','a')
        m.write('Date: '+str(k.date())+' Time: '+str(k.time())+' :- '+write+'\n')
        m.close()
        ser()
    elif User==2 and user1==2:
        me=open('maria.txt','a')
        me.write('Date: '+str(k.date())+' Time: '+str(k.time())+' :- '+write+'\n')
        me.close()    
        ser() 
    elif User==3 and user1 ==1:
        s=open('safu.txt','a')
        s.write('Date: '+str(k.date())+' Time: '+str(k.time())+' :- '+write+'\n')
        s.close()
        ser()
    elif User==3 and user1==2:
        se=open('safue.txt','a')
        se.write('Date: '+str(k.date())+' Time: '+str(k.time())+' :- '+write+'\n') 
        se.close()  
        ser()
elif saw==2:
    if  User==1 and user1==1:
        n_=open('naima.txt')
        print(n_.read())
        n_.close()
    elif User==1 and user1==2:
        ne_=open('naimae.txt')
        print(ne_.read())
        ne_.close()
    elif User==2 and user1==1:
        m_=open('maria.txt')
        print(m_.read())
        m_.close()
    elif User==2 and user1==2:
        me_=open('mariae.txt')
        print(me_.read())
        me_.close()
    elif User==3 and user1==1:
        s_=open('safu.txt')
        print(s_.read())
        s_.close()
    elif User==3 and user1==2:
        se_=open('safue.txt')
        print(se_.read())
        se_.close()
elif saw==3:
    if User==1 and user1 ==1:
        q=open('naima.txt','w')
        q.write("")
        q.close()
        rty()
    elif User==1 and user1==2:
        e=open('naimae.txt','w')
        e.write("")
        e.close()  
        rty()  
    elif User==2 and user1 ==1:
        lh=open('maria.txt','w')
        lh.write("")
        lh.close()
        rty()
    elif User==2 and user1==2:
        mre=open('maria.txt','w')
        mre.write("")
        mre.close()    
        rty()
    elif User==3 and user1 ==1:
        stry=open('safu.txt','w')
        stry.write("")
        stry.close()  
        rty()         
    elif User==3 and user1==2:
        re=open('safue.txt','w')
        re.write("") 
        re.close()  
        rty()