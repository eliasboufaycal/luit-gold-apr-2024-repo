user_age = int(input('What is your age? '))
if user_age > 30:
    print('You are over 30 years old and you do not qualify.')

elif user_age == 30:
    print('You are exactly 30 years old, and you will need additional docymentation to qualify.')
    
else:
    print('You are less than 30 years old, congratulations you qualify.')
    