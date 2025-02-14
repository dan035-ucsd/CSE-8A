### CSE 8A Homework 4
### Author: Dani Nguyen
### Collaborations: Spencer Ellison <3 from the Physics Department ??? (not for long, maybe)

### Interactive Quiz about Mary Ann Horton
### Source: https://maryannhorton.com/mary-ann-horton/ 

key = ["B", "A", "D", "B", "A"]

question1 = """1. What text editor did Mary Ann Horton contributed to developing? 
A. Notepad     B. vi     C. TextEdit     D. Notepad++"""

question2 = """2. Which institution did Mary Ann Horton NOT work at?
A. UC San Diego    B. Bell Labs     C. SDG&E     D. AT&T"""

question3 = """3. In 1997, Mary Ann Horton requested Lucent Technologies to included Transgender people 
in their nondiscrimination clause. Which of the following word was NOT in her request to Lucent Technologies?
A. Gender Identity     B. Characteristics    C. Expressions    D. Sexual Orientation"""

question4 = """4. What early social media / internet forums did Mary Ann Horton help develop?
A. Reddit    B. Usenet    C. Stack Overflow   D. 4chan"""

question5 = """5. What part of email did Mary Ann Horton invent?
A. File Attachments     B. Addresses     C. cc / Carbon Copy     D. Spam Filters"""

questions = [question1, question2, question3, question4, question5]

def questionPrompt():   # resets userAns prompts questions and answers
    userAns = []
    for question in questions:
        print(question)
        userAns.append(input("Enter your answer: ").upper())
    checkKey(userAns)

def checkKey(userAns):         # compares userAns to key
    index = 0
    while index < len(key):
        if userAns[index] == key[index]:
            userAns[index] = True
        else:
            userAns[index] = False
        index += 1
    printResults(userAns)

def printResults(userAns):     # prints results from userAns
    print("Here are your quiz results:")
    questionNum = 1
    score = 0
    for ans in userAns:
        if ans == False:
            print("Question " + str(questionNum) + ": incorrect")
        else:
            print("Question " + str(questionNum) + ": correct")
            score += 1
        questionNum += 1
    print("Your final score is " + str(score) + " out of " + str(len(key)))
    retryPrompt()

def retryPrompt():      # prompts retry
    retry = input("Would you like to try again? (Y/N) ")
    if retry.upper() == "Y":
        questionPrompt()
    elif retry.upper() == "N":
        quit()
    else:
        print("Please enter Y or N")
        retryPrompt()

questionPrompt()