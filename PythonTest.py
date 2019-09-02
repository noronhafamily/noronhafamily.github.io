def q():
    print ("GAME OVER!")

def main():
    print ("Welcome to the Soccer Quiz!")
    print ("Some names may be first and last names ")
    q1 = input("What player as of 2019 plays with Messi and Ronaldo? : ")
    if q1 == "Paulo Dybala":
        print ("yes")
        q2 = input("What country does Van Dijk play for? :  ")
    else:
        q()
    if q2 == "Netherlands":
        print ("yes")
    else:
        q()
 

if __name__ == "__main__":
    main()