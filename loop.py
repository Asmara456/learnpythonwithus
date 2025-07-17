# for loop
# syntax of for loop is for variable in interatives :
# print counting from 1 to 8

for i in range(1,9):
    print(i)
for i in list["asmara",34,True] :
    print(i)  
for i in "python" :
    if i=="h":
      break
    print (i)
i=2
while i<6:
    print("hello world")  
    i+=1
i=1    
while i<=5:
    if i==3:
        break 
    i+=1
    print(i) 
for i in range (1,11):
    print(i) 
for i in range(2,21,2):
    print(i) 
    
# sum of first 10 natural numbers     
sum=0
for i in range (1,11) :
    sum+=i
print("sum is ",sum)                  
    
sum = 0
for i in range(1, 11):
    sum += i
print("Sum is:", sum)         



# table of a number 
num=5
for i in range (1,11):
    print (f"{num}*{i}={num*i}")
num=13
for i in range (1,13)   :
    print(f"{num}*{i}={num*i}") 


# factorial of a number 
num=4
fact=1
for i in range(1,num+1) :
    fact=fact*i
print("factorial is ", fact ) 



# prime number or not.....
num=int(input("enter a number :" ))
is_prime=True
for i in range(1,num):
    if num%i==0:
        is_prime==False
        print("number is not prime ")
        break 
    else :
        print("numer is prime ") 



# reverse of the number
num=int(input("enter a number "))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num//=10 
print("reversed number is ",reverse )  


# printing star 
for i in range(1, 6):
    print("*" * i)



# guessing the number using while loop 

import random

def guess_the_number():
    print("Welcome to the Number Guessing Game ! ")
    secret_number = random.randint(1,20)
    attempts = 0
    max_attempts = 5
    while attempts < max_attempts :
        try :
            guess = int(input(f"Attempt{attempts + 1}. Guess a number between 1 and 20 : "))
            attempts += 1
            if guess < 1 or guess > 20 :
                print("Please guess a number within range ! ")
            elif guess < secret_number :
                print("Too low ! Try again ")
            elif guess > secret_number :
                print("Too high ! Try again ")
            else :
                print(f"Congratulations ! you guessed it in {attempts} attempts ")
                break 

        except ValueError:
            print("Please enter a valid number ")

    if guess != secret_number :
        print(f"Game over ! The correct number was {secret_number}.")

guess_the_number()




# guessing alphabet correctly
import random
import string

def guess_the_alphabet():
    print(" Welcome to the Alphabet Guessing Game")

    secret_letter = random.choice(string.ascii_uppercase)  
    attempts = 0
    max_attempts = 6  

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}. Guess a letter (A-Z): ").upper()

        if len(guess) != 1 or guess not in string.ascii_uppercase:
            print(" Invalid input! Please enter a single letter from A to Z.")
            continue  

        attempts += 1

        if guess < secret_letter:
            print(" Too low alphabetically. Try again!")
        elif guess > secret_letter:
            print(" Too high alphabetically. Try again!")
        else:
            print(f" Correct! You guessed the letter '{secret_letter}' in {attempts} attempts.")
            break

    if guess != secret_letter:
        print(f" Game Over! The correct letter was '{secret_letter}'.")

# Start the game
guess_the_alphabet()






         






