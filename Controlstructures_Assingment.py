num = 6
if num % 2 == 0:
  print('The number is even')
else:
  print('The number is odd')


my_list = ["London", "Moscow", "New York", "Auckland", "Cape Town"]
if len(my_list) == 0:
    print('The list is empty')
else: 
   print('The list is not empty')


num = 7
if num % 2 == 0:
   print('The number is even')
else:
   print('The number is odd')


temp = 15.07
if temp <= 0:
   print('It\'s Freezing Cold')
elif temp <= 10:
   print('It\'s Cold')
elif temp <= 20: 
   print('It\'s Moderate')
elif temp <= 25:
   print('It\'s Warm')
else:
   print('It\'s Hot!')


string = 'Hello, World'
for chair in string:
   print(chair)


squares = [i ** 2 for i in range(1, 11)]
print(squares)


total_sum = 0
current_number = 1
while total_sum <100: 
   total_sum += current_number
   current_number += 1
print('The sum of numbers untill reaching 100 is:', total_sum)