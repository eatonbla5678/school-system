''' School System Copyright By Blake Eaton.
    Do not use without my exclusive permission.
    Use my email to ask for permissions: blake.eaton@gmail.com
    Thank you.
    '''


g = 89
h = 98
i = 92
k = "History"
l = "Language Arts"
m = "Math"
p = "A"
q = "B"
r = "C"


def john():
    global g
    g = input('What would you like to change the grade to?\n> ')

def sarah():
    global h
    h = input('What would you like to change the grade to?\n> ')

def alan():
    global i
    i = input('What would you like to change the grade to?\n> ')



def johncc():
    global k
    k = input('What would you like to change the class to?\n> ')

def sarahcc():
    global l
    l = input('What would you like to change the class to?\n> ')

def alancc():
    global m
    m = input('What would you like to change the class to?\n> ')



def johnrc():
    global p
    p = input('What would you like to change the room to?\n> ')

def sarahrc():
    global q
    q = input('What would you like to change the room to?\n> ')

def alanrc():
    global r
    r = input('What would you like to change the room to?\n> ')


def rc():
  print('The students are: John, Sarah, and Alan.')
  global s
  s = input('Which student\'s room do you want to change?\n> ')
  if ('John' in s):
    johnrc()
  elif ('john' in s):
    johnrc()
  elif ('j' in s):
    johnrc()
  elif ('Sarah' in s):
    sarahrc()
  elif ('sarah' in s):
    sarahrc()
  elif ('s' in s):
    sarahrc()
  elif ('Alan' in s):
    alanrc()
  elif ('alan' in s):
    alanrc()
  elif ('a' in s):
    alanrc()
  global t
  t = input('Do you want to change another student\'s room? [yes|no]\n> ')
  if(t == 'yes'):
    cc()
  elif(t == 'y'):
    cc()
  elif(t == 'no'):
    print('Exiting the RoomChanger System...')
    print('Done \n ')
    greeting()
  elif(t == 'n'):
    print('Exiting the RoomChanger System...')
    print('Done \n ')
    greeting()
  else:
    print('Error: Invalid')
    print('Exiting the RoomChanger System...')
    print('Done \n ')
    greeting()

def cc():
  print('The students are: John, Sarah, and Alan.')
  global n
  n = input('Which student\'s class do you want to change?\n> ')
  if ('John' in n):
    johncc()
  elif ('john' in n):
    johncc()
  elif ('j' in n):
    johncc()
  elif ('Sarah' in n):
    sarahcc()
  elif ('sarah' in n):
    sarahcc()
  elif ('s' in n):
    sarah()
  elif ('Alan' in n):
    alancc()
  elif ('alan' in n):
    alancc()
  elif ('a' in n):
    alancc()
  global o
  o = input('Do you want to change another student\'s class? [yes|no]\n> ')
  if(o == 'yes'):
    cc()
  elif(o == 'y'):
    cc()
  elif(o == 'no'):
    print('Exiting the ClassChanger System...')
    print('Done \n ')
    greeting()
  elif(o == 'n'):
    print('Exiting the ClassChanger System...')
    print('Done \n ')
    greeting()
  else:
    print('Error: Invalid')
    print('Exiting the ClassChanger System...')
    print('Done \n ')
    greeting()

def gc():
  print('The students are: John, Sarah, and Alan.')
  global f
  f = input('Which student\'s grade do you want to change?\n> ')
  if ('John' in f):
    john()
  elif ('john' in f):
    john()
  elif ('j' in f):
    john()
  elif ('Sarah' in f):
    sarah()
  elif ('sarah' in f):
    sarah()
  elif ('s' in f):
    sarah()
  elif ('Alan' in f):
    alan()
  elif ('alan' in f):
    alan()
  elif ('a' in f):
    alan()
  global j
  j = input('Do you want to change another student\'s grade? [yes|no]\n> ')
  if(j == 'yes'):
    gc()
  elif(j == 'y'):
    gc()
  elif(j == 'no'):
    print('Exiting the GradeChanger System...')
    print('Done \n ')
    greeting()
  elif(j == 'n'):
    print('Exiting the GradeChanger System...')
    print('Done \n ')
    greeting()
  else:
    print('Error: Invalid')
    print('Exiting the GradeChanger System...')
    print('Done \n ')
    greeting()

def grade():
  print('The students are: John, Sarah, and Alan.')
  global b
  b = input('Which student do you want to see the grade of?\n> ')
  if (b == 'John'):
    print("His grade is: ")
    print(g)
  elif (b == 'john'):
    print("His grade is: ")
    print(g)
  elif (b == 'j'):
    print("His grade is: ")
    print(g)
  elif (b == 'Sarah'):
    print("Her grade is: ")
    print(h)
  elif (b == 'sarah'):
    print("Her grade is: ")
    print(h)
  elif (b == 's'):
    print("Her grade is: ")
    print(h)
  elif (b == 'Alan'):
    print("His grade is: ")
    print(i)
  elif (b == 'alan'):
    print("His grade is: ")
    print(i)
  elif (b == 'a'):
    print("His grade is: ")
    print(i)
  else:
      print('Error: Invalid')
      grade()
  global e
  e = input('Do you want to see another student\'s grade? [yes|no]\n> ')
  if(e == 'yes'):
    grade()
  elif(e == 'y'):
    grade()
  elif(e == 'no'):
    print('Exiting the GradePoint System...')
    print('Done \n ')
    greeting()
  elif(e == 'n'):
    print('Exiting the GradePoint System...')
    print('Done \n ')
    greeting()
  else:
    print('Error: Invalid')
    print('Exiting the GradePoint System...')
    print('Done \n ')
    greeting()

def cv():
  print('The students are: John, Sarah, and Alan.')
  global d
  d = input('Which student\'s class do you wish to see?\n> ')
  if (d == 'John'):
    print("His class is: ")
    print(k)
  elif (d == 'john'):
    print("His class is: ")
    print(k)
  elif (d == 'j'):
    print("His class is: ")
    print(k)
  elif (d == 'Sarah'):
    print("Her class is: ")
    print(l)
  elif (d == 'sarah'):
    print("Her class is: ")
    print(l)
  elif (d == 's'):
    print("Her class is: ")
    print(l)
  elif (d == 'Alan'):
    print("His class is: ")
    print(m)
  elif (d == 'alan'):
    print("His class is: ")
    print(m)
  elif (d == 'a'):
    print("His class is: ")
    print(m)
  global a
  a = input('Do you want to see another student\'s class? [yes|no]\n> ')
  if(a == 'yes'):
    cv()
  elif(a == 'y'):
    cv()
  elif(a == 'no'):
    print('Exiting the ClassViewer System...')
    print('Done \n ')
    greeting()
  elif(a == 'n'):
    print('Exiting the ClassViewer System...')
    print('Done \n ')
    greeting()
  else:
    print('Error: Invalid')
    print('Exiting the ClassViewer System...')
    print('Done \n ')
    greeting()

def rv():
  print('The students are: John, Sarah, and Alan.')
  global u
  u = input('Which student\'s room do you wish to see?\n> ')
  if (u == 'John'):
    print("His room is: ")
    print(p)
  elif (u == 'john'):
    print("His room is: ")
    print(p)
  elif (u == 'j'):
    print("His room is: ")
    print(p)
  elif (u == 'Sarah'):
    print("Her room is: ")
    print(q)
  elif (u == 'sarah'):
    print("Her room is: ")
    print(q)
  elif (u == 's'):
    print("Her room is: ")
    print(q)
  elif (u == 'Alan'):
    print("His room is: ")
    print(r)
  elif (u == 'alan'):
    print("His room is: ")
    print(r)
  elif (u == 'a'):
    print("His room is: ")
    print(r)
  global v
  v = input('Do you want to see another student\'s room? [yes|no]\n> ')
  if(v == 'yes'):
    cv()
  elif(v == 'y'):
    cv()
  elif(v == 'no'):
    print('Exiting the RoomViewer System...')
    print('Done \n ')
    greeting()
  elif(v == 'n'):
    print('Exiting the RoomViewer System...')
    print('Done \n ')
    greeting()
  else:
    print('Error: Invalid')
    print('Exiting the RoomViewer System...')
    print('Done \n ')
    greeting()

