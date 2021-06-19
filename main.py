from tkinter import *
from tkinter import messagebox
import random

math_score=0
english_score=0
physics_score=0
chemistry_score=0
biology_score=0
general_score=0

asked = []

names_bank = []


def randomiser():

  global qnum

  qnum = random.randint(1, 10)

  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()

  randomiser()   

math_quiz_questions = {
    1: ["?", "1", "2", "3", "4", "5", 1, "1"],
    2: ["!", "1", "2", "3", "4", "5", 1, "1"],
    3: ["@", "1", "2", "3", "4", "5", 1, "1"],
    4: ["$", "1", "2", "3", "4", "5", 1, "1"],
    5: ["%", "1", "2", "3", "4", "5", 1, "1"],
    6: ["^", "1", "2", "3", "4", "5", 1, "1"],
    7: ["&", "1", "2", "3", "4", "5" ,1, "1"],
    8: ["*", "1", "2", "3", "4", "5", 1, "1"],
    9: ["(", "1", "2", "3", "4", "5", 1, "1"],
    10: [")", "1", "2", "3", "4", "5", 1, "1"],
    }

english_quiz_questions = {
    1: ["?", "1", "2", "3", "4", "5", 1, "1"],
    2: ["!", "1", "2", "3", "4", "5", 1, "1"],
    3: ["@", "1", "2", "3", "4", "5", 1, "1"],
    4: ["$", "1", "2", "3", "4", "5", 1, "1"],
    5: ["%", "1", "2", "3", "4", "5", 1, "1"],
    6: ["^", "1", "2", "3", "4", "5", 1, "1"],
    7: ["&", "1", "2", "3", "4", "5" ,1, "1"],
    8: ["*", "1", "2", "3", "4", "5", 1, "1"],
    9: ["(", "1", "2", "3", "4", "5", 1, "1"],
    10: [")", "1", "2", "3", "4", "5", 1, "1"],
    }

physics_quiz_questions = {
    1: ["?", "1", "2", "3", "4", "5", 1, "1"],
    2: ["!", "1", "2", "3", "4", "5", 1, "1"],
    3: ["@", "1", "2", "3", "4", "5", 1, "1"],
    4: ["$", "1", "2", "3", "4", "5", 1, "1"],
    5: ["%", "1", "2", "3", "4", "5", 1, "1"],
    6: ["^", "1", "2", "3", "4", "5", 1, "1"],
    7: ["&", "1", "2", "3", "4", "5" ,1, "1"],
    8: ["*", "1", "2", "3", "4", "5", 1, "1"],
    9: ["(", "1", "2", "3", "4", "5", 1, "1"],
    10: [")", "1", "2", "3", "4", "5", 1, "1"],
    }

chemistry_quiz_questions = {
    1: ["?", "1", "2", "3", "4", "5", 1, "1"],
    2: ["!", "1", "2", "3", "4", "5", 1, "1"],
    3: ["@", "1", "2", "3", "4", "5", 1, "1"],
    4: ["$", "1", "2", "3", "4", "5", 1, "1"],
    5: ["%", "1", "2", "3", "4", "5", 1, "1"],
    6: ["^", "1", "2", "3", "4", "5", 1, "1"],
    7: ["&", "1", "2", "3", "4", "5" ,1, "1"],
    8: ["*", "1", "2", "3", "4", "5", 1, "1"],
    9: ["(", "1", "2", "3", "4", "5", 1, "1"],
    10: [")", "1", "2", "3", "4", "5", 1, "1"],
    }

biology_quiz_questions = {
    1: ["?", "1", "2", "3", "4", "5", 1, "1"],
    2: ["!", "1", "2", "3", "4", "5", 1, "1"],
    3: ["@", "1", "2", "3", "4", "5", 1, "1"],
    4: ["$", "1", "2", "3", "4", "5", 1, "1"],
    5: ["%", "1", "2", "3", "4", "5", 1, "1"],
    6: ["^", "1", "2", "3", "4", "5", 1, "1"],
    7: ["&", "1", "2", "3", "4", "5" ,1, "1"],
    8: ["*", "1", "2", "3", "4", "5", 1, "1"],
    9: ["(", "1", "2", "3", "4", "5", 1, "1"],
    10: [")", "1", "2", "3", "4", "5", 1, "1"],
    }



