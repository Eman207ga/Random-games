print ("**** How to Buy BMW???? ****")

while True:
    having_money = input("\nDo you have money?? (yes/no): ").strip().lower()
    if (having_money == "yes"):
        print ("\n#################")
        print ("You got a BMW")
        print ("#################")
    elif (having_money == "no"):
        working = input ("\nDo you working? (yes/no): ").strip().lower()
        if (working == "yes"):
            salary = input ("\nDo you take a salary? (yes/no): ").strip().lower()
            if (salary == "yes"):
                print("\n#################")
                print("You got a BMW")
                print("#################")
            elif (salary == "no"):
                property = input ("\nDo you have property?? (yes/no): ").strip().lower()
                if (property == "yes"):
                    print ("Sell them")
                    print("\n#################")
                    print ("You got a BMW")
                    print("#################")
            else:
                print ("Invalid Choice!!!")
        elif (working == "no"):
            property = input("\nDo you have property?? (yes/no): ").strip().lower()
            if (property == "yes"):
                print("Sell them")
                print("\n#################")
                print("You got a BMW")
                print("#################")
            elif (property == "no"):
                while True:
                    kidney = input ("\nDo you have kidney??? (yes/no): ").strip().lower()
                    if (kidney == "yes"):
                        print ("Sell it")
                        print("\n#################")
                        print("You got a BMW")
                        print("#################")
                    elif (kidney == "no"):
                        print ("\nLiar")
                    else:
                        print("Invalid Choice!!!")
            else:
                print("Invalid Choice!!!")
        else:
            print("Invalid Choice!!!")
    else:
        print("Invalid Choice!!!")




        