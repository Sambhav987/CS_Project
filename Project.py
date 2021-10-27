import pandas as pd
print('----------------WELCOME TO HOTEL MANAGEMENT SYSTEM-----------------')
flag=True
while(flag):
    print('-------------SELECT THE OPTION AS PER YOUR REQUIREMENT------------')
    print('PRESS 1 TO INSERT NEW RECORD')
    print('PRESS 2 TO VIEW ALL THE RECORDS')
    print('PRESS 3 TO SEARCH A RECORD BY HOTEL')
    print('PRESS 4 TO SEARCH A RECORD BY CUSTOMER NAME')
    print('PRESS 5 TO SEARCH A RECORD BY CHECK IN DATE')
    print('PRESS 6 TO SEARCH A RECORD BY CHECK OUT DATE')
    print('PRESS ANY OTHER NUMBER TO QUIT')
    choice=int(input('ENTER YOUR CHOICE:'))
    if choice==1:
        HOTEL=input("ENTER THE HOTEL NAME:  ")
        NAME=input("ENTER THE CUSTOMER NAME:  ")
        INDATE=input("ENTER CHECK IN DATE (DD/MM/YY):  ")
        OUTDATE=input("ENTER CHECK OUT DATE (DD/MM/YY) :  ")
        L=[[HOTEL,NAME,INDATE,OUTDATE]]
        df=pd.DataFrame(L)
        df.to_csv("E:\\HOTEL.csv",mode='a',header=False,index=False)
        print('Record Inserted Successfully')
    elif choice==2:
        print('-------DISPLAYING ALL THE HOTEL DETAILS-------------')
        df=pd.read_csv("E:\\HOTEL.csv")
        print(df)
    elif choice==3:
        n=input('ENTER A HOTEL NAME TO SEARCH :  ')
        df=pd.read_csv("E:\\HOTEL.csv",names=['HOTEL','NAME','INDATE','OUTDATE'])
        val=df[df['HOTEL']==n]
        if(val.empty==True):
            print('No Such Customer Exists')
        else:
            print(val)
    elif choice==4:
        n=input('ENTER CUSTOMER NAME TO SEARCH :  ')
        df=pd.read_csv("E:\\HOTEL.csv",names=['HOTEL','NAME','INDATE','OUTDATE'])
        val=df[df['NAME']==n]
        if(val.empty==True):
            print('No Such Customer Exists')
        else:
            print(val)
    elif choice==5:
        n=input('ENTER CHECK-IN DATE (DD/MM/YY) TO SEARCH :  ')
        df=pd.read_csv("E:\\HOTEL.csv",names=['HOTEL','NAME','INDATE','OUTDATE'])
        val=df[df['INDATE']==n]
        if(val.empty==True):
            print('No Such Customer Exists')
        else:
            print(val)
    elif choice==6:
        n=input('ENTER CHECK-OUT DATE (DD/MM/YY) TO SEARCH :  ')
        df=pd.read_csv("E:\\HOTEL.csv",names=['HOTEL','NAME','INDATE','OUTDATE'])
        val=df[df['OUTDATE']==n]
        if(val.empty==True):
            print('No Such Customer Exists')
        else:
            print(val)
    else:
        print('THANK YOU FOR USING HOTEL MANAGEMENT SYSTEM')
        flag=False