class Signup:
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
                                        bg = "midnight blue", fg = "white", command = self.name_collection)
        self.continue_button.grid(row = 4, padx = 50, pady = 200, sticky = E)
        

        #Exit button #gap for easy visability
        self.exit_button = Button(self.quiz_frame, text = "Exit", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                   bg="Firebrick4", fg = "white", command = root.destroy)
        self.exit_button.grid(row = 4, padx = 50, pady = 200, sticky = W)

        
    def name_collection(self):
        name = self.entry_box.get()
        if str.isalpha(name) == True and int(len(name)) <= 15:
            names_bank.append(name) 
            self.quiz_frame.destroy()
            Nav(root)
        else:
          #Applying messagebox for boundry testing
          messagebox.showerror("Error", "Please insert a username that is between 1-15 letters long")

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

        root.maxsize(2000, 2500)

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "Math Internal and External Notes",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

        math_label_1 = Label(self.quiz_frame, text = """Knowledge 1
        amazing
        """, font = ("Ariel", "14"), bg = "white")
        math_label_1.grid(row = 1, padx = 25, pady = 50, sticky = W)

        math_label_2 = Label(self.quiz_frame, text = """Knowledge 2
        amazing
        """, font = ("Ariel", "14"), bg = "white")
        math_label_2.grid(row = 2, padx = 25, pady = 50, sticky = W)

        math_label_3 = Label(self.quiz_frame, text = """Knowledge 3
        amazing
        """, font = ("Ariel", "14"), bg = "white")
        math_label_3.grid(row = 3, padx = 25, pady = 50, sticky = W)

        math_label_4 = Label(self.quiz_frame, text = """Knowledge 4
        amazing
        """, font = ("Ariel", "14"), bg = "white")
        math_label_4.grid(row = 4, padx = 25, pady = 50, sticky = W)

        math_label_5 = Label(self.quiz_frame, text = """Knowledge 5
        amazing
        """, font = ("Ariel", "14"), bg = "white")
        math_label_5.grid(row = 1, padx = 25, pady = 50, sticky = E)

        math_label_6 = Label(self.quiz_frame, text = """Knowledge 6
        amazing
        """, font = ("Ariel", "14"), bg = "white")
        math_label_6.grid(row = 2, padx = 25, pady = 50, sticky = E)

        math_label_7 = Label(self.quiz_frame, text = """Knowledge 7
        amazing
        """, font = ("Ariel", "14"), bg = "white")
        math_label_7.grid(row = 3, padx = 25, pady = 50, sticky = E)

        math_label_8 = Label(self.quiz_frame, text = """Knowledge 8
        amazing
        """, font = ("Ariel", "14"), bg = "white")
        math_label_8.grid(row = 4, padx = 25, pady = 50, sticky = E)

        #Next page button
        self.next_pg = Button(self.quiz_frame, text = "Next", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                     bg = "midnight blue", fg = "white", command = self.next_res_pg)
        self.next_pg.grid(row = 3, sticky = SE)

      
        #Return Button
        self.return_button = Button(self.quiz_frame, text = "Return", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                     bg = "Firebrick4", fg = "white", command = self.return_to_res_options)
        self.return_button.grid(row = 0, sticky = NW)


    def return_to_res_options(self):
        if self.return_to_res_options:
            self.quiz_frame.destroy()
            res_options(root)

    def next_res_pg(self):
        if self.next_pg:
            self.quiz_frame.destroy()
            math_res_pg_2(root)

