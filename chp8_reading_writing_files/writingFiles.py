import os

helloFile = open('D:\\auto_py\\chp8_reading_writing_files\\sample.txt')
#print(helloFile)#<_io.TextIOWrapper name='D:\\auto_py\\chp8_reading_writing_files\\sample.txt' mode='r' encoding='cp1252'>

helloContent = helloFile.read()
#print(helloContent)
helloFile = open('chp8_reading_writing_files\\sample.txt')
print(helloFile.readlines())
'''
Output:

['In the first example, "III" represents the number 3. The function correctly converts it to an integer and returns 3.\n', '\n', 'In the second example, "LVIII" represents the number 58. The function converts it to an integer and returns 58.\n', '\n', 'In the third example, "MCMXCIV" represents the number
1994. The function converts it to an integer and returns 1994.\n', '\n', 'Remember, Roman numerals are written from left to right with larger symbols appearing before smaller ones. The only exception is when a smaller symbol appears before a larger one, indicating subtraction.\n', '\n', 'I hope this explanation makes it clear how to convert Roman numerals to integers! Let me know if you have any further questions.']

'''

#WRITING FILES


sample2File = open('sample2.txt', 'w')
sample2File.write('Hello world\n')#12
sample2File.close()
sample2File = open('sample2.txt', 'a')
sample2File.write('The Mansaba has returned, its time to get started.')
sample2File.close()
sample2File = open('sample2.txt')
content = sample2File.read()
print(sample2File.close())
print(content)

