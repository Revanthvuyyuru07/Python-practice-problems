print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stands for? ")
if answer == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stands for? ")
if answer == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does ROM stands for? ")
if answer == "read only memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stands for? ")
if answer == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")