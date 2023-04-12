# Nakul Thureja
# ROLL NO :- 2020528
# BRANCH  :- CSE
# AI Assignment 3

from durable.lang import *
flag = True

Courses = ["Machine Learning", "Artificial Intelligence", "Deep Learning", "Computer Networks", "Fundamentals of Computer Security", "Network Security",
           "Human Computer Interaction", "Prototyping Interactive Systems", "3D Animation",
           "Digital Circuits", "Basic Electronics", "Signals and Systems",
           "Data Structures and Algorithms", "Algorithm Design and Analysis", "Intro to Programming",
           "Linear Algebra", "Probability and Statistics", "Calculus",
           "Money and Banking", "Foundations of Finance", "Economics"]

Interest = ["Machine Learning", "Cyber Security", "Electronics", "Finance",
            "UI-UX Designer", "Mathematics and Computing"]

with ruleset('courses'):
    @ when_all(((m.course1 == "Machine Learning") | (m.course2 == "Machine Learning") | (m.course3 == "Machine Learning") | (m.course4 == "Machine Learning") | (m.course5 == "Machine Learning"))
               & ((m.course1 == "Artificial Intelligence") | (m.course2 == "Artificial Intelligence") | (m.course3 == "Artificial Intelligence") | (m.course4 == "Artificial Intelligence") | (m.course5 == "Artificial Intelligence"))
               & ((m.course1 == "Deep Learning") | (m.course2 == "Deep Learning") | (m.course3 == "Deep Learning") | (m.course4 == "Deep Learning") | (m.course5 == "Deep Learning")))
    def print_career(c):
        global flag
        if (flag):
            print("Career Recommended: Data Scientist")
            print("Since you have chosen courses related to Machine Learning, Artificial Intelligence and Deep Learning, you are most likely to be interested in Data Science.")
            flag = False

    @ when_all(((m.course1 == "Computer Networks") | (m.course2 == "Computer Networks") | (m.course3 == "Computer Networks") | (m.course4 == "Computer Networks") | (m.course5 == "Computer Networks"))
               & ((m.course1 == "Fundamentals of Computer Security") | (m.course2 == "Fundamentals of Computer Security") | (m.course3 == "Fundamentals of Computer Security") | (m.course4 == "Fundamentals of Computer Security") | (m.course5 == "Fundamentals of Computer Security"))
               & ((m.course1 == "Network Security") | (m.course2 == "Network Security") | (m.course3 == "Network Security") | (m.course4 == "Network Security") | (m.course5 == "Network Security")))
    def print_career(c):
        global flag
        if (flag):
            print("Career Recommended: Computer Network & Security Engineer")
            print("Since you have chosen courses related to Computer Networks, Fundamentals of Computer Security and Network Security, you are most likely to be interested in Computer Network & Security Engineering.")
            flag = False

    @ when_all(((m.course1 == "Human Computer Interaction") | (m.course2 == "Human Computer Interaction") | (m.course3 == "Human Computer Interaction") | (m.course4 == "Human Computer Interaction") | (m.course5 == "Human Computer Interaction"))
               & ((m.course1 == "Prototyping Interactive Systems") | (m.course2 == "Prototyping Interactive Systems") | (m.course3 == "Prototyping Interactive Systems") | (m.course4 == "Prototyping Interactive Systems") | (m.course5 == "Prototyping Interactive Systems"))
               & ((m.course1 == "3D Animation") | (m.course2 == "3D Animation") | (m.course3 == "3D Animation") | (m.course4 == "3D Animation") | (m.course5 == "3D Animation")))
    def print_career(c):
        global flag
        if (flag):
            print("Career Recommended: UI/UX Designer")
            print("Since you have chosen courses related to Human Computer Interaction, Prototyping Interactive Systems and 3D Animation, you are most likely to be interested in UI/UX Designing.")
            flag = False

    @ when_all(((m.course1 == "Digital Circuits") | (m.course2 == "Digital Circuits") | (m.course3 == "Digital Circuits") | (m.course4 == "Digital Circuits") | (m.course5 == "Digital Circuits"))
               & ((m.course1 == "Basic Electronics") | (m.course2 == "Basic Electronics") | (m.course3 == "Basic Electronics") | (m.course4 == "Basic Electronics") | (m.course5 == "Basic Electronics"))
               & ((m.course1 == "Signals and Systems") | (m.course2 == "Signals and Systems") | (m.course3 == "Signals and Systems") | (m.course4 == "Signals and Systems") | (m.course5 == "Signals and Systems")))
    def print_career(c):
        global flag
        if (flag):
            print("Career Recommended: Electronics Engineer")
            print("Since you have chosen courses related to Digital Circuits, Basic Electronics and Signals and Systems, you are most likely to be interested in Electronics Engineering.")
            flag = False

    @ when_all(((m.course1 == "Data Structures and Algorithms") | (m.course2 == "Data Structures and Algorithms") | (m.course3 == "Data Structures and Algorithms") | (m.course4 == "Data Structures and Algorithms") | (m.course5 == "Data Structures and Algorithms"))
               & ((m.course1 == "Algorithm Design and Analysis") | (m.course2 == "Algorithm Design and Analysis") | (m.course3 == "Algorithm Design and Analysis") | (m.course4 == "Algorithm Design and Analysis") | (m.course5 == "Algorithm Design and Analysis"))
               & ((m.course1 == "Intro to Programming") | (m.course2 == "Intro to Programming") | (m.course3 == "Intro to Programming") | (m.course4 == "Intro to Programming") | (m.course5 == "Intro to Programming")))
    def print_career(c):
        global flag
        if (flag):
            print("Career Recommended: Algorithm Design Researcher/ SDE")
            print("Since you have chosen courses related to Data Structures and Algorithms, Algorithm Design and Analysis and Intro to Programming, you are most likely to be interested in Algorithm Design Research or Software Development Engineer.")
            flag = False

    @ when_all(((m.course1 == "Linear Algebra") | (m.course2 == "Linear Algebra") | (m.course3 == "Linear Algebra") | (m.course4 == "Linear Algebra") | (m.course5 == "Linear Algebra"))
               & ((m.course1 == "Probability and Statistics") | (m.course2 == "Probability and Statistics") | (m.course3 == "Probability and Statistics") | (m.course4 == "Probability and Statistics") | (m.course5 == "Probability and Statistics"))
               & ((m.course1 == "Calculus") | (m.course2 == "Calculus") | (m.course3 == "Calculus") | (m.course4 == "Calculus") | (m.course5 == "Calculus")))
    def print_career(c):
        global flag
        if (flag):
            print("Career Recommended: Maths and Computing Researcher")
            print("Since you have chosen courses related to Linear Algebra, Probability and Statistics and Calculus, you are most likely to be interested in Maths and Computing Research.")
            flag = False

    @ when_all(((m.course1 == "Money and Banking") | (m.course2 == "Money and Banking") | (m.course3 == "Money and Banking") | (m.course4 == "Money and Banking") | (m.course5 == "Money and Banking"))
               & ((m.course1 == "Foundations of Finance") | (m.course2 == "Foundations of Finance") | (m.course3 == "Foundations of Finance") | (m.course4 == "Foundations of Finance") | (m.course5 == "Foundations of Finance"))
               & ((m.course1 == "Economics") | (m.course2 == "Economics") | (m.course3 == "Economics") | (m.course4 == "Economics") | (m.course5 == "Economics")))
    def print_career(c):
        global flag
        if (flag):
            print("Career Recommended: Finance")
            print("Since you have chosen courses related to Money and Banking, Foundations of Finance and Economics, you are most likely to be interested in Finance.")
            flag = False

    @ when_all(m.output == True)
    def print_career(c):
        global flag
        if (flag):
            print("Career Recommended: SDE (Software Development Engineer)")
            print("Since your interests and favourite courses do not coincide, we recommend you to take up a career in the field of software development and further chooce a more specific career path down the line.")
            flag = False

