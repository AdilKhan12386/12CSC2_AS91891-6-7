#Specific resources Heading
       # self.res_pg_label = Label(self.quiz_frame, text = "", bd = 10, relief = "raised", font = ("Ariel", "25"))
        #self.res_pg_label.grid(row = 0, padx = 225, sitcky = N)

#later information
#
#, command = self.move_on
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
            self.error_label.config(text = "")
            self.error_label.config(self.quiz_frame, text="Remember your username needs to be non-numerical and between 0-15 letters",
                                       font=("Ariel", "20", "bold"),fg = "red")
           

class Nav:
    def __init__(self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Second Heading
        self.nav_label = Label(self.quiz_frame, text = "Welcome, please select one of the given resources",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.nav_label.grid(row=0, padx = 225, sticky = N)

        #Gradhat Image temp replacement
        self.irtr = Label(self.quiz_frame, text = "Work in progress", bd = 20, relief = "ridge", font = ("Ariel", "50"))
        self.irtr.grid(row = 2, padx = 225, pady = 125)

        #Leaderboard Button
        self.Leader_button = Button(self.quiz_frame, text = "Leaderboard Page", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                       compound = "c", bg = "purple4", fg = "white", command = self.lead_move_on)
        self.Leader_button.grid(row = 4, padx = 20, sticky = S)

        #Resources Button
        self.resources_button = Button(self.quiz_frame, text = "Resources Page", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                       compound = "c", bg = "purple4", fg = "white", command = self.res_move_on)
        self.resources_button.grid(row = 3, padx = 40, sticky = W)

        #Quiz Button
        self.quiz_button = Button(self.quiz_frame, text = "Quiz Page", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                       compound = "c", bg = "purple4", fg = "white", command = self.quiz_move_on)
        self.quiz_button.grid(row = 3, padx = 60, sticky = E)

        #Exit button
        self.exit_button = Button(self.quiz_frame, text = "Exit", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg="Firebrick4", fg = "white", command = root.destroy)
        self.exit_button.grid(row = 0, column = 0, sticky = NW)

    def res_move_on(self):
        if self.resources_button:
            self.quiz_frame.destroy()
            res_options(root)


    def lead_move_on(self):
        if self.Leader_button:
            self.quiz_frame.destroy()
            Leaderboard(root)

    def quiz_move_on(self):
        if self.quiz_button:
            self.quiz_frame.destroy()
            quiz_options(root)

        


class res_options:
    def __init__(self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "Select a subject you would like short notes for",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

        #Math Button
        self.math_button = Button(self.quiz_frame, text = "Math", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg="Purple4", fg = "white", command = self.math_res_move_on)
        self.math_button.grid(row = 2, padx = 50, pady = 100, sticky = NW)

        #English Button
        self.english_button = Button(self.quiz_frame, text = "English", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg="Purple4", fg = "white", command = self.english_res_move_on)
        self.english_button.grid(row = 2, padx = 50, pady = 100)

        #Physics Button
        self.physics_button = Button(self.quiz_frame, text = "Physics", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg="Purple4", fg = "white", command = self.physics_res_move_on)
        self.physics_button.grid(row = 2, padx = 50, pady = 100, sticky = NE)

        #Chemistry Button
        self.chemistry_button = Button(self.quiz_frame, text = "Chemistry", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg="Purple4", fg = "white", command = self.chemistry_res_move_on)
        self.chemistry_button.grid(row = 4, padx = 50, pady = 100, sticky = SW)

        #Biology Button
        self.biology_button = Button(self.quiz_frame, text = "Biology", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg="Purple4", fg = "white", command = self.biology_res_move_on)
        self.biology_button.grid(row = 4, padx = 50, pady = 100, sticky = SE)

    def math_res_move_on(self):
        if self.math_button:
            self.quiz_frame.destroy()
            math_res_pg(root)

    def english_res_move_on(self):
        if self.math_button:
            self.quiz_frame.destroy()
            english_res_pg(root)

    def physics_res_move_on(self):
        if self.math_button:
            self.quiz_frame.destroy()
            physics_res_pg(root)

    def chemistry_res_move_on(self):
        if self.math_button:
            self.quiz_frame.destroy()
            chemistry_res_pg(root)

    def biology_res_move_on(self):
        if self.math_button:
            self.quiz_frame.destroy()
            biology_res_pg(root)

class math_res_pg:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "Math Internal and External Notes",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

        math_label_1 = Label(self.quiz_frame, text = "Math + Math = 2Math or Math^2. That's math right?", font = ("Ariel", "18"), bg = "white")
        math_label_1.grid(row = 1, padx = 25, pady = 50)

class english_res_pg:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "English Internal and External Notes",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

        english_label_1 = Label(self.quiz_frame, text = "What might happen if we didn't have english", font = ("Ariel", "18"), bg = "white")
        english_label_1.grid(row = 1, padx = 25, pady = 50)

class physics_res_pg:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "Physics Internal and External Notes",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

        physics_label_1 = Label(self.quiz_frame, text = "Why is circular motion a thing?", font = ("Ariel", "18"), bg = "white")
        physics_label_1.grid(row = 1, padx = 25, pady = 50)

class chemistry_res_pg:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "Chemistry Internal and External Notes",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

        chemistry_label_1 = Label(self.quiz_frame, text = "Thankfully this subject isn't hard. Yet.", font = ("Ariel", "18"), bg = "white")
        chemistry_label_1.grid(row = 1, padx = 25, pady = 50)

class biology_res_pg:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "Biology Internal and External Notes",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

        biology_label_1 = Label(self.quiz_frame, text = "I haven't taken this subject thankfully", font = ("Ariel", "18"), bg = "white")
        biology_label_1.grid(row = 1, padx = 25, pady = 50)






class quiz_options:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "Select a subject to test your knowledge against",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

class Leaderboard:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "Here are the top scores for each quiz",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

        
if __name__ == "__main__":
    root = Tk()
    root.title("NCEA L2 Study Guide") 

    #instantiation, making an instance of the class Quiz
    quiz_instance = Quiz(root)
    #so the frame doesnt dissapear
    root.mainloop()
