from tkinter import *
from tkinter import ttk
from PIL import Image
import os
import cv2
from MediaPipe import create

def menu():
    root = Tk()
    root.title("Select Excercise")
    root.geometry("370x370")
    
    """
    #Scroll Bar
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH,expand=1)
    
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side = LEFT, fill=BOTH,expand=1)
    
    my_scrollbar = ttk.Scrollbar(main_frame , orient=VERTICAL,command=my_canvas.yview)
    my_scrollbr.pack(side=RIGHT,fill=Y)
    
    my_canvas.configure(yscrollcommand==my_scrollbar.set())
    my_canvas.bind('<Configure>', Lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    
    second_frame = Frame(my_canvas)
    
    
    my_canvas.create_window((0,0),window=second_frame,anchor="nw")
    """
    
    #img = Image.open("bicep.png")
    #img = img.resize((100,100), Image.ANTIALIAS)
    #img.save("temp2.png")
    #images = os.listdir("images")
    #img = PhotoImage(file="temp3.png")
    
    #rows = int(len(images)/3)
    #for i in range(2):
    #    for j in range(3):
        
    def showDemo(video):
        cap = cv2.VideoCapture(video)
        while(cap.isOpened()):
            try:    
              ret, frame = cap.read()
              cv2.imshow('Demo: Press "q" to Exit',frame)
              if cv2.waitKey(50) & 0xFF == ord('q'):
                break
            except:
                break
        
        cap.release()
        cv2.destroyAllWindows()
    
    
    def shoulder():
        root.destroy()
        showDemo("shoulder.mp4")
        create(arg=2)
        from menu import menu
        menu()
        
    def bicep():
        root.destroy()
        showDemo("right.mp4")
        create(arg=3)
        from menu import menu
        menu()
        
    def squat():
        root.destroy()
        showDemo("squat.mp4")
        create(arg=1)
        from menu import menu
        menu()
        
    img1 = PhotoImage(file="temp1.png")
    Button(root, image = img1 ,borderwidth=0, text="Shoulder", command = shoulder ).grid(row=0,column=0,padx=10,pady=70)
    
    img2 = PhotoImage(file="temp2.png")
    Button(root, image = img2 ,borderwidth=0, text="Shoulder", command = bicep).grid(row=0,column=1,padx=10,pady=50)
    
    img3 = PhotoImage(file="temp3.png")
    Button(root, image = img3 ,borderwidth=0, text="Shoulder", command = squat).grid(row=0,column=2,padx=10,pady=10)
    
    Label(root, text = "Shoulders").grid(row=3,column=0,padx=10,pady=1)
    Label(root, text = "Bicep").grid(row=3,column=1,padx=10,pady=1)
    Label(root, text = "Squat").grid(row=3,column=2,padx=10,pady=1)

    #l.config(font =("Courier", 14))
   
    
    # Quit Button
    Quit = Button(root, text = "Quit", width="10", command = root.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.675)

    def backk():
        root.destroy()
        from Select import select 
        select()

    Back = Button(root, text = "Back", width="10", command = backk, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Back.place(anchor ='se',rely=1,relx=0.675)

    footer=Label(root, bg="white",text="GuidePose",fg="black",font="Leelawadee 14")
    footer.place(height=36,width=350,x=50, y=657)
    
    
    root.mainloop()

#menu()






















































































































