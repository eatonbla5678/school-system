
''' School System Copyright By Blake Eaton.
    Do not use without my exclusive permission.
    Use my gmail to ask for permissions: blake.eaton@gmail.com
    Thank you.
    '''

students =  { "John" : 89, "Sarah" : 94, "Alan" : 84 }
classes = { "John" : "History", "Sarah" : "Language Arts", "Alan" : "Math" }

def grade():
  print('The students are: John, Sarah, and Alan.')
  b = input('Which student do you want to see the grade of?')
  if (b == 'John'):
    print("His grade is: ")
    print(students["John"])
  elif (b == 'Sarah'):
    print("Her grade is: ")
    print(students["Sarah"])
  else:
    print("His grade is: ")
    print(students["Alan"])
  e = input('Do you want to see another student\'s grade? [yes|no]')
  if(e == 'yes'):
    grade()
  else:
    print('Exiting the GradePoint System...')
    print('Done')
    greeting()

def cc():
  print('The students are: John, Sarah, and Alan.')
  d = input('Which student\'s class do you wish to see?')
  if (d == 'John'):
    print("His class is: ")
    print(classes["John"])
  elif (d == 'Sarah'):
    print("Her class is: ")
    print(classes["Sarah"])
  else:
    print("His class is: ")
    print(classes["Alan"])
  a = input('Do you want to see another student\'s class? [yes|no]')
  if(a == 'yes'):
    cc()
  else:
    print('Exiting the ClassCollector System...')
    print('Done')
    greeting()
    
def greeting():
  print('Welcome to the School System \n ')
  c = input('What Power Program do you wish to use? [GradePoint|ClassCollector|Exit]')
  if(c == 'GradePoint'):
    grade()
  elif(c == 'ClassCollector'):
    cc()
  else:
    print('Exiting the School System...')
    print('Done')
    exit()
    
greeting()
