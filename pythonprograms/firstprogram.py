import random

def main():
   
    program2()


def program2():
    
    secret_number = random.randint(1,9)
    turns=3

    while turns>0:
        print("You have ",turns, "turn(s)")
        num = int(input("Guess a number"))
        if num == secret_number:
            print("good job! the number is ",num,",")
            break
        else:
            print("incorrect. guess again")
        turns = turns-1

    if turns==0:
        print("ooops the number is ",secret_number)



if __name__ == "__main__":
    main()

