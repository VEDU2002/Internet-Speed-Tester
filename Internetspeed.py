from tkinter import *
import speedtest 



def speedcheck():
    sp=speedtest.Speedtest()  #calling Speedtest class from speedtest module
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+"Mbps"  #gives downloading speed
    up=str(round(sp.upload()/(10**6),3))+"Mbps"  #gives uploading speed
    lab_down.config(text=down)
    lab_up.config(text=up)



sp=Tk()  #calling tinker class

sp.title("Internet Speed Tester")

sp.geometry('500x600')

sp.config(bg="Black")

lab=Label(sp,text="Internet Speed Tester",font=("Tahoma",20,"bold"),bg="Black",fg="Red")
lab.place(x=30,y=30,height=50,width=380)

lab=Label(sp,text="Download Speed",font=("Tahoma",20,"bold"),bg="Black",fg="Red")
lab.place(x=30,y=130,height=50,width=380)

lab_down=Label(sp,text="00",font=("Tahoma",20,"bold"),bg="Black",fg="Red")
lab_down.place(x=30,y=200,height=50,width=380)

lab=Label(sp,text="Upload Speed",font=("Tahoma",20,"bold"),bg="Black",fg="Red")
lab.place(x=30,y=290,height=50,width=380)

lab_up=Label(sp,text="00",font=("Tahoma",20,"bold"),bg="Black",fg="Red")
lab_up.place(x=30,y=360,height=50,width=380)

button=Button(sp,text="Check Speed",font=("Tahoma",20,"bold"),relief=RAISED,bg="Green",command=speedcheck)
button.place(x=30,y=460,height=50,width=380)



sp.mainloop()