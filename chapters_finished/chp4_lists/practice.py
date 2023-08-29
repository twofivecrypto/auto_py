#1
print("an empty list = []")
#2
spam = [2, 4, 6, 8 ,10]
spam.insert(2, 'world')
print(spam)
#3,4, 5
spam = ['a', 'b', 'c', 'd']

print(spam[int(int('3' * 2) // 11)]) #'d'
print(spam[-1]) #'d'
print(spam[:2]) #'a', 'b'

#6,7, 8
bacon = [3.14, 'cat', 11, 'cat', True]
print(bacon.index('cat')) #[1]
print(bacon.append(99)) #None
print(bacon.remove('cat'))#None
print(bacon)

#9
print("\n\t\tthe '+' and '*' operators are used to concatenate and duplicate lists (+/*)\n")

#10
print("The difference between append() & insert() methods are: \n")
print("\tThe append() method adds the value to the end of the list, while\n" +
      "\t\tthe insert() method allows you to control which index the value goes into.\n")

#11
print("Two ways to remove values from a list are:\n" +
      "\tthe remove() method and:\n" + "\t\t the del() method.\n")

#12
list_values = ['slicing', 'for loops', 'len()', 'indexing', 'in & not in operators']
string_values = list_values
print('String values contains the same items list values does:')
print('\tList Values: \n' + '\t\t' + str(list_values) + '\n\t\t\tString Values: ' + '\n\t\t\t\t' + str(list_values))

#13
print("\nLists and tuples are different in two ways:\n" +
      "\t 1. Tuples are typed with (), instead of [] and: \n" +
      "\t\t 2. The MAIN way the differ is that TUPLES ARE IMMUTABLE, their contents don't change.\n")

#14
print("A tuple with an interger value of '42' can be displayed as such:\n" + "\tnumber = (42)\n")

#15
print("The list form of a tuple can be displayed like so:\n")
'''
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)

output : (1, 2, 3, 4, 5)
'''
print("The tuple form of a list value can be displayed as such:\n")
'''
my_list(a, b, c, d, e)
my_tuple = tuple(my_list)
print(my_tuple)

output : [a, b, c, d, e]
'''
print("extra credit:\n")
'''
list('hello')
output : ['h', 'e', 'l', 'l', 'o']
'''
#16
print("they actually contain 'items', not list values.\n")

#17
print("The difference between 'copy.copy()' & 'copy.deepcopy()' are:\n" +
      "\tcopy.copy() allows changes to the original to occur to the copy version while:\n" + 
      "\t\tcopy.deepcopy() becomes it's own object, not affected by changes to the original.\n")

'''
copy.copy()
--------------
import copy

original_list = [1, 2, [3, 4]]
copied_list = copy.copy(original_list)

original_list[2].append(5)

print(original_list)  # [1, 2, [3, 4, 5]]
print(copied_list)  # [1, 2, [3, 4, 5]]

copy.deepcopy()
----------------
import copy

original_list = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list)

original_list[2].append(5)

print(original_list)  # [1, 2, [3, 4, 5]]
print(deep_copied_list)  # [1, 2, [3, 4]]
'''