with ruleset('career'):
    @ when_all((m.interest == "Machine Learning")
               & ((((m.course1 == "Machine Learning") | (m.course2 == "Machine Learning") | (m.course3 == "Machine Learning") | (m.course4 == "Machine Learning") | (m.course5 == "Machine Learning"))
                  & ((m.course1 == "Artificial Intelligence") | (m.course2 == "Artificial Intelligence") | (m.course3 == "Artificial Intelligence") | (m.course4 == "Artificial Intelligence") | (m.course5 == "Artificial Intelligence")))
               | (((m.course1 == "Machine Learning") | (m.course2 == "Machine Learning") | (m.course3 == "Machine Learning") | (m.course4 == "Machine Learning") | (m.course5 == "Machine Learning"))
                  & ((m.course1 == "Deep Learning") | (m.course2 == "Deep Learning") | (m.course3 == "Deep Learning") | (m.course4 == "Deep Learning") | (m.course5 == "Deep Learning")))
               | (((m.course1 == "Deep Learning") | (m.course2 == "Deep Learning") | (m.course3 == "Deep Learning") | (m.course4 == "Deep Learning") | (m.course5 == "Deep Learning"))
                  & ((m.course1 == "Artificial Intelligence") | (m.course2 == "Artificial Intelligence") | (m.course3 == "Artificial Intelligence") | (m.course4 == "Artificial Intelligence") | (m.course5 == "Artificial Intelligence")))))
    def print_career(c):
        global flag
        if (flag):
            print("Career Recommended: Data Scientist")
            print("Since you have done two-three courses in the field of Machine Learning, we recommend you to take up a career in the field of Data Science.")
            flag = False

    @ when_all((m.interest == "Cyber Security")
               & ((((m.course1 == "Computer Networks") | (m.course2 == "Computer Networks") | (m.course3 == "Computer Networks") | (m.course4 == "Computer Networks") | (m.course5 == "Computer Networks"))
                  & ((m.course1 == "Fundamentals of Computer Security") | (m.course2 == "Fundamentals of Computer Security") | (m.course3 == "Fundamentals of Computer Security") | (m.course4 == "Fundamentals of Computer Security") | (m.course5 == "Fundamentals of Computer Security")))
               | (((m.course1 == "Computer Networks") | (m.course2 == "Computer Networks") | (m.course3 == "Computer Networks") | (m.course4 == "Computer Networks") | (m.course5 == "Computer Networks"))
                  & ((m.course1 == "Network Security") | (m.course2 == "Network Security") | (m.course3 == "Network Security") | (m.course4 == "Network Security") | (m.course5 == "Network Security")))
               | (((m.course1 == "Network Security") | (m.course2 == "Network Security") | (m.course3 == "Network Security") | (m.course4 == "Network Security") | (m.course5 == "Network Security"))
                  & ((m.course1 == "Fundamentals of Computer Security") | (m.course2 == "Fundamentals of Computer Security") | (m.course3 == "Fundamentals of Computer Security") | (m.course4 == "Fundamentals of Computer Security") | (m.course5 == "Fundamentals of Computer Security")))))
    def print_career(c):
        global flag
        if (flag):
            print("Career Recommended: Computer Network & Security Engineer")
            print("since you have done two-three courses in the field of Cyber Security, we recommend you to take up a career in the field of Computer Network & Security Engineering.")
            flag = False

    @ when_all((m.interest == "UI-UX Designer")
               & ((((m.course1 == "Human Computer Interaction") | (m.course2 == "Human Computer Interaction") | (m.course3 == "Human Computer Interaction") | (m.course4 == "Human Computer Interaction") | (m.course5 == "Human Computer Interaction"))
                  & ((m.course1 == "Prototyping Interactive Systems") | (m.course2 == "Prototyping Interactive Systems") | (m.course3 == "Prototyping Interactive Systems") | (m.course4 == "Prototyping Interactive Systems") | (m.course5 == "Prototyping Interactive Systems")))
               | (((m.course1 == "Human Computer Interaction") | (m.course2 == "Human Computer Interaction") | (m.course3 == "Human Computer Interaction") | (m.course4 == "Human Computer Interaction") | (m.course5 == "Human Computer Interaction"))
                  & ((m.course1 == "3D Animation") | (m.course2 == "3D Animation") | (m.course3 == "3D Animation") | (m.course4 == "3D Animation") | (m.course5 == "3D Animation")))
               | (((m.course1 == "3D Animation") | (m.course2 == "3D Animation") | (m.course3 == "3D Animation") | (m.course4 == "3D Animation") | (m.course5 == "3D Animation"))
                  & ((m.course1 == "Prototyping Interactive Systems") | (m.course2 == "Prototyping Interactive Systems") | (m.course3 == "Prototyping Interactive Systems") | (m.course4 == "Prototyping Interactive Systems") | (m.course5 == "Prototyping Interactive Systems")))))
    def print_career(c):
        global flag
        if (flag):
            print("Career Recommended: UI/UX Designer")
            print("Since you have done two-three courses in the field of UI/UX Design, we recommend you to take up a career in the field of UI/UX Design.")
            flag = False

    @ when_all((m.interest == "Electronics")
               & ((((m.course1 == "Digital Circuits") | (m.course2 == "Digital Circuits") | (m.course3 == "Digital Circuits") | (m.course4 == "Digital Circuits") | (m.course5 == "Digital Circuits"))
                  & ((m.course1 == "Basic Electronics") | (m.course2 == "Basic Electronics") | (m.course3 == "Basic Electronics") | (m.course4 == "Basic Electronics") | (m.course5 == "Basic Electronics")))
               | (((m.course1 == "Digital Circuits") | (m.course2 == "Digital Circuits") | (m.course3 == "Digital Circuits") | (m.course4 == "Digital Circuits") | (m.course5 == "Digital Circuits"))
                  & ((m.course1 == "Signals and Systems") | (m.course2 == "Signals and Systems") | (m.course3 == "Signals and Systems") | (m.course4 == "Signals and Systems") | (m.course5 == "Signals and Systems")))
               | (((m.course1 == "Signals and Systems") | (m.course2 == "Signals and Systems") | (m.course3 == "Signals and Systems") | (m.course4 == "Signals and Systems") | (m.course5 == "Signals and Systems"))
                  & ((m.course1 == "Basic Electronics") | (m.course2 == "Basic Electronics") | (m.course3 == "Basic Electronics") | (m.course4 == "Basic Electronics") | (m.course5 == "Basic Electronics")))))
    def print_career(c):
        global flag
        if (flag):
            print("Career Recommended: Electronics Engineer")
            print("Since you have done two-three courses in the field of Electronics, we recommend you to take up a career in the field of Electronics Engineering.")
            flag = False

    @ when_all((m.interest == "Mathematics and Computing")
               & ((((m.course1 == "Data Structures and Algorithms") | (m.course2 == "Data Structures and Algorithms") | (m.course3 == "Data Structures and Algorithms") | (m.course4 == "Data Structures and Algorithms") | (m.course5 == "Data Structures and Algorithms"))
                  & ((m.course1 == "Algorithm Design and Analysis") | (m.course2 == "Algorithm Design and Analysis") | (m.course3 == "Algorithm Design and Analysis") | (m.course4 == "Algorithm Design and Analysis") | (m.course5 == "Algorithm Design and Analysis")))
               | (((m.course1 == "Data Structures and Algorithms") | (m.course2 == "Data Structures and Algorithms") | (m.course3 == "Data Structures and Algorithms") | (m.course4 == "Data Structures and Algorithms") | (m.course5 == "Data Structures and Algorithms"))
                  & ((m.course1 == "Signals and Systems") | (m.course2 == "Signals and Systems") | (m.course3 == "Signals and Systems") | (m.course4 == "Signals and Systems") | (m.course5 == "Signals and Systems")))
               | (((m.course1 == "Intro to Programming") | (m.course2 == "Signals and Systems") | (m.course3 == "Signals and Systems") | (m.course4 == "Signals and Systems") | (m.course5 == "Signals and Systems"))
                  & ((m.course1 == "Algorithm Design and Analysis") | (m.course2 == "Algorithm Design and Analysis") | (m.course3 == "Algorithm Design and Analysis") | (m.course4 == "Algorithm Design and Analysis") | (m.course5 == "Algorithm Design and Analysis")))))
    def print_career(c):
        global flag
        if (flag):
            print("Career Recommended: Algorithm Design Researcher / SDE")
            print("Since you have done two-three courses in the field of Computing, we recommend you to take up a career in the field of Algorithm Design Researcher / SDE.")
            flag = False

    @ when_all((m.interest == "Mathematics and Computing")
               & ((((m.course1 == "Linear Algebra") | (m.course2 == "Linear Algebra") | (m.course3 == "Linear Algebra") | (m.course4 == "Linear Algebra") | (m.course5 == "Linear Algebra"))
                  & ((m.course1 == "Probability and Statistics") | (m.course2 == "Probability and Statistics") | (m.course3 == "Probability and Statistics") | (m.course4 == "Probability and Statistics") | (m.course5 == "Probability and Statistics")))
               | (((m.course1 == "Linear Algebra") | (m.course2 == "Linear Algebra") | (m.course3 == "Linear Algebra") | (m.course4 == "Linear Algebra") | (m.course5 == "Linear Algebra"))
                  & ((m.course1 == "Calculus") | (m.course2 == "Calculus") | (m.course3 == "Calculus") | (m.course4 == "Calculus") | (m.course5 == "Calculus")))
               | (((m.course1 == "Intro to Programming") | (m.course2 == "Calculus") | (m.course3 == "Calculus") | (m.course4 == "Calculus") | (m.course5 == "Calculus"))
                  & ((m.course1 == "Probability and Statistics") | (m.course2 == "Probability and Statistics") | (m.course3 == "Probability and Statistics") | (m.course4 == "Probability and Statistics") | (m.course5 == "Probability and Statistics")))))
    def print_career(c):
        global flag
        if (flag):
            print("Career Recommended: Maths and Computing Researcher")
            print("Since you have done two-three courses in the field of Mathematics, we recommend you to take up a career in the field of Maths and Computing Researcher.")
            flag = False

    @ when_all((m.interest == "Finance")
               & ((((m.course1 == "Money and Banking") | (m.course2 == "Money and Banking") | (m.course3 == "Money and Banking") | (m.course4 == "Money and Banking") | (m.course5 == "Money and Banking"))
                  & ((m.course1 == "Foundations of Finance") | (m.course2 == "Foundations of Finance") | (m.course3 == "Foundations of Finance") | (m.course4 == "Foundations of Finance") | (m.course5 == "Foundations of Finance")))
               | (((m.course1 == "Money and Banking") | (m.course2 == "Money and Banking") | (m.course3 == "Money and Banking") | (m.course4 == "Money and Banking") | (m.course5 == "Money and Banking"))
                  & ((m.course1 == "Economics") | (m.course2 == "Economics") | (m.course3 == "Economics") | (m.course4 == "Economics") | (m.course5 == "Economics")))
               | (((m.course1 == "Intro to Programming") | (m.course2 == "Economics") | (m.course3 == "Economics") | (m.course4 == "Economics") | (m.course5 == "Economics"))
                  & ((m.course1 == "Foundations of Finance") | (m.course2 == "Foundations of Finance") | (m.course3 == "Foundations of Finance") | (m.course4 == "Foundations of Finance") | (m.course5 == "Foundations of Finance")))))
    def print_career(c):
        global flag
        if (flag):
            print("Career Recommended: Finance")
            print("Since you have done two-three courses in the field of Finance, we recommend you to take up a career in the field of Finance.")
            flag = False

    @ when_all(m.output == True)
    def print_career(c):
        global flag
        if (flag):
            c.assert_fact('courses', {'course1': c.m.course1, 'course2': c.m.course2,
                                      'course3': c.m.course3, 'course4': c.m.course4,
                                      'course5': c.m.course5, 'output': c.m.output})
            flag = False


