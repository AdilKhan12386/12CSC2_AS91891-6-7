#nested if blocks
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
import random

score=0

asked = []
names_bank = []
global math_quiz_questions

math_quiz_questions = {
    1: ["?", "1", "2", "3", "4", "5", "1", 1],
    2: ["!", "1", "2", "3", "4", "5", "1", 1],
    3: ["@", "1", "2", "3", "4", "5", "1", 1],
    4: ["$", "1", "2", "3", "4", "5", "1", 1],
    5: ["%", "1", "2", "3", "4", "5", "1", 1],
    6: ["^", "1", "2", "3", "4", "5", "1", 1],
    7: ["&", "1", "2", "3", "4", "5" ,"1", 1],
    8: ["*", "1", "2", "3", "4", "5", "1", 1],
    9: ["(", "1", "2", "3", "4", "5", "1", 1],
    10: [")", "1", "2", "3", "4", "5", "1", 1],
    }


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
    

    def name_collection(self):
        name = self.entry_box.get()
        if str.isalpha(name) == True and len(name) <=16:
            names_bank.append(name) 
            self.quiz_frame.destroy()
            Nav(root)
        else:
            def error_message(self):
                self.messagebox.error("error", "Please insert a username that is between 1-15 letters long")
           

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

        #Return Button
        self.return_button = Button(self.quiz_frame, text = "Return", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                    compound = "c", bg = "Firebrick4", fg = "white", command = self.return_to_nav)
        self.return_button.grid(row = 0, sticky = NW)

    def return_to_nav(self):
        if self.return_to_nav:
            self.quiz_frame.destroy()
            Nav(root)

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

        #Return Button
        self.return_button = Button(self.quiz_frame, text = "Return", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                    compound = "c", bg = "Firebrick4", fg = "white", command = self.return_to_res_options)
        self.return_button.grid(row = 0, sticky = NW)

    def return_to_res_options(self):
        if self.return_to_res_options:
            self.quiz_frame.destroy()
            res_options(root)
            
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

        #Return Button
        self.return_button = Button(self.quiz_frame, text = "Return", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                    compound = "c", bg = "Firebrick4", fg = "white", command = self.return_to_res_options)
        self.return_button.grid(row = 0, sticky = NW)

    def return_to_res_options(self):
        if self.return_to_res_options:
            self.quiz_frame.destroy()
            res_options(root)
            
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

        #Return Button
        self.return_button = Button(self.quiz_frame, text = "Return", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                    compound = "c", bg = "Firebrick4", fg = "white", command = self.return_to_res_options)
        self.return_button.grid(row = 0, sticky = NW)

    def return_to_res_options(self):
        if self.return_to_res_options:
            self.quiz_frame.destroy()
            res_options(root)
            
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

        #Return Button
        self.return_button = Button(self.quiz_frame, text = "Return", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                    compound = "c", bg = "Firebrick4", fg = "white", command = self.return_to_res_options)
        self.return_button.grid(row = 0, sticky = NW)

    def return_to_res_options(self):
        if self.return_to_res_options:
            self.quiz_frame.destroy()
            res_options(root)
            
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

        #Return Button
        self.return_button = Button(self.quiz_frame, text = "Return", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                    compound = "c", bg = "Firebrick4", fg = "white", command = self.return_to_res_options)
        self.return_button.grid(row = 0, sticky = NW)

    def return_to_res_options(self):
        if self.return_to_res_options:
            self.quiz_frame.destroy()
            res_options(root)




class quiz_options:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "Select a subject to test your knowledge against",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

        #Math Button
        self.math_button = Button(self.quiz_frame, text = "Math", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg="Purple4", fg = "white", command = self.math_quiz_move_on)
        self.math_button.grid(row = 2, padx = 50, pady = 100, sticky = NW)

        #English Button
        self.english_button = Button(self.quiz_frame, text = "English", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg="Purple4", fg = "white", command = self.english_quiz_move_on)
        self.english_button.grid(row = 2, padx = 50, pady = 100)

        #Physics Button
        self.physics_button = Button(self.quiz_frame, text = "Physics", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg="Purple4", fg = "white", command = self.physics_quiz_move_on)
        self.physics_button.grid(row = 2, padx = 50, pady = 100, sticky = NE)

        #Chemistry Button
        self.chemistry_button = Button(self.quiz_frame, text = "Chemistry", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg="Purple4", fg = "white", command = self.chemistry_quiz_move_on)
        self.chemistry_button.grid(row = 4, padx = 50, pady = 100, sticky = SW)

        #Biology Button
        self.biology_button = Button(self.quiz_frame, text = "Biology", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                  compound = "c", bg="Purple4", fg = "white", command = self.biology_quiz_move_on)
        self.biology_button.grid(row = 4, padx = 50, pady = 100, sticky = SE)

        #Return Button
        self.return_button = Button(self.quiz_frame, text = "Return", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                    compound = "c", bg = "Firebrick4", fg = "white", command = self.return_to_nav)
        self.return_button.grid(row = 0, sticky = NW)

    def return_to_nav(self):
        if self.return_to_nav:
            self.quiz_frame.destroy()
            Nav(root)

    def math_quiz_move_on(self):
        if self.math_button:
            self.quiz_frame.destroy()
            math_quiz_pg(root)

    def english_quiz_move_on(self):
        if self.math_button:
            self.quiz_frame.destroy()
            english_quiz_pg(root)

    def physics_quiz_move_on(self):
        if self.math_button:
            self.quiz_frame.destroy()
            physics_quiz_pg(root)

    def chemistry_quiz_move_on(self):
        if self.math_button:
            self.quiz_frame.destroy()
            chemistry_quiz_pg(root)

    def biology_quiz_move_on(self):
        if self.math_button:
            self.quiz_frame.destroy()
            biology_quiz_pg(root)

