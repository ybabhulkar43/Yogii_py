user_input = input('Are you hungry? ')

if user_input.lower() == 'yes':
     print('Eat samosa..')
     print('Eat burger..')
     print('Eat pizza..')
else:
     thirsty = input('Are you thirsty? ')
     if thirsty.lower() == 'yes':
          print('Drink water..')
          print('Drink soda..')
          print('drink juice...')
          print('Drink milk...')
     else:
          print('Okay, have a nice day!')
