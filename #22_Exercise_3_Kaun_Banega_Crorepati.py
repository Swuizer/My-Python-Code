print("Welcome to Kon Banega Koror Poti")
print("Start")
price = 0

# Question 1
print("King of Jangle")
print("1. Lion")
print("2. Tiger")
print("3. Fox")
print("4. Wolf")
Qes = int(input("Chose your option ",))
match(Qes):
    case 1:
        print("RIght Answer\nYou Win 1000/-")
        price = price + 1000

        # Question 2
        print("Capital City Of India")
        print("1. West Bengla")
        print("2. Panjab")
        print("3. Pune")
        print("4. Delhi")
        Qes = int(input("Chose your option ",))
        match(Qes):
            case 1:
                print("You enter wrong answer\nGood Bye")
            case 2:
                print("You enter wrong answer\nGood Bye")
            case 3:
                print("You enter wrong answer\nGood Bye")
            case 4:
                print("RIght Answer\nYou Win 5000/-")
                price = price + 5000

                # Question 3
                print("What color is a mirror")
                print("1. Silver")
                print("2. Green")
                print("3. White")
                print("4. None")
                Qes = int(input("Chose your option ",))
                match(Qes):
                    case 1:
                        print("You enter wrong answer\nGood Bye")
                    case 2:
                        print("You enter wrong answer\nGood Bye")
                    case 3:
                        print("RIght Answer\nYou Win 25000/-")
                        price = price + 25000

                        # Question 4
                        print("What is the orange part of an egg called")
                        print("1. Albumen")
                        print("2. Yolk")
                        print("3. Chalaza")
                        print("4. None")
                        Qes = int(input("Chose your option ",))
                        match(Qes):
                            case 1:
                                print("You enter wrong answer\nGood Bye")
                            case 2:
                                print("RIght Answer\nYou Win 50000/-")
                                price = price + 50000
                            case 3:
                                print("You enter wrong answer\nGood Bye")
                            case 4:
                                print("You enter wrong answer\nGood Bye")
                    case 4:
                        print("You enter wrong answer\nGood Bye")
    case 2:
        print("You enter wrong answer\nGood Bye")
    case 3:
        print("You enter wrong answer\nGood Bye")
    case 4:
        print("You enter wrong answer\nGood Bye")
print("Ok, Your Game is over, your total price you win",price)