print("""
  ___         _     ___
 | _ \___  __| |__ | _ \__ _ _ __  ___ _ _
 |   / _ \/ _| / / |  _/ _` | '_ \/ -_) '_|
 |_|_\___/\__|_\_\ |_| \__,_| .__/\___|_|
 / __| __(_)______ ___ _ _ _|_|
 \__ \/ _| (_-<_-</ _ \ '_(_-<
 |___/\__|_/__/__/\___/_| /__/    Game By Muhammad Hanan Asghar       """)



import random
from time import sleep


user_points = 0
computer_points = 0
print("")
print("""
Rules:
1. You Have to Made A Choice Between 5 Sec.
2. Whoever wins gets a point.
3. After 3 Points Game is Closed.And Player Wins.
""")

print()
print("""
Select one of these:
1. Rock
2. Paper
3. Scissors
""")

def validation(a, b):
	global computer_points
	global user_points
	if a==1 and b==2:
		# print("Computer Wins")
		computer_points += 1
		user_points += 0
		return (computer_points, user_points)

	elif a==1 and b==3:
		# print("You Win")
		user_points += 1
		computer_points += 0
		return (computer_points, user_points)

	elif a==3 and b==1:
		computer_points += 1
		user_points += 0
		return (computer_points, user_points)

	elif a==2 and b==1:
		# print("You Win")
		user_points += 1
		computer_points += 0
		return (computer_points, user_points)

	elif a==3 and b==2:
		# print("You Win")
		user_points += 1
		computer_points += 0
		return (computer_points, user_points)

	elif a==2 and b==3:
		# print("Computer Wins")
		computer_points += 1
		user_points += 0
		return (computer_points, user_points)

	elif a==1 and b==1:
		# print("No One Wins")
		computer_points += 0
		user_points += 0
		return (computer_points, user_points)

	elif a==2 and b==2:
		# print("No One Wins")
		computer_points += 0
		user_points += 0
		return (computer_points, user_points)

	elif a==3 and b==3:
		# print("No One Wins")
		computer_points += 0
		user_points += 0
		return (computer_points, user_points)

	else:
		# print("No One Wins")
		computer_points += 0
		user_points += 0
		return (computer_points, user_points)



def art_rock(user):
	print()
	print(f"""{user}
	    _______
	---'   ____)
	      (_____)
	      (_____)
	      (____)
	---.__(___)""")
	
def art_paper(user):
	print()
	print(f"""{user}
	    _______
	---'    ____)____
	           ______)
	          _______)
	         _______)
	---.__________)""")
	
def art_scissors(user):
	print()
	print(f"""{user}
	    _______
	---'   ____)____
	          ______)
	       __________)
	      (____)
	---.__(___)""")
	


chances = True
while chances:
	try:
		choice_user = int(input("Enter Choice :"))
		print()
		computer = random.randint(1,3)
		if (choice_user == 1) and (computer == 1):
			art_rock("You Selected")
			art_rock("Computer Selected")
			(x, y) = validation(choice_user,computer)
			print(f"Your Points is {y} and Computer Points is {x}")

		elif (choice_user == 2) and (computer == 2):
			art_paper("You Selected")
			art_paper("Computer Selected")
			(x, y) = validation(choice_user,computer)
			print(f"Your Points is {y} and Computer Points is {x}")

		elif (choice_user == 3) and (computer == 3):
			art_scissors("You Selected")
			art_scissors("Computer Selected")
			(x, y) = validation(choice_user,computer)
			print(f"Your Points is {y} and Computer Points is {x}")

		elif (choice_user == 1) and (computer == 2):
			art_rock("You Selected")
			art_paper("Computer Selected")
			(x, y) = validation(choice_user,computer)
			print(f"Your Points is {y} and Computer Points is {x}")

		elif (choice_user == 1) and (computer == 3):
			art_rock("You Selected")
			art_scissors("Computer Selected")
			(x, y) = validation(choice_user,computer)
			print(f"Your Points is {y} and Computer Points is {x}")

		elif (choice_user == 2) and (computer == 1):
			art_paper("You Selected")
			art_rock("Computer Selected")
			(x, y) = validation(choice_user,computer)
			print(f"Your Points is {y} and Computer Points is {x}")

		elif (choice_user == 2) and (computer == 3):
			art_paper("You Selected")
			art_scissors("Computer Selected")
			(x, y) = validation(choice_user,computer)
			print(f"Your Points is {y} and Computer Points is {x}")

		elif (choice_user == 3) and (computer == 1):
			art_scissors("You Selected")
			art_rock("Computer Selected")
			(x, y) = validation(choice_user,computer)
			print(f"Your Points is {y} and Computer Points is {x}")

		elif (choice_user == 3) and (computer == 2):
			art_scissors("You Selected")
			art_paper("Computer Selected")
			(x, y) = validation(choice_user,computer)
			print(f"Your Points is {y} and Computer Points is {x}")

		else:
			print("Please Enter Between 1 to 3.")
	except ValueError:
		print("Please Enter Number. 1 to 3")
	if user_points==3:
		print()
		print("You have Win the game.")
		chances = False
	elif computer_points==3:
		print()
		print("Computer have Win the game.")
		chances = False
	else:
		pass

