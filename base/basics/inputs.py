name = input("What is your name? ")
num = int(input("What is your age? "))

if(name == "criz"):
    print("Hello criz")

else:
    print("Hello " + name)


if(num >= 18):
    print("You are old enough to vote")

    if(num >= 21):
        print("Nice")

    else:
        print("Oh ok !")

else:
    print("You are not old enough to vote")
