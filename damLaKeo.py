from random import randint
print("Nhap Dam, La, Keo")
user= input();
user=user.capitalize()
opponent  = randint(0,2)
if opponent  == 0:
	opponent = "Dam"
elif opponent  == 1:
	opponent  ="La"
else:
	opponent ="Keo"
print("---")
print("You choose: " + user)
print("Faker choose: " + opponent )
print("---")
if user == opponent:
	print("Draw")
elif user == "Dam":
	if opponent =="Keo":
		print("You Win")
	else:
		print("You Lose")
elif user == "La":
	if opponent =="Dam":
		print("You Win")
	else:
		print("You Lose")
elif user == "Keo":
	if opponent =="Dam":
		print("You Win")
	else:
		print("You Lose")
else:
	print("Input error")