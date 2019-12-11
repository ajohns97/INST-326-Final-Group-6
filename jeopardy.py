import csv

class Categories():
  def __init__(self,sports,politics,popculture,tech,food):
      self.sports=sports
      self.politics=politics
      self.popculture=popculture
      self.tech=tech
      self.food=food
      

def main():
  hundred=[]
  
  
  with open('final_project_questions.csv') as handle:
    reader=csv.DictReader(handle, delimiter=',')
     for row in reader:
      questions=Categories(row['Sports],row['Politics'],row['Pop Culture'],row['Technology'],row['Food']
      hundred.append[questions.sports[0]
      
  user_input=''
  
