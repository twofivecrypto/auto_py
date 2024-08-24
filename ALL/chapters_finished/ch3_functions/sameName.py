'''
LOCAL & GLOBAL SCOPES MATTER BECAUSE:

 - CODE IN THE GLOBAL SCOPE CANNOT USE ANY LOCAL VARIABLES
 - LOCAL SCOPES CAN HOWEVER USE GLOBAL SCOPES
 - CODE IN FUNCTIONS LOCAL SCOPE CANNOT USE OTHER LOCAL SCOPE'S VARABLES
 - YOU CAN USE THE SAME VARIABLE NAMES FOR DIFFERENT SCOPES
'''

#SCOPES

def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)