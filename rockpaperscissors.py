rock = 0
paper = 1
scissors = 2
import random
import my_module
# randomNumber = random.randint(4, 18)
# #random.random() generates a random float between 0 and 1
# #random.uniform(a, b) generates a random float between a and b
# print(randomNumber)
# print(randomNumber * my_module.favorite_number)
# random.choice()
# random_index = random.randint(0, 4)
# bill_payer = my_module.friends[random_index]
# print(bill_payer)
# input is always a string so we need to turn it into an int() to compare
print("It's time for rock, paper, scissors! Type 0 for rock, 1 for paper, or 2 for scissors")
user_input = int(input())
print(user_input)
cpu_input = random.randint(0, 2)
print(cpu_input)
if user_input == 0 and cpu_input == 1:
    print("You chose paper, CPU chose scissors, you lose!")
elif user_input == 1 and cpu_input == 0:
    print("You chose scissors, CPU chose paper, you win!")
elif user_input == 2 and cpu_input == 0:
    print("You chose scissors, CPU chose rock, you lose!")
elif user_input == 0 and cpu_input == 2:
    print("You chose rock, CPU chose scissors, you win!")
elif user_input == 1 and cpu_input == 2:
    print("You chose paper, CPU chose scissors, you lose!")
elif user_input == 2 and cpu_input == 1:
    print("You chose scissors, CPU chose paper, you lose!")
elif user_input == cpu_input:
    print("It's a draw")
else:
    print("Try again")
