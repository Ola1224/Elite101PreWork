import random
#Used, but altered from C2C Samples

intro_name = input("Hello, what is your name? ")
print("Nice to meet you, " + intro_name  + ". My name is Chase!")


def myFeeling(feeling):
  randresp1 = random.randint(1,2)
  randresp2 = random.randint(1,2)
  goodFeelings = ["good","happy" , "great" , "excellent"]
  badFeelings = ["sad","tired","not good", "bad"]

  if feeling in goodFeelings:
      if randresp1 == 1:
          print("That's great!")
      elif randresp1 == 2:
          print("How nice!")
  elif  feeling in badFeelings:
      if randresp2 == 1:
          print("That's sad to hear! Don't worry you much.")
      elif randresp2 == 2:
          print("I hope it gets better!")


feeling = input("\nHow are you today? ").lower()
myFeeling(feeling)
#asking for age
def myAge(age):
  response3 = random.randint(1, 2)

  if age <15:
      if response3 == 1:
          print("Wow you're quite young! What do you like doing?")
      elif response3 == 2:
          print("Interesting!")
  elif age >= 15 and age < 18:
      print("That's great! You should start planning your future!")

  elif age >= 18 and age < 55:
      print("Oh great, you're an adult!")
  elif age >= 55 and age<120:
      print("I hope your day is going well!")
  else:
      print("That's unbelievable! Try again.")
      age2 = int(input("What is your age?"))
      if age2<=120:
        print("Okay! This more like an age number.")


age = int(input("\nHow old are you? "))
myAge(age)

# from stack overflow
from random import randint

colors = ['red', 'blue', 'black', 'pink']
generator = randint(0,len(colors)-1)
guess = input('guess a color: ')

for color in colors[generator]:
    if guess != colors[generator]:
        print('wrong, try again')
        guess = input('guess a color: ')
    elif guess == colors[generator]:
        break


print('yay, color was: ' + colors[generator])