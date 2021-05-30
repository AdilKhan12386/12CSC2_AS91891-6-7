
from tkinter import *
names = []


class Quiz:
    def __init__(self, parent):
 
        background_color="Darkolivegreen2"

        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()
               
        #widgets set up
        self.heading_label=Label(self.quiz_frame, text="Welcome to the NCEA Level 2 Study Guide",bd=10, relief="ridge", font=("Ariel","25"))
        self.heading_label.grid(row=0, padx=225)
        #Doesn't work: self.heading_label.place(relx = 0.5, rely = 0.5, anchor = centre)
            
        
        #Username label
        self.user_label=Label(self.quiz_frame, text="Please enter your username below: ", font=("Tw Cen MT","18"),bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=50) 
        
        #entry box set up
        self.entry_box=Entry(self.quiz_frame, font=("Ariel","18"))
        self.entry_box.grid(row=2,padx=50, pady=0)
        
        
        #continue button #gap for easy visability
        self.continue_button = Button(self.quiz_frame, text="Continue",bd=10, relief="raised", font=("Ariel", "20", "bold"),
                                      compound = "c", bg="midnight blue", fg = "white", command=self.name_collection)
        self.continue_button.grid(row=3, padx=50, pady=200, sticky = E)
        

        #Exit button #gap for easy visability
        self.exit_button = Button(self.quiz_frame, text="Exit", bd=10, relief="raised", font=("Ariel", "20", "bold"),
                                  compound = "c", bg="Firebrick4", fg = "white", command=root.destroy)
        self.exit_button.grid(row=3, padx=50, pady=200, sticky = W)

    def name_collection(self):
        name=self.entry_box.get()
        names.append(name)
        root.destroy()

      
           

if __name__ == "__main__":
    root = Tk()
    root.title("NCEA L2 Study Guide") 

    quiz_instance = Quiz(root)
    root.mainloop()