class math_res_pg_2:
  def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

        root.maxsize(2000, 2000)

        #Resource heading
        self.res_label = Label(self.quiz_frame, text = "Math Internal and External Notes",bd = 10, relief = "ridge", font = ("Ariel","25"))
        self.res_label.grid(row=0, padx = 225, sticky = N)

        math_label_3 = Label(self.quiz_frame, text = """Knowledge 3
        amazing
        amazing
        amazing
        amazing
        amazing
        amazing
        amazing""", font = ("Ariel", "14"), bg = "white")
        math_label_3.grid(row = 1, padx = 25, pady = 50, sticky = W)

        math_label_4 = Label(self.quiz_frame, text = """Knowledge 4
        amazing
        amazing
        amazing
        amazing
        amazing
        amazing
        amazing""", font = ("Ariel", "14"), bg = "white")
        math_label_4.grid(row = 2, padx = 25, pady = 50, sticky = W)

        math_label_7 = Label(self.quiz_frame, text = """Knowledge 7
        amazing
        amazing
        amazing
        amazing
        amazing
        amazing
        amazing""", font = ("Ariel", "14"), bg = "white")
        math_label_7.grid(row = 1, padx = 25, pady = 50, sticky = E)

        math_label_8 = Label(self.quiz_frame, text = """Knowledge 8
        amazing
        amazing
        amazing
        amazing
        amazing
        amazing
        amazing""", font = ("Ariel", "14"), bg = "white")
        math_label_8.grid(row = 2, padx = 25, pady = 50, sticky = E)

        #Previous page button
        self.prev_pg = Button(self.quiz_frame, text = "Back", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                     bg = "midnight blue", fg = "white", command = self.prev_res_pg)
        self.prev_pg.grid(row = 0, sticky = NW)

  def prev_res_pg(self):
    if self.prev_pg:
      self.quiz_frame.destroy()
      math_res_pg(root)


            
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


        self.var1 = IntVar()

        #Math Button
        self.math_button = Radiobutton(self.quiz_frame, text = "Math", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                   bg="Purple4", fg = "white", value = 1, variable = self.var1, indicator = 0, command = self.quiz_selection)
        self.math_button.grid(row = 2, padx = 50, pady = 100, sticky = NW)

        #English Button
        self.english_button = Radiobutton(self.quiz_frame, text = "English", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                   bg="Purple4", fg = "white", value = 2, variable = self.var1, indicator = 0, command = self.quiz_selection)
        self.english_button.grid(row = 2, padx = 50, pady = 100)

        #Physics Button
        self.physics_button = Radiobutton(self.quiz_frame, text = "Physics", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                   bg="Purple4", fg = "white", value = 3, variable = self.var1, indicator = 0, command = self.quiz_selection)
        self.physics_button.grid(row = 2, padx = 50, pady = 100, sticky = NE)

        #Chemistry Button
        self.chemistry_button = Radiobutton(self.quiz_frame, text = "Chemistry", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                   bg="Purple4", fg = "white", value = 4, variable = self.var1, indicator = 0, command = self.quiz_selection)
        self.chemistry_button.grid(row = 4, padx = 50, pady = 100, sticky = SW)

        #Biology Button
        self.biology_button = Radiobutton(self.quiz_frame, text = "Biology", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                   bg="Purple4", fg = "white", value = 5, variable = self.var1, indicator = 0, command = self.quiz_selection)
        self.biology_button.grid(row = 4, padx = 50, pady = 100, sticky = SE)

        #Return Button
        self.return_button = Button(self.quiz_frame, text = "Return", bd = 10, relief = "raised", font = ("Ariel", "20", "bold"),
                                     bg = "Firebrick4", fg = "white", command = self.return_to_nav)
        self.return_button.grid(row = 0, sticky = NW)

    def return_to_nav(self):
        if self.return_to_nav:
            self.quiz_frame.destroy()
            Nav(root)

    def quiz_selection(self):
        global chosen_quiz
        select_quiz = self.var1.get()

        if select_quiz == 1:
            chosen_quiz = math_quiz_questions
            self.quiz_frame.destroy()
            quiz_pg(root)
        elif select_quiz == 2:
            chosen_quiz = english_quiz_questions
            self.quiz_frame.destroy()
            quiz_pg(root)
        elif select_quiz == 3:
            chosen_quiz = physics_quiz_questions
            self.quiz_frame.destroy()
            quiz_pg(root)
        elif select_quiz == 4:
            chosen_quiz = chemistry_quiz_questions
            self.quiz_frame.destroy()
            quiz_pg(root)
        elif select_quiz == 5:
            chosen_quiz = math_quiz_questions
            self.quiz_frame.destroy()
            quiz_pg(root)

