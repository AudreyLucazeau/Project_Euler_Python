#Brute Force : concatener all the number as a string.
#Note : how to stop, to avoid looking at the len of the string and make and if statement at every passage in the loop,
# some analysis are necessary.

# All the figures from 1-9 represent 1*9 = 9 characters
# All the numbers from 10 to 99 represent 2*90 = 180 characters
...
# All the numbers from 10000 to 99999 represent 5*90000 = 450000 characters

#At this point we have 488889 characters
# To reach 1000000 we need (1000000-488889)/6 more numbers (now that numbers are greater than 1000000)
# Thats means 85186 more numbers


concatenation = ""
for i in range(0,185186):
    concatenation = concatenation + str(i)

print(int(concatenation[1000000])*int(concatenation[100000])*int(concatenation[10000])*int(concatenation[1000])*int(concatenation[100]))

#Note : some manual calculations as begun is the analysis would have been enough 