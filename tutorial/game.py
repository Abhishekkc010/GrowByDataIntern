print('Welcome to the QUiizzzzess Game')

print('Do you want to start the Game?')
Start = input ("Yes OR NO " )
if Start.lower() != "yes":
    quit()
else:
    print ("Get ready")


score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect! You Lost")
    quit()
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect! You Lost")
    quit()

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect! You Lost")
    quit()

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
     
    score += 1
else:
    print("Incorrect! You Lost")
    quit()
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")