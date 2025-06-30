from random import shuffle
import sys
from Dataaccess import getlines

print(f'\n\nYour Quiz Starting...\n\nYour args passed in are: {sys.argv}')

questionFile=''
Filechoice = True
if (len(sys.argv)==1):
 print('\nsys.argv has length of: %s' % len(sys.argv))
 # FIXME: rather than default to a file, we should be adjusting for accessing data in a DB
 # at some point, this could mean using vector similarity and allow for semantic matches rathar than exact token/string match
 questionFile="mytest.tsv"
 #print('You will be tested from questions in the default file: mytest.tsv')
 print('You will receive questions NOT FROM A FILE')
 Filechoice = False

else:
 questionFile=sys.argv[1]
 print('you asked for questions from the file: %s' % sys.argv[1])

#getlines returns class 'list' of strings which are questions and answers

lines = getlines(Filechoice, questionFile)

shuffle(lines)
#numRight is a variable that keeps track of how many correct answers
numRight = 0
# wrong is a new variable for a list of all the questions that were wrongly answered
wrong = []

numQuestions = int(input("How many questions? "))
try:
 for line in lines[:numQuestions]:
  question, rightAnswer = line.strip().split("~")
  answer = input(question + ' ')
  if answer.upper().strip() == rightAnswer.upper().strip():
   print('Right!')
   numRight += 1
  else:
   print('No, the answer is %s.' % rightAnswer)
   wrong.append(question)
except:
 raise

print('You got %i right' % (numRight))
if (wrong):
    print('You got these wrong: ')
    for questionthatiswrong in wrong:
        print(questionthatiswrong)

percentage = ((numRight*1.0)/numQuestions)
percentage = float(percentage * 100.00)
print('\nYour percentage is:   %s' %str(percentage))