with ruleset('gpa'):
    @ when_all(m.cgpa <= 7.0)
    def gpa(c):
        global flag
        if (flag):
            print("Career Recommended: SDE\nDue to your CGPA system recommends you to go for SDE and get better at skills and then choose a more specific career path")
            flag = False

    @ when_all(m.cgpa > 7.0)
    def gpa(c):
        global flag
        if (flag):
            c.assert_fact('career', {'course1': c.m.course1, 'course2': c.m.course2,
                                     'course3': c.m.course3, 'course4': c.m.course4,
                                     'course5': c.m.course5, 'interest': c.m.interest,
                                     'output': c.m.output})
            flag = False


print("Career Advisory System for College Students of IIIT DELHI")
name = input("Enter your Name: ")
cgpa = float(int(input("\nEnter Your CGPA: ")))
if (cgpa < 0 or cgpa > 10):
    print("Invalid Input")
    exit()

course1 = None
course2 = None
course3 = None
course4 = None
course5 = None
interest = None
output = True

print("\nInterests: ")
j = 1
for i in Interest:
    print(str(j) + ". " + i)
    j += 1

interestinput = int(input("Enter Your Interest: "))
if (interestinput <= 0 or interestinput > len(Interest)):
    print("Invalid Input")
    exit()
interest = Interest[interestinput-1]

