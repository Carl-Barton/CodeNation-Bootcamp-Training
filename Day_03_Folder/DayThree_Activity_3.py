# Objective: Create a variable called num.
# If num is divisible by 3 print "fizz", if it's divisible by 7 print "buzz",
# if it's divisible by both 3 and 7 print "fizzbuzz"
# Other wise print num

num = int(input("input number: "))

if num % 3 == 0 and num % 7 == 0:
    print('fizzbuzz')
elif num % 3 == 0:                       
    print('fizz')                         
elif num % 7 == 0:
    print('buzz') 
else:
    print(num)