def greeting():
  print('Welcome to the School System \n ')
  global w
  w = input('Which Power System do you wish to use? [Grade|Class|Room|Exit]\n> ')
  if (w == 'Grade'):
    global c
    c = input('Which Power Program do you wish to use? [GradePoint|GradeChanger|Exit]\n> ')
    if (c == 'GradePoint'):
      grade()
    elif (c == 'gradepoint'):
      grade()
    elif (c == 'gp'):
      grade()
    elif (c == 'GradeChanger'):
      gc()
    elif (c == 'gradechanger'):
      gc()
    elif (c == 'gc'):
      gc()
    elif (c == 'Exit'):
      print('Exiting the Grade System...')
      print('Done')
      greeting()
    elif (c == 'exit'):
      print('Exiting the Grade System...')
      print('Done')
      greeting()
    elif (c == 'e'):
      print('Exiting the Grade System...')
      print('Done')
      greeting()
    else:
      print('Error: Invalid')
      greeting()

  elif (w == 'grade'):
    global z
    z = input('Which Power Program do you wish to use? [GradePoint|GradeChanger|Exit]\n> ')
    if (z == 'GradePoint'):
      grade()
    elif (z == 'gradepoint'):
      grade()
    elif (z == 'gp'):
      grade()
    elif (z == 'GradeChanger'):
      gc()
    elif (z == 'gradechanger'):
      gc()
    elif (z == 'gc'):
      gc()
    elif (z == 'Exit'):
      print('Exiting the Grade System...')
      print('Done')
      greeting()
    elif (z == 'exit'):
      print('Exiting the Grade System...')
      print('Done')
      greeting()
    elif (z == 'e'):
      print('Exiting the Grade System...')
      print('Done')
      greeting()
    else:
      print('Error: Invalid')
      greeting()

  elif (w == 'G'):
    global aa
    aa = input('Which Power Program do you wish to use? [GradePoint|GradeChanger|Exit]\n> ')
    if (aa == 'GradePoint'):
      grade()
    elif (aa == 'gradepoint'):
      grade()
    elif (aa == 'gp'):
      grade()
    elif (aa == 'GradeChanger'):
      gc()
    elif (aa == 'gradechanger'):
      gc()
    elif (aa == 'gc'):
      gc()
    elif (aa == 'Exit'):
      print('Exiting the Grade System...')
      print('Done')
      greeting()
    elif (aa == 'exit'):
      print('Exiting the Grade System...')
      print('Done')
      greeting()
    elif (aa == 'e'):
      print('Exiting the Grade System...')
      print('Done')
      greeting()
    else:
      print('Error: Invalid')
      greeting()

  elif (w == 'g'):
    global ab
    ab = input('Which Power Program do you wish to use? [GradePoint|GradeChanger|Exit]\n> ')
    if (ab == 'GradePoint'):
      grade()
    elif (ab == 'gradepoint'):
      grade()
    elif (ab == 'gp'):
      grade()
    elif (ab == 'GradeChanger'):
      gc()
    elif (ab == 'gradechanger'):
      gc()
    elif (ab == 'gc'):
      gc()
    elif (ab == 'Exit'):
      print('Exiting the Grade System...')
      print('Done')
      greeting()
    elif (ab == 'exit'):
      print('Exiting the Grade System...')
      print('Done')
      greeting()
    elif (ab == 'e'):
      print('Exiting the Grade System...')
      print('Done')
      greeting()
    else:
      print('Error: Invalid')
      greeting()

  elif (w == 'Class'):
    global x
    x = input('Which Power Program do you wish to use? [ClassViewer|ClassChanger|Exit]\n> ')
    if (x == 'ClassViewer'):
      cv()
    elif (x == 'classviewer'):
      cv()
    elif (x == 'cv'):
      cv()
    elif (x == 'ClassChanger'):
      cc()
    elif (x == 'classchanger'):
      cc()
    elif (x == 'cc'):
      cc()
    elif (x == 'Exit'):
      print('Exiting the Class System...')
      print('Done')
      greeting()
    elif (x == 'exit'):
      print('Exiting the Class System...')
      print('Done')
      greeting()
    elif (x == 'e'):
      print('Exiting the Class System...')
      print('Done')
      greeting()
    else:
      print('Error: Invalid')
      greeting()

  elif (w == 'class'):
    global ac
    ac = input('Which Power Program do you wish to use? [ClassViewer|ClassChanger|Exit]\n> ')
    if (ac == 'ClassViewer'):
      cv()
    elif (ac == 'classviewer'):
      cv()
    elif (ac == 'cv'):
      cv()
    elif (ac == 'ClassChanger'):
      cc()
    elif (ac == 'classchanger'):
      cc()
    elif (ac == 'cc'):
      cc()
    elif (ac == 'Exit'):
      print('Exiting the Class System...')
      print('Done')
      greeting()
    elif (ac == 'exit'):
      print('Exiting the Class System...')
      print('Done')
      greeting()
    elif (ac == 'e'):
      print('Exiting the Class System...')
      print('Done')
      greeting()
    else:
      print('Error: Invalid')
      greeting()

  elif (w == 'C'):
    global ad
    ad = input('Which Power Program do you wish to use? [ClassViewer|ClassChanger|Exit]\n> ')
    if (ad == 'ClassViewer'):
      cv()
    elif (ad == 'classviewer'):
      cv()
    elif (ad == 'cv'):
      cv()
    elif (ad == 'ClassChanger'):
      cc()
    elif (ad == 'classchanger'):
      cc()
    elif (ad == 'cc'):
      cc()
    elif (ad == 'Exit'):
      print('Exiting the Class System...')
      print('Done')
      greeting()
    elif (ad == 'exit'):
      print('Exiting the Class System...')
      print('Done')
      greeting()
    elif (ad == 'e'):
      print('Exiting the Class System...')
      print('Done')
      greeting()
    else:
      print('Error: Invalid')
      greeting()

  elif (w == 'c'):
    global ae
    ae = input('Which Power Program do you wish to use? [ClassViewer|ClassChanger|Exit]\n> ')
    if (ae == 'ClassViewer'):
      cv()
    elif (ae == 'classviewer'):
      cv()
    elif (ae == 'cv'):
      cv()
    elif (ae == 'ClassChanger'):
      cc()
    elif (ae == 'classchanger'):
      cc()
    elif (ae == 'cc'):
      cc()
    elif (ae == 'Exit'):
      print('Exiting the Class System...')
      print('Done')
      greeting()
    elif (ae == 'exit'):
      print('Exiting the Class System...')
      print('Done')
      greeting()
    elif (ae == 'e'):
      print('Exiting the Class System...')
      print('Done')
      greeting()
    else:
      print('Error: Invalid')
      greeting()

  elif (w == 'Room'):
    global y
    y = input('Which Power Program do you wish to use? [RoomViewer|RoomChanger|Exit]\n> ')
    if(y == 'RoomViewer'):
      rv()
    elif(y == 'roomviewer'):
      rv()
    elif (y == 'RoomChanger'):
      rc()
    elif (y == 'roomchanger'):
      rc()
    elif (y == 'rv'):
      rv()
    elif (y == 'rc'):
      rc()
    elif (y == 'Exit'):
      print('Exiting the School System...')
      print('Done')
      greeting()
    elif (y == 'exit'):
      print('Exiting the School System...')
      print('Done')
      greeting()
    elif (y == 'e'):
      print('Exiting the School System...')
      print('Done')
      greeting()
    else:
      print('Error: Invalid')
      greeting()

  elif (w == 'room'):
    global af
    af = input('Which Power Program do you wish to use? [RoomViewer|RoomChanger|Exit]\n> ')
    if (af == 'RoomViewer'):
      rv()
    elif (af == 'roomviewer'):
      rv()
    elif (af == 'RoomChanger'):
      rc()
    elif (af == 'roomchanger'):
      rc()
    elif (af == 'rv'):
      rv()
    elif (af == 'rc'):
      rc()
    elif (af == 'Exit'):
      print('Exiting the School System...')
      print('Done')
      greeting()
    elif (af == 'exit'):
      print('Exiting the School System...')
      print('Done')
      greeting()
    elif (af == 'e'):
      print('Exiting the School System...')
      print('Done')
      greeting()
    else:
      print('Error: Invalid')
      greeting()

  elif (w == 'R'):
    global ag
    ag = input('Which Power Program do you wish to use? [RoomViewer|RoomChanger|Exit]\n> ')
    if (ag == 'RoomViewer'):
      rv()
    elif (ag == 'roomviewer'):
      rv()
    elif (ag == 'RoomChanger'):
      rc()
    elif (ag == 'roomchanger'):
      rc()
    elif (ag == 'rv'):
      rv()
    elif (ag == 'rc'):
      rc()
    elif (ag == 'Exit'):
      print('Exiting the School System...')
      print('Done')
      greeting()
    elif (ag == 'exit'):
      print('Exiting the School System...')
      print('Done')
      greeting()
    elif (ag == 'e'):
      print('Exiting the School System...')
      print('Done')
      greeting()
    else:
      print('Error: Invalid')
      greeting()

  elif (w == 'r'):
    global ah
    ah = input('Which Power Program do you wish to use? [RoomViewer|RoomChanger|Exit]\n> ')
    if (ah == 'RoomViewer'):
      rv()
    elif (ah == 'roomviewer'):
      rv()
    elif (ah == 'RoomChanger'):
      rc()
    elif (ah == 'roomchanger'):
      rc()
    elif (ah == 'rv'):
      rv()
    elif (ah == 'rc'):
      rc()
    elif (ah == 'Exit'):
      print('Exiting the School System...')
      print('Done')
      greeting()
    elif (ah == 'exit'):
      print('Exiting the School System...')
      print('Done')
      greeting()
    elif (ah == 'e'):
      print('Exiting the School System...')
      print('Done')
      greeting()
    else:
      print('Error: Invalid')
      greeting()

greeting()