j = 1
print("\nCourses: ")
for i in Courses:
    print(str(j) + ". " + i)
    j += 1
courseinput1 = int(input("Enter Course Number 1: "))
if (courseinput1 <= 0 or courseinput1 > 21):
    print("Invalid Input")
    exit()
course1 = Courses[courseinput1-1]

courseinput2 = int(input("Enter Course Number 2: "))
if (courseinput2 <= 0 or courseinput2 > 21):
    print("Invalid Input")
    exit()
course2 = Courses[courseinput2-1]

courseinput3 = int(input("Enter Course Number 3: "))
if (courseinput3 <= 0 or courseinput3 > 21):
    print("Invalid Input")
    exit()
course3 = Courses[courseinput3-1]

courseinput4 = int(input("Enter Course Number 4: "))
if (courseinput4 <= 0 or courseinput4 > 21):
    print("Invalid Input")
    exit()
course4 = Courses[courseinput4-1]
1
courseinput5 = int(input("Enter Course Number 5: "))
if (courseinput5 <= 0 or courseinput5 > 21):
    print("Invalid Input")
    exit()
course5 = Courses[courseinput5-1]

assert_fact('gpa', {'course1': course1, 'course2': course2,
                    'course3': course3, 'course4': course4,
                    'course5': course5, 'interest': interest,
                    'cgpa': cgpa, 'output': output})
