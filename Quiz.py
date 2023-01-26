import time

print("Welcome to Rico's quiz")
time.sleep(2)
print('You will be faced with 10 question, answer one wrong and you will have to restart')
time.sleep(3)
print('You have 5 tries. Best of luck')
time.sleep(2)
print('you may begin!')
time.sleep(1)
question = input('Do you play Fortnite?')
if question == 'yes':
    print('WRONG ANSWER, RESTART :)')
    exit()
else:
    print('Congrats u finish the first question, 9 more to go!')
time.sleep(1)
question = input('Do you play valorant?')
if question == "no":
    exit()
else:
    print('Smart answer')
time.sleep(1)
question = input('Solve: 8x+14=58')
if question == "10":
    print('WRONG ANSWER, RESTART :)')
    exit()
else:
    print("I Would have laughed if you got that wrong")
time.sleep(1)
question = input("How many letters are in the alphabet?")
if question == "11":
    print('smart man, smart man')
else:
    print("WRONG ANSWER")
    exit()
time.sleep(1)
question = input('How many properties of matter are there?')
if question == '4':
    print('Wrong')
    exit()
else:
    print("At least you know the basics")
time.sleep(1)
question = input('Is this gramaticaly correct: Bob had they\'re nails done')
if question == 'no':
    print('Meeting my expectations')
else:
    print('NO WAY U GOT THAT RIGHT!')
    time.sleep(2)
    print('Jk')
    exit()
question = input("What does  être  mean in english")
if question == 'to be':
    print ('wiwi, baget baget')
else:
    print ('Wrong, Mr french man')
    exit()
time.sleep(1)
question = input('What is the capital of Canada')
if question == 'Quebec':
    print ('Ur an idiot')
    exit()
else:
    print('you better have gotten that right')
question = input('How many provinces are there?')
if question == '11':
    print('ur canadian...')
    exit()
else:
    print('Good job, you can answer grade 3 questions')
time.sleep(1)
print('Last question')
time.sleep(1)
print('Are you ready?')
time.sleep(1)
print('you better be')
time.sleep(1)
print('Hear we go')
time.sleep(3)
question = input('In overwatch how much damage does 1 Genji shuriken do?')
if question == "27":
    time.sleep(2)
    print('U DONT EVEN KNOW UR MAIN HAHAHH')
    time.sleep(2)
    print('just kidding u won')
else:
    time.sleep(2)
    print('Back to the beginning u go')



