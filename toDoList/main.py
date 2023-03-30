import tkinter 
from tkinter import *
from datetime import date

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []
dailytask_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        if var1.get() == 1:
            #add error cannot have date for daily 
            #if len(date_entry.get()) != 0:
                
            task = "(DAILY) " + task
            with open('dailytasklist.txt', 'a') as taskfile:
                taskfile.write(f"\n{task}")
            task_list.append(task)
            listbox.insert(END,task)
        else:
            if len(date_entry.get()) != 0:
                task = task + " " + str(date_entry.get()) + "*"
            with open('tasklist.txt', 'a') as taskfile:
                taskfile.write(f"\n{task}")
            task_list.append(task)
            listbox.insert(END,task)
            

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))

    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w')as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)  
    else:
        listbox.delete(ANCHOR)  
        
def deleteDailyTask():
    global dailytask_list
    task = str(listbox.get(ANCHOR))
    if task in dailytask_list:
        with open("dailytasklist.txt",'w')as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)  

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
               
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file=open('tasklist.txt', 'w')
        file.close()

def openDailyTasks():
    try: 
        global dailytask_list
        with open("dailytasklist.txt" , "r") as taskfile:
            dailytasks = taskfile.readlines()
        for dailytask in dailytasks:
            if dailytask != '\n':
                dailytask_list.append(dailytask)
                listbox.insert(END, dailytask)
    except:
        file=open('dailytasklist.txt', 'w')
        file.close()
    
## not working deletes task on new startup 






##### GUI ###### 
#icon
Image_icon = PhotoImage(file="Image/icon.png")
root.iconphoto(False, Image_icon)

#topbar
TopImage=PhotoImage(file="Image/topbar.png")
Label(root,image=TopImage).pack()

#dockimage
DockImage =PhotoImage(file="Image/dock.png")
Label(root, image=DockImage, bg ="#32405b").place(x=30,y=25)

#noteimage
#NoteImage = PhotoImage(file="Image/icon.png")
#Label(root, image=NoteImage, bg ="#32405b").place(x=30,y=25)

heading = Label(root,text="Tasks for today",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=125,y=20)

#####mainFrame
frame = Frame(root,width=400,height=50, bg="white")
frame.place(x =0, y=100)

#input text box for task 
task=StringVar()
task_entry = Entry(frame,width=18,font="arial 20",bg ="#E0E6E9",bd=0)
task_entry.place(x=10,y=8)
task_entry.focus()

#add button
button = Button(frame,text="NEW TASK", font="arial 14 bold", width=8, bg="#79C4FC", fg="#fff", bd=0,command=addTask)
button.place(x=295, y=8)


####Frame 2
#area beneath add button 
frame2 = Frame(root, bd= 3, width = 700, height =80)
frame2.pack(pady=(70,0))

#everyday checkbox
var1 = IntVar()
checkButton = Checkbutton(frame2, text="Daily", variable=var1, font="arial 12")
checkButton.place(x = 10, y= 5)

#date picker 
T = Label(frame2, text ="Date(DD/MM/YY)", width = 20, font="arial 12")
T.place(x = 85, y = 6)

date=StringVar()
date_entry = Entry(frame2,width=13,font="arial 15",bg ="#E0E6E9",bd=0)
date_entry.place(x=245,y=6)
date_entry.focus()


#remove a daily task 
button = Button(frame2,text="REMOVE DAILY TASK", font="arial 10 bold", width=25, bg="#D5D9DB", fg="#fff", bd=0, command = deleteDailyTask)
button.place(x = 100, y =40)

####Frame1
#listbox where tasks are 
frame1=Frame(root,bd=3, width=700, height=200, bg="#32405b")
frame1.pack(pady=(10,0))

#scrollbar for listbox
listbox= Listbox(frame1, font=('arial',12),width=40, height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#delete button 
Delete_icon=PhotoImage(file="Image/complete.png")
Button(root, image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)

openDailyTasks()
openTaskFile()

root.mainloop()