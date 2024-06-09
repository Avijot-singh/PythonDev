# BASIC QUIZ

def Questions():
    scores = 0
    print("Welcome to the quiz")

    question_1 = input("Captial of India: ").lower()
    if(question_1 == 'delhi'):
        scores +=1
    question_2 = input("My name: ").lower()
    if(question_2 == 'avi'):
        scores += 1
    question_3 = input("City I live in: ").lower()
    if(question_3 == 'melbourne'):
        scores += 1
    
    print('Out of 3 you scored ', scores)
    print((scores / 3) * 100) # Calcualting percentages 
Questions()