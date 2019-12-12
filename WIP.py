df = pd.read_csv('sports_modified.csv')

print("Welcome to Jeopardy!")

total_points = 0
total_questions = 25
questions_answered = 0



randomizer = random.randint(1,25)
dailydouble = randomizer - 1

        

while df.empty == False:
    
    
    print("To leave game, type quit.")
    
    category_list = []
    for i in df['Category']:
        if i not in category_list:
            category_list.append(i)
        else:
            pass
    
    for i in category_list:
        print(i)
    
   
    user_input = input("Choose a category!""\n")
    if user_input.lower() == 'quit':
        break
        
    else:
        user_input = user_input.title()
    
    
    category = df[df['Category'] == user_input]

    values = category['Points']

    print(values.to_string(index=False),"\n")

    userchoice = input("Choose a point value!""\n")
    if userchoice.lower() == 'quit':
        break
    else:
        userchoice = int(userchoice)
    
    if questions_answered == dailydouble:
        print("DAILY DOUBLE!")
        point_multiplier = 2
    else:
        point_multiplier = 1
    
    rho = category[category['Points']==userchoice]

    #print(rho)

    question = rho['Question']
    question = question.to_string(index=False)
    answer = rho['Answer']
    answer = answer.to_string(index=False)
    points = int(rho['Points']) * point_multiplier
    
    #print (answer)

    print(question, "\n")

    user_answer = input("What is your answer?""\n")
    if user_answer.lower() == 'quit':
        break
    elif user_answer == answer:
        print("That's correct! You've earned " + str(points) + " points!", "\n")
        total_points = total_points + (points)
    else:
        print("Sorry! That's incorrect. The correct answer is " + answer + "\n")
        
    df = df.drop(rho.index)
    
    questions_answered += 1

print("Thanks for playing!")
print("Total points:", total_points)
print("Total questions:", total_questions)
print("Questions answered:", questions_answered)

    
    
def main():
    
    import csv
    import random
    import pandas as pd


if __name__ == '__main__':
    main()
    
    