class math_quiz_pg:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "Maths and Stats",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

        biology_label_1 = Label(self.quiz_frame, text = "I haven't taken this subject thankfully", font = ("Ariel", "18"), bg = "white")
        biology_label_1.grid(row = 1, padx = 25, pady = 50)

        self.question_label = Label(self.quiz_frame, text = math_quiz_questions[qn][0], font = ("Ariel", "20", "bold"), bg = background_color)
        self.question_label.grid(row=0, padx = 225, sticky = N)

        self.radb = IntVar()

        #Option 1 Button
        self.op1 = Radiobutton(self.quiz_frame, text = math_quiz_questions[qn][1], font = ("Ariel", "15"), bg = background_color, value = 1, padx = 25,
                               pady = 10, variable = self.radb, indicator = 0, background = "white")
        self.op1.grid(row = 2, sticky = W)

        #Option 2 Button
        self.op2 = Radiobutton(self.quiz_frame, text = math_quiz_questions[qn][2], font = ("Ariel", "15"), bg = background_color, value = 1, padx = 25,
                               pady = 10, variable = self.radb, indicator = 0, background = "white")
        self.op2.grid(row = 3, sticky = W)

        #Option 3 Button
        self.op3 = Radiobutton(self.quiz_frame, text = math_quiz_questions[qn][3], font = ("Ariel", "15"), bg = background_color, value = 1, padx = 25,
                               pady = 10, variable = self.radb, indicator = 0, background = "white")
        self.op3.grid(row = 4, sticky = W)

        #Option 4 Button
        self.op4 = Radiobutton(self.quiz_frame, text = math_quiz_questions[qn][4], font = ("Ariel", "15"), bg = background_color, value = 1, padx = 25,
                               pady = 10, variable = self.radb, indicator = 0, background = "white")
        self.op4.grid(row = 5, sticky = W)

        #Option 5 Button
        self.op5 = Radiobutton(self.quiz_frame, text = math_quiz_questions[qn][5], font = ("Ariel", "15"), bg = background_color, value = 1, padx = 25,
                               pady = 10, variable = self.radb, indicator = 0, background = "white")
        self.op5.grid(row = 6, sticky = W)

        #confirm button 2 (to confirm your answer choice)
        self.confirm_button = Button(self.quiz_frame, text = "Confirm", bg = "midnight blue", command = self.math_test)
        self.confirm_button.grid(row = 7, sticky = E)

        #Score label (shows score while cconsumer is taking the test)
        self.score_label = Label(self.quiz_frame, text = "SCORE:", font("Ariel", "15", "Bold"), bg = background_color)
        self.score_label.grid(row = 7, sticky = W)

    #Question changing method
    def questions_changer(self):
        randomiser()
        self.radb.set = (0)
        self.next_question.config(text = math_quiz_questions[qn][0])
        self.op1.config(text = math_quiz_questions[qn][1])
        self.op2.config(text = math_quiz_questions[qn][2])
        self.op3.config(text = math_quiz_questions[qn][3])
        self.op4.config(text = math_quiz_questions[qn][4])
        self.op5.config(text = math_quiz_questions[qn][5])



    def math_test(self):
        global score
        score_label = self.score_label
        choice = self.radb.get()
        if len(asked)>9:
            if choice == math_quiz_question[qn][8]:
                score+=1
                score_label.config(text = score)
                self.quiz_instance.config(text = "Confirm")
            else:
                score+=0
                score_label.config(text = "Sorry but the correct answer was: " + math_quiz_questions[qn][7]
                self.quiz_instance.config(text = "Confirm")
        else:
            if choice == 0:
                self.quiz_instance.config(text = "Oops. You forgot to select an option. Try again.")
                choice = self.radb.get()
            else:
                if choice == math_quiz_questions[qn][8]:
                    score+=1
                    score_label.config(text = score)
                    self.quiz_instance.config(text = "Confirm")
                    self.questions_changer()
                else:
                    score+=0
                    score_label.config(text = "Sorry but the correct answer was: " + math_quiz_questions[qn][6])
                    self.quiz_instance.config(text = "Confirm")
                    self.questions_changer()

class english_quiz_pg:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "English",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

        biology_label_1 = Label(self.quiz_frame, text = "I haven't taken this subject thankfully", font = ("Ariel", "18"), bg = "white")
        biology_label_1.grid(row = 1, padx = 25, pady = 50)

class physics_quiz_pg:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "Physics",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

        biology_label_1 = Label(self.quiz_frame, text = "I haven't taken this subject thankfully", font = ("Ariel", "18"), bg = "white")
        biology_label_1.grid(row = 1, padx = 25, pady = 50)

class chemistry_quiz_pg:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "Chemistry",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

        biology_label_1 = Label(self.quiz_frame, text = "I haven't taken this subject thankfully", font = ("Ariel", "18"), bg = "white")
        biology_label_1.grid(row = 1, padx = 25, pady = 50)

class biology_quiz_pg:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "Biology",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

        biology_label_1 = Label(self.quiz_frame, text = "I haven't taken this subject thankfully", font = ("Ariel", "18"), bg = "white")
        biology_label_1.grid(row = 1, padx = 25, pady = 50)


class Leaderboard:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "Here are the top scores for each quiz",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

  def randomiser():
            global qn
            qn = random.randint(1,10)
            if qn not in asked:
                asked.append(qn)
            elif qn in asked:
                randomiser()

        randomiser()              

        
if __name__ == "__main__":
    root = Tk()
    root.title("NCEA L2 Study Guide") 

    #instantiation, making an instance of the class Quiz
    quiz_instance = Quiz(root)
    #so the frame doesnt dissapear
    root.mainloop()
