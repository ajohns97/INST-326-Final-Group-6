import csv

class Categories(): # Creating a categories class
  def __init__ (self, sports, politics, popculture, tech, food):
      self.sports = sports
      self.politics = politics
      self.popculture = popculture
      self.tech = tech
      self.food = food

class Answers(): # Creating an answers class
  def __init__ (self, sports, politics, popculture, tech, food):
      self.sports = sports
      self.politics = politics
      self.popculture = popculture
      self.tech = tech
      self.food = food
        
def get_categories(file):
#category lists
    sports = []
    politics = []
    popculture = []
    tech = []
    food = []
    
    #open file 
    with open(file, encoding = "UTF-8") as handle:
        reader = csv.DictReader(handle, delimiter = ',')
        #iterate over file
        for row in reader:
            #assign category objects
            questions = Categories(row['Sports'], row['Politics'], row['Pop Culture'], row['Technology'], row['Food'])
            #add questions to category list
            sports.append(questions.sports)
            politics.append(questions.politics)
            popculture.append(questions.popculture)
            tech.append(questions.tech)
            food.append(questions.food)
    return sports, politics, popculture, tech, food

def get_answers(file):
     #answers for        
    sports_answers = []
    politics_answers = []
    popculture_answers = []
    tech_answers = []
    food_answers = []
    with open(file, encoding = "UTF-8") as handle:
        reader = csv.DictReader(handle, delimiter = ',')
        for row in reader:
            answers = Answers(row['Sports'],row['Politics'],row['Pop Culture'],row['Technology'],row['Food'])
            sports_answers.append(answers.sports)
            politics_answers.append(answers.politics)
            popculture_answers.append(answers.popculture)
            tech_answers.append(answers.tech)
            food_answers.append(answers.food)
    return sports_answers, politics_answers, popculture_answers, tech_answers, food_answers    


def print_questions(category):
    incr = 1
    for question in category:
        print(f'{incr}. {question}')
        incr += 1

def check_answer(answer):
    user_answer = input('What is your answer?''\n')
    if user_answer.lower() == 'quit':
        return 'quit'
    if user_answer.lower() == answer.lower():
        return True
    else:
        return False
        
def jeopardy():
    
    sports, politics, popculture, tech, food = get_categories('final_project_questions.csv')
    sports_answers, politics_answers, popculture_answers, tech_answers, food_answers = get_answers('final_project_answers.csv')

    #Prompt User for game
    total_points = 0
    total_questions = 25
    questions_answered = 0
    
    while questions_answered < total_questions:
        user_category = input('Pick a Category: Sports, Politics, Pop Culture, Technology, Food''\n')
        user_category = user_category.lower()
        #check 
        if user_category == 'sports':
            print_questions(sports)
            user_question = input('Pick a question using it"s number''\n')
            if user_question == '1':
                print(sports[0])
                answer = check_answer(sports_answers[0])
                if answer == 'quit':
                    break
                if answer == True:
                    print('You earned 100 points')
                    total_points += 100
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 100 points. :(")
                    print(f'The correct answer was {sports_answers[0]}')
                    total_points -= 100
                    print(total_points)
                    questions_answered += 1
            elif user_question =='2':
                print(sports[1])
                answer = check_answer(sports_answers[1])
                if answer == True:
                    print('You earned 200 points')
                    total_points += 200
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 200 points. :(")
                    print(f'The correct answer was {sports_answers[1]}')
                    total_points -= 200
                    print(total_points)
                    questions_answered += 1
            elif user_question =='3':
                print(sports[2])
                answer = check_answer(sports_answers[2])
                if answer == True:
                    print('You earned 300 points')
                    total_points += 300
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 300 points. :(")
                    print(f'The correct answer was {sports_answers[2]}')
                    total_points -= 300
                    print(total_points)
                    questions_answered += 1
            elif user_question =='4':
                print(sports[3])
                answer = check_answer(sports_answers[3])
                if answer == True:
                    print('You earned 400 points')
                    total_points += 400
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 400 points. :(")
                    print(f'The correct answer was {sports_answers[3]}')
                    total_points -= 400
                    print(total_points)
                    questions_answered += 1
            elif user_question =='5':
                print(sports[4])
                answer = check_answer(sports_answers[4])
                if answer == True:
                    print('You earned 500 points')
                    total_points += 500
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 500 points. :(")
                    print(f'The correct answer was {sports_answers[4]}')
                    total_points -= 500
                    print(total_points)
                    questions_answered += 1
            else:
                print("That question doesn't exist. Please try again")
                print_questions(sports)

        elif user_category == 'politics':
            print_questions(politics)
            user_question=input('Pick a question using a number''\n')
            if user_question == '1':
                print(politics[0])
                answer = check_answer(politics_answers[0])
                if answer == True:
                    print('You earned 100 points')
                    total_points += 100
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 100 points. :(")
                    print(f'The correct answer was {politics_answers[0]}')
                    total_points -= 100
                    print(total_points)
                    questions_answered += 1
            elif user_question =='2':
                print(politics[1])
                answer = check_answer(politics_answers[1])
                if answer == True:
                    print('You earned 200 points')
                    total_points += 200
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 200 points. :(")
                    print(f'The correct answer was {politics_answers[1]}')
                    total_points -= 200
                    print(total_points)
                    questions_answered += 1
            elif user_question =='3':
                print(politics[2])
                answer = check_answer(politics_answers[2])
                if answer == True:
                    print('You earned 300 points')
                    total_points += 300
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 300 points. :(")
                    print(f'The correct answer was {politics_answers[2]}')
                    total_points -= 300
                    print(total_points)
                    questions_answered += 1
            elif user_question =='4':
                print(politics[3])
                answer = check_answer(politics_answers[3])
                if answer == True:
                    print('You earned 400 points')
                    total_points += 400
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 400 points. :(")
                    print(f'The correct answer was {politics_answers[3]}')
                    total_points -= 400
                    print(total_points)
                    questions_answered += 1
            elif user_question =='5':
                print(politics[4])
                answer = check_answer(politics_answers[4])
                if answer == True:
                    print('You earned 500 points')
                    total_points += 500
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 500 points. :(")
                    print(f'The correct answer was {politics_answers[4]}')
                    total_points -= 500
                    print(total_points)
                    questions_answered += 1
            else:
                print("That question doesn't exist. Please try again")
                print_questions(politics)
                          
        elif user_category=='pop culture':
            print_questions(popculture)
            user_question=input('Pick a question using a number''\n')
            if user_question == '1':
                print(popculture[0])
                answer = check_answer(popculture_answers[0])
                if answer == True:
                    print('You earned 100 points')
                    total_points += 100
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 100 points. :(")
                    print(f'The correct answer was {popculture_answers[0]}')
                    total_points -= 100
                    print(total_points)
                    questions_answered += 1
            elif user_question =='2':
                print(popculture[1])
                answer = check_answer(popculture_answers[1])
                if answer == True:
                    print('You earned 200 points')
                    total_points += 200
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 200 points. :(")
                    print(f'The correct answer was {popculture_answers[1]}')
                    total_points -= 200
                    print(total_points)
                    questions_answered += 1
            elif user_question =='3':
                print(popculture[2])
                answer = check_answer(popculture_answers[2])
                if answer == True:
                    print('You earned 300 points')
                    total_points += 300
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 300 points. :(")
                    print(f'The correct answer was {popculture_answers[2]}')
                    total_points -= 300
                    print(total_points)
                    questions_answered += 1
            elif user_question =='4':
                print(popculture[3])
                answer = check_answer(popculture_answers[3])
                if answer == True:
                    print('You earned 400 points')
                    total_points += 400
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 400 points. :(")
                    print(f'The correct answer was {popculture_answers[3]}')
                    total_points -= 400
                    print(total_points)
                    questions_answered += 1
            elif user_question =='5':
                print(popculture[4])
                answer = check_answer(popculture_answers[4])
                if answer == True:
                    print('You earned 500 points')
                    total_points += 500
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 500 points. :(")
                    print(f'The correct answer was {popculture_answers[4]}')
                    total_points -= 500
                    print(total_points)
                    questions_answered += 1
            else:
                print("That question doesn't exist. Please try again")
                print_questions(popculture)
                
        elif user_category == 'technology':
            print_questions(tech)
            user_question=input('Pick a question using a number''\n')
            if user_question == '1':
                print(tech[0])
                answer = check_answer(tech_answers[0])
                if answer == True:
                    print('You earned 100 points')
                    total_points += 100
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 100 points. :(")
                    print(f'The correct answer was {tech_answers[0]}')
                    total_points -= 100
                    print(total_points)
                    questions_answered += 1
            elif user_question =='2':
                print(tech[1])
                answer = check_answer(tech_answers[1])
                if answer == True:
                    print('You earned 200 points')
                    total_points += 200
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 200 points. :(")
                    print(f'The correct answer was {tech_answers[1]}')
                    total_points -= 200
                    print(total_points)
                    questions_answered += 1
            elif user_question =='3':
                print(tech[2])
                answer = check_answer(tech_answers[2])
                if answer == True:
                    print('You earned 300 points')
                    total_points += 300
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 300 points. :(")
                    print(f'The correct answer was {tech_answers[2]}')
                    total_points -= 300
                    print(total_points)
                    questions_answered += 1
            elif user_question =='4':
                print(tech[3])
                answer = check_answer(tech_answers[3])
                if answer == True:
                    print('You earned 400 points')
                    total_points += 400
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 400 points. :(")
                    print(f'The correct answer was {tech_answers[3]}')
                    total_points -= 400
                    print(total_points)
                    questions_answered += 1
            elif user_question =='5':
                print(tech[4])
                answer = check_answer(tech_answers[4])
                if answer == True:
                    print('You earned 500 points')
                    total_points += 500
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 500 points. :(")
                    print(f'The correct answer was {tech_answers[4]}')
                    total_points -= 500
                    print(total_points)
                    questions_answered += 1
            else:
                print("That question doesn't exist. Please try again")
                print_questions(tech)
                
        elif user_category=='food':
            print_questions(food)
            user_question=input('Pick a question using a number''\n')
            if user_question == '1':
                print(food[0])
                answer = check_answer(food_answers[0])
                if answer == True:
                    print('You earned 100 points')
                    total_points += 100
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 100 points. :(")
                    print(f'The correct answer was {food_answers[0]}')
                    total_points -= 100
                    print(total_points)
                    questions_answered += 1
            elif user_question =='2':
                print(food[1])
                answer = check_answer(food_answers[1])
                if answer == True:
                    print('You earned 200 points')
                    total_points += 200
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 200 points. :(")
                    print(f'The correct answer was {food_answers[1]}')
                    total_points -= 200
                    print(total_points)
                    questions_answered += 1
            elif user_question =='3':
                print(food[2])
                answer = check_answer(food_answers[2])
                if answer == True:
                    print('You earned 300 points')
                    total_points += 300
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 300 points. :(")
                    print(f'The correct answer was {food_answers[2]}')
                    total_points -= 300
                    print(total_points)
                    questions_answered += 1
            elif user_question =='4':
                print(food[3])
                answer = check_answer(food_answers[3])
                if answer == True:
                    print('You earned 400 points')
                    total_points += 400
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 400 points. :(")
                    print(f'The correct answer was {food_answers[3]}')
                    total_points -= 400
                    print(total_points)
                    questions_answered += 1
            elif user_question =='5':
                print(food[4])
                answer = check_answer(food_answers[4])
                if answer == True:
                    print('You earned 500 points')
                    total_points += 500
                    print(total_points)
                    questions_answered += 1
                else:
                    print("sorry! that answer was incorrect. You lose 500 points. :(")
                    print(f'The correct answer was {food_answers[4]}')
                    total_points -= 500
                    print(total_points)
                    questions_answered += 1
            else:
                print("That question doesn't exist. Please try again")
                print_questions(food)
        else:
            print("Sorry, that's not one of our categories. Please choose again.")
        if user_category.lower() == 'quit':
            break
    return total_points, questions_answered


def get_score(points, questions):
    avg = ( points / questions ) * 100
    return int(avg)
    


def main():

    print('Welcome to Jeopardy: Please pick different questions each time (25 different questions)')
    print('Question 1=100, Question 2=200, Question 3=300, Question 4=400, Question 5=500')
    print('Enter "Quit" to end the game.')
    points, questions_answered = jeopardy()
    print('Thanks for playing!')
    avg = get_score(points, questions_answered)
    print(f'Your total points: {points}')
    print(f'You answered {avg}% of questions correct!')

if __name__ == '__main__':
    main()

    
