#later information

#self.image = Image.open("Gradhat.png") 
#        picture = ImageTk.PhotoImage(self.img) 
 #       picture_label.configure(image = picture) 
  #      picture_label.image = image
   #s     picture_label.grid(row = 1)
#self.var1=IntVar()
 #       root.configure(bg = background_color)
#Pil Library for images. Use CMD in the search bar
from tkinter import *
names_bank = []


class Quiz:
    def __init__(self, parent):
 
        background_color="Darkolivegreen2"

        #frame set up
        self.quiz_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
        self.quiz_frame.grid()
               
        #Heading Label
        self.heading_label=Label(self.quiz_frame, text = "Welcome to the NCEA Level 2 Study Guide",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.heading_label.grid(row=0, padx = 225)
            
        
        #Username label
        self.user_label = Label(self.quiz_frame, text = "Please enter your username below: ", font = ("Tw Cen MT","18"),bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=50) 
        
        #entry box set up
        self.entry_box=Entry(self.quiz_frame, font=("Ariel","18"))
        self.entry_box.grid(row=2,padx=50, pady=0)
        
        
        #continue button #gap for easy visability
        self.continue_button = Button(self.quiz_frame, text = "Continue",bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                      compound = "c", bg = "midnight blue", fg = "white", command = self.name_collection)
        self.continue_button.grid(row = 3, padx = 50, pady = 200, sticky = E)
        

        #Exit button #gap for easy visability
        self.exit_button = Button(self.quiz_frame, text = "Exit", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg="Firebrick4", fg = "white", command = root.destroy)
        self.exit_button.grid(row = 3, padx = 50, pady = 200, sticky = W)

        #Error Label
        self.error_label = Label(self.quiz_frame, text = "", font = ("Ariel", "15", "bold"),bg = background_color, fg= "red")
        self.error_label.grid(row = 3,)
        

    def name_collection(self):
        name = self.entry_box.get()
        if str.isalpha(name) == True and len(name) <=16:
            names_bank.append(name) 
            self.quiz_frame.destroy()
            Nav(root)
        else:
            self.error_label.configure(text = "")
            self.error_label.configure(self.quiz_frame, text="Remember your username needs to be non-numerical and between 0-15 letters",
                                       font=("Ariel", "20", "bold"),fg = "red")
           

class Nav:
    def __init__(self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 100)
        self.quiz_frame.grid()

        #Second Heading
        self.nav_label = Label(self.quiz_frame, text = "Welcome, please select one of the given resources",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.nav_label.grid(row=0, padx = 225)

        #Leaderboard Button
        self.Leader_button = Button(self.quiz_frame, text = "Leaderboard Page", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                       compound = "c", bg = "purple4", fg = "white", command = self.move_on)
        self.Leader_button.grid(row = 4, column = 1, padx = 50, pady = 200, sticky = S)

        #Resources Button
        self.resources_button = Button(self.quiz_frame, text = "Resources Page", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                       compound = "c", bg = "purple4", fg = "white", command = self.move_on)
        self.resources_button.grid(row = 3, column = 0, padx = 75, pady = 200, sticky = W)

        #Quiz Button
        self.quiz_button = Button(self.quiz_frame, text = "Quiz Page", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                       compound = "c", bg = "purple4", fg = "white", command = self.move_on)
        self.quiz_button.grid(row = 3, column = 2, padx = 25, pady = 200, sticky = E)

        #Exit button
        self.exit_button = Button(self.quiz_frame, text = "Exit", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg="Firebrick4", fg = "white", command = root.destroy)
        self.exit_button.grid(row = 1, column = 0, sticky = NW)

    def move_on(self):
        if self.resources_button:
            self.quiz_frame.destroy()
            Res_options(root)
        elif self.Leader_button:
            self.quiz_frame.destroy()
            Leaderboard(root)
        elif self.quiz_button:
            self.quiz_frame.destroy()
            quiz_options(root)
        elif choice == self.exit_button:
            self.exit_button
        


class Res_options:
    def __init__(self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #test button
        self.test_button = Button(self.quiz_frame, text = "Test", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg = "Firebrick4", fg = "white", command = root.destroy)
        self.test_button.grid(row = 3, padx = 50, pady = 200, sticky = W)


class quiz_options:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #test button
        self.test_button = Button(self.quiz_frame, text = "Test", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg = "Firebrick4", fg = "white", command = root.destroy)
        self.test_button.grid(row = 3, padx = 50, pady = 200, sticky = W)

class Leaderboard:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #test button
        self.test_button = Button(self.quiz_frame, text = "Test", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg = "Firebrick4", fg = "white", command = root.destroy)
        self.test_button.grid(row = 3, padx = 50, pady = 200, sticky = W)

        
if __name__ == "__main__":
    root = Tk()
    root.title("NCEA L2 Study Guide") 

    #instantiation, making an instance of the class Quiz
    quiz_instance = Quiz(root)
    #so the frame doesnt dissapear
    root.mainloop()
