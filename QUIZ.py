Age = int(input("enter your age: "))
name=input("enter your name :")
class_=input("enter your class :")
section=input("enter your section :")
fater_name=input("enter your father name :")
mother_name=input("enter your mother name :")
email=input("enter your email id :")
phnNo=input("enter your phone number :")
InstituteName=input("enter your instituion name :")

if Age >= 18:
    print("you are eligible")
    password = str(input("enter your password: "))
    
    

    for i in range(4):
        enter_pass = str(input("enter your confirm password: "))
        
        if enter_pass == password:
            print("correct password!!")
            print("HERE ARE SOME TERMS AND CONDITIONS!!!")

            print("1. do not cheat")
            print("2. each question carry 1 mark")
            print("3. you have 3 chances to answer correctly ")        
            print("4. camera should be on while attempting ")    
            print("5. no help from others")    
            print("6. accept cookies fully")    
            print("7. Have internet access")
            
            g= input("do you wish to continue?(yes or no) : ")
    
            if g== "yes":
                print("Start Quiz")
            
#-------------------------------------------QUIZ QUESTIONS-------------------------------

#-------------------------------------------FIRST QUESTION-------------------------------

                print("WHAT IS THE FULL FORM OF RAM ? ")
                print("Option 1: RANDOM ACCESS MEMORY  ")
                print("Option 2: REVERSE ACCESS MEMORY")
                print("Option 3: BOTH OF ABOVE")
                print("Option 4: none of above")
                correct_ans="Option 1"
                marks=0
                for i in range (3):
                    ans=input("enter your answer :")

                    if ans==correct_ans:
                        print("Correct answer!!!")
                        marks+=1
                        break 
                    else:
                     chance_left=2-i
                     if chance_left>0 :
                        print("please try again !! you have ",chance_left,"chances left") 
                     else:
                         print("no chances left")

                print("marks = ", marks)

                # ----------------------------SECOND QUESTION------------------------------------

                print("WHAT IS FULL FORM OF CPU")
                print("Option 1: CONTROL PROCESSING UNIT ")
                print("Option 2: CENTRAL PROCESSING UNIT")
                print("Option 3: BOTH OF THE ABOVE")
                print("Option 4: NONE OF ABOVE")

                correct_ans="Option 2"

                for i in range (3):
                    ans=input("enter your answer :")

                    if ans==correct_ans:
                    
                        print("Correct answer!!!")

                        break 
                    else:
                     chance_left=2-i
                     if chance_left>0 :
                        print("please try again !! you have ",chance_left,"chances left") 
                     else:
                         print("no chances left")
                if ans==correct_ans:
                    marks+=1 
                    print("marks = ", marks)

                # -----------------------------------THIRD QUESTION--------------------------------------

                print("HOW MANY BITS ARE THERE IN 1 BYTE")
                print("Option 1: 4 ")
                print("Option 2: 8")
                print("Option 3: 16")
                print("Option 4: 56")

                correct_ans="Option 2"

                for i in range (3):
                    ans=input("enter your answer :")

                    if ans==correct_ans:
                    
                        print("Correct answer!!!")

                        break 
                    else:
                     chance_left=2-i
                     if chance_left>0 :
                        print("please try again !! you have ",chance_left,"chances left") 
                     else:
                         print("no chances left")
                if ans==correct_ans:
                    marks+=1 
                    print("marks = ", marks)

                # -----------------------------FOURTH QUESTION--------------------------------------------

                print("WHICH OF THESE FUNCTIONS IS A LOOP IN PYTHON ")
                print("Option 1: FOR ")
                print("Option 2: LOOP")
                print("Option 3: REPEAT")
                print("Option 4: ITERATE")

                correct_ans="Option 1"

                for i in range (3):
                    ans=input("enter your answer :")

                    if ans==correct_ans:
                    
                        print("Correct answer!!!")

                        break 
                    else:
                     chance_left=2-i
                     if chance_left>0 :
                        print("please try again !! you have ",chance_left,"chances left") 
                     else:
                         print("no chances left")
                if ans==correct_ans:
                    marks+=1 
                    print("marks = ", marks)

                # -----------------------------FIFTH QUESTION--------------------------------------------

                print("WHAT DOES HTML STANDS FOR ")
                print("Option 1: HYPER TEXT MARKUP LANGUAGE ")
                print("Option 2: HIGH TEXT MACHINE LANGUAGE")
                print("Option 3: NONE OF ABOVE")
                print("Option 4: BOTH 'A' AND 'B' ")

                correct_ans="Option 1"

                for i in range (3):
                    ans=input("enter your answer :")

                    if ans==correct_ans:
                    
                        print("Correct answer!!!")
                        break 
                    
                    else:
                     chance_left=2-i
                     if chance_left>0 :
                    
                        print("please try again !! you have ",chance_left,"chances left") 
                     else:
                         print("no chances left")
                if ans==correct_ans:
                    marks+=1 
                    print("marks = ", marks)    

                # -----------------------------SIXTH QUESTION--------------------------------------------    

                print("WHICH COMPANY DEVLOPED WINDOWS ")
                print("Option 1: IBM ")
                print("Option 2: GOOGLE")
                print("Option 3: MICROSOFT")
                print("Option 4: APPLE")

                correct_ans="Option 3"

                for i in range (3):
                    ans=input("enter your answer :")

                    if ans==correct_ans:
                    
                        print("Correct answer!!!")

                        break 
                    else:
                     chance_left=2-i
                     if chance_left>0 :
                    
                        print("please try again !! you have ",chance_left,"chances left") 
                     else:
                         print("no chances left")
                if ans==correct_ans:
                    marks+=1 
                    print("marks = ", marks)

                # -----------------------------SEVENTH QUESTION--------------------------------------------    

                print("WHICH SYMBOL IS FOR COMMENTS IN PYTHON ")
                print("Option 1: @ ")
                print("Option 2: % ")
                print("Option 3: * ")
                print("Option 4: # ")

                correct_ans="Option 4"

                for i in range (3):
                    ans=input("enter your answer :")

                    if ans==correct_ans:
                    
                        print("Correct answer!!!")

                        break 
                    else:
                     chance_left=2-i
                     if chance_left>0 :
                    
                        print("please try again !! you have ",chance_left,"chances left") 
                     else:
                         print("no chances left")
                if ans==correct_ans:
                    marks+=1 
                    print("Your Total marks for this quiz are ",marks,"out of 7  ")


                    print("THANKYOU FOR PARTICIPATING IN THE QUIZ ")
                break
            else:
             print("please EXIT")
             break
                    
        else:
                        chances_left=3-i
                        if chances_left>0:
                            print("password incorrect!! PLEASE RETRY!! YOU HAVE ",chances_left,"chances left")
                        else:
                            print("TOO MANY ATTEMPTS!! ")
                            print("ACCESS DENIED!! YOU MAY EXIT")
    else:       
        print("you are under age!!")
        print("not eligible please exit")