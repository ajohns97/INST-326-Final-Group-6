import csv

class Categories():
  def __init__ (self,sports,politics,popculture,tech,food):
      self.sports=sports
      self.politics=politics
      self.popculture=popculture
      self.tech=tech
      self.food=food

class Answers():
    def __init__ (self,sports,politics,popculture,tech,food):
        self.sports=sports
        self.politics=politics
        self.popculture=popculture
        self.tech=tech
        self.food=food


def main():

    ''' Read the files'''
    sports=[]
    politics=[]
    popculture=[]
    tech=[]
    food=[]
    with open('final_project_questions.csv', encoding="UTF-8") as handle:
        reader=csv.DictReader(handle, delimiter=',')

        for row in reader:
            questions = Categories(row['Sports'],row['Politics'],row['Pop Culture'],row['Technology'],row['Food'])

            sports.append(questions.sports)
            politics.append(questions.politics)
            popculture.append(questions.popculture)
            tech.append(questions.tech)
            food.append(questions.food)

    sports_answers=[]
    politics_answers=[]
    popculture_answers=[]
    tech_answers=[]
    food_answers=[]

    with open('final_project_answers.csv', encoding="UTF-8") as handle:
        reader=csv.DictReader(handle, delimiter=',')
        for row in reader:

            answers= Answers(row['Sports'],row['Politics'],row['Pop Culture'],row['Technology'],row['Food'])

            sports_answers.append(answers.sports)
            politics_answers.append(answers.politics)
            popculture_answers.append(answers.popculture)
            tech_answers.append(answers.tech)
            food_answers.append(answers.food)


    '''Prompt User for game'''
    total_points=0
    total_questions=25
    questions_answered=0

    print('Welcome to Jeopardy: Please pick different questions each time (25 different questions)')
    while questions_answered<total_questions:


        user_category=input('Pick a Category: Sports, Politics, Pop Culture, Technology, Food''\n')
        '''For Sports'''
        if user_category=='Sports':
            print(sports)
            user_question=input('Pick a question using a number''\n')
            if user_question == '1':
                print(sports[0])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==sports_answers[0]:
                    print('You earned 100 points')
                    total_points=total_points+100
                    print(total_points)
            elif user_question =='2':
                print(sports[1])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==sports_answers[1]:
                    print('You earned 200 points')
                    total_points=total_points+200
                    print(total_points)
            elif user_question =='3':
                print(sports[2])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==sports_answers[2]:
                    print('You earned 300 points')
                    total_points=total_points+300
                    print(total_points)
            elif user_question =='4':
                print(sports[3])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==sports_answers[3]:
                    print('You earned 400 points')
                    total_points=total_points+400
                    print(total_points)
            elif user_question =='5':
                print(sports[4])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==sports_answers[4]:
                    print('You earned 500 points')
                    total_points=total_points+500
                    print(total_points)

        elif user_category=='Politics':
            print(politics)
            user_question=input('Pick a question using a number''\n')
            if user_question == '1':
                print(politics[0])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==politics_answers[0]:
                    print('You earned 100 points')
                    total_points=total_points+100
                    print(total_points)
            elif user_question =='2':
                print(politics[1])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==politics_answers[1]:
                    print('You earned 200 points')
                    total_points=total_points+200
                    print(total_points)
            elif user_question =='3':
                print(politics[2])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==politics_answers[2]:
                    print('You earned 300 points')
                    total_points=total_points+300
                    print(total_points)
            elif user_question =='4':
                print(politics[3])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==politics_answers[3]:
                    print('You earned 400 points')
                    total_points=total_points+400
                    print(total_points)
            elif user_question =='5':
                print(politics[4])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==politics_answers[4]:
                    print('You earned 500 points')
                    total_points=total_points+500
                    print(total_points)
        elif user_category=='Pop Culture':
            print(popculture)
            user_question=input('Pick a question using a number''\n')
            if user_question == '1':
                print(popculture[0])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==popculture_answers[0]:
                    print('You earned 100 points')
                    total_points=total_points+100
                    print(total_points)
            elif user_question =='2':
                print(popculture[1])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==popculture_answers[1]:
                    print('You earned 200 points')
                    total_points=total_points+200
                    print(total_points)
            elif user_question =='3':
                print(popculture[2])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==popculture_answers[2]:
                    print('You earned 300 points')
                    total_points=total_points+300
                    print(total_points)
            elif user_question =='4':
                print(popculture[3])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==popculture_answers[3]:
                    print('You earned 400 points')
                    total_points=total_points+400
                    print(total_points)
            elif user_question =='5':
                print(popculture[4])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==popculture_answers[4]:
                    print('You earned 500 points')
                    total_points=total_points+500
                    print(total_points)
        elif user_category== 'Technology':
            print(tech)
            user_question=input('Pick a question using a number''\n')
            if user_question == '1':
                print(tech[0])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==tech_answers[0]:
                    print('You earned 100 points')
                    total_points=total_points+100
                    print(total_points)
            elif user_question =='2':
                print(tech[1])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==tech_answers[1]:
                    print('You earned 200 points')
                    total_points=total_points+200
                    print(total_points)
            elif user_question =='3':
                print(tech[2])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==tech_answers[2]:
                    print('You earned 300 points')
                    total_points=total_points+300
                    print(total_points)
            elif user_question =='4':
                print(tech[3])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==tech_answers[3]:
                    print('You earned 400 points')
                    total_points=total_points+400
                    print(total_points)
            elif user_question =='5':
                print(tech[4])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==tech_answers[4]:
                    print('You earned 500 points')
                    total_points=total_points+500
                    print(total_points)
        elif user_category=='Food':
            print(food)
            user_question=input('Pick a question using a number''\n')
            if user_question == '1':
                print(food[0])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==food_answers[0]:
                    print('You earned 100 points')
                    total_points=total_points+100
                    print(total_points)
            elif user_question =='2':
                print(food[1])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==food_answers[1]:
                    print('You earned 200 points')
                    total_points=total_points+200
                    print(total_points)
            elif user_question =='3':
                print(food[2])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==food_answers[2]:
                    print('You earned 300 points')
                    total_points=total_points+300
                    print(total_points)
            elif user_question =='4':
                print(food[3])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==food_answers[3]:
                    print('You earned 400 points')
                    total_points=total_points+400
                    print(total_points)
            elif user_question =='5':
                print(food[4])
                user_answer=input('What is your answer?''\n')
                questions_answered+=1
                if user_answer==food_answers[4]:
                    print('You earned 500 points')
                    total_points=total_points+500
                    print(total_points)
    print('Thanks for playing')
    print(total_points)






if __name__ == '__main__':
    main()