class quiz_pg:
    def __init__ (self,parent):

        background_color="Darkolivegreen2"

        self.quiz_frame=Frame(parent, bg = background_color, padx = 100, pady = 25)
        self.quiz_frame.grid()

       
        #Question label (Question for user to answer)
        self.question_label = Label(self.quiz_frame, text = chosen_quiz[qnum][0], font = ("Ariel", "20", "bold"), bg = background_color)
        self.question_label.grid(row=0, padx = 225, sticky = N)

        self.var1 = IntVar()

        #Option 1 Button
        self.op1 = Radiobutton(self.quiz_frame, text = chosen_quiz[qnum][1], font = ("Ariel", "15"), bg = background_color, value = 1, padx = 25,
                               pady = 10, variable = self.var1, indicator = 0, background = "white")
        self.op1.grid(row = 2, sticky = W)

        #Option 2 Button
        self.op2 = Radiobutton(self.quiz_frame, text = chosen_quiz[qnum][2], font = ("Ariel", "15"), bg = background_color, value = 2, padx = 25,
                               pady = 10, variable = self.var1, indicator = 0, background = "white")
        self.op2.grid(row = 3, sticky = W)

        #Option 3 Button
        self.op3 = Radiobutton(self.quiz_frame, text = chosen_quiz[qnum][3], font = ("Ariel", "15"), bg = background_color, value = 3, padx = 25,
                               pady = 10, variable = self.var1, indicator = 0, background = "white")
        self.op3.grid(row = 4, sticky = W)

        #Option 4 Button
        self.op4 = Radiobutton(self.quiz_frame, text = chosen_quiz[qnum][4], font = ("Ariel", "15"), bg = background_color, value = 4, padx = 25,
                               pady = 10, variable = self.var1, indicator = 0, background = "white")
        self.op4.grid(row = 5, sticky = W)

        #Option 5 Button
        self.op5 = Radiobutton(self.quiz_frame, text = chosen_quiz[qnum][5], font = ("Ariel", "15"), bg = background_color, value = 5, padx = 25,
                               pady = 10, variable = self.var1, indicator = 0, background = "white")
        self.op5.grid(row = 6, sticky = W)

        #Confirm Button 
        self.confirm_button = Button(self.quiz_frame, text = 'Confirm', bd = 10, relief = "raised", font = ("Ariel", "15", "bold"),
                                     bg = "midnight blue", fg = "white", command = self.quiz_runner)
        self.confirm_button.grid(row = 6 , sticky = E)

        #score label (shows score while consumer is taking the test)
        self.score_label = Label(self.quiz_frame, text = "", font = ("Ariel", "15", "bold"), bg = background_color)
        self.score_label.grid(row = 7, sticky = W)

        #Error Label 2 (For which ever quiz is being run, if they don't select an option)
        self.error_label = Label(self.quiz_frame, text = "", font = ("Ariel", "16", "bold"), fg = "red")
        self.error_label.grid(row = 1)

    

    #Question changing method
    def questions_changer(self):
        randomiser()
        self.var1.set(0)
        self.next_question.config(text = chosen_quiz[qnum][0])
        self.op1.config(text = chosen_quiz[qnum][1])
        self.op2.config(text = chosen_quiz[qnum][2])
        self.op3.config(text = chosen_quiz[qnum][3])
        self.op4.config(text = chosen_quiz[qnum][4])
        self.op5.config(text = chosen_quiz[qnum][5])
        self.score_label.config(text = quiz_runner)


    def quiz_runner(self):
        global math_score
        global english_score
        global physics_score
        global chemistry_score
        global biology_score
        global general_score
        score_label = self.score_label
        choice = self.var1.get()
        score = chosen_quiz[qnum][7]
        #This first nested if is for the last question, whether it's right or wrong
        if len(asked)>9:
            if choice == chosen_quiz[qnum][6]:
                score_label += 1
                self.confirm_button.config(text = "Confirm")
            else:
                score_label += 0
                score_label.config(text = "Sorry but the correct answer was: " + chosen_quiz[qnum][7])
                self.confirm_button.config(text = "Confirm")
        #This represents the choices made for anything other than the last question.
        else:
            if choice == 0:
                self.error_label.config(text = "Oops. You forgot to select an option. Try again.")
                choice = self.var1.get()
            else:
                if choice == chosen_quiz[qnum][6]:
                    if chosen_quiz == math_quiz_questions:
                        math_score += 1
                    elif chosen_quiz == english_quiz_questions:
                        english_score += 1
                    elif chosen_quiz == physics_quiz_quesstions:
                        physics_score += 1
                    elif chosen_quiz == chemistry_quiz_questions:
                        chemistry_score += 1
                    elif chosen_quiz == biology_quiz_questions:
                        biology_score += 1
                    else:
                        questions_changer()
                else:
                    score_label.config(text = "Sorry but the correct answer was: " + chosen_quiz[qnum][7])
                    self.questions_changer()
           

        
if __name__ == "__main__":
    root = Tk()
    root.title("NCEA L2 Study Guide") 

    #instantiation, making an instance of the class Quiz
    quiz_instance = Signup(root)
    #so the frame doesnt dissapear
    root.mainloop()
