def spam():
    global eggs
    eggs = 'spam' #this is the global

def bacon():
    eggs = 'bacon' #this is a local

def ham():
    print(eggs) #call to the global

eggs = 42 #this is now the global
spam()
print(eggs)


print('\n----------\nThe following code produces an error.')
print('\nYou may not code a function that uses a local variable (eggs)' +
      'and then later in that same function use the same variable (global eggs)\n' +
      '------------\n')

def spam():
    print(eggs) #ERROR IS RIGHT HERE
    eggs = 'spam local'

eggs = 'global'
spam()