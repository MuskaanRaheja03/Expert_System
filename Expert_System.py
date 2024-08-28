print("1. James Bond Films")
print("2. Super Hero Films")
genre = int(input("Choose the subgenre (1 or 2):"))

# Dr. No was the only movie which doesn't include pre-title credits action sequence.
# Quantum of solace was james bond movie in which there was 1 love encounter and bond actor wa Daniel Craig.
# Skyball was james bond movie in which there was 2 love encounter and bond actor wa Daniel Craig.
# In Die Another Day, bond actor was Pierce Bronsan.
# You only live twice cast Sean Connery and has maximum kills.
# Moonranker cast Rooger Moore.
# Thnderball cast Sean Connery and has more than 100 kills.
# The Spy Who Loved Me also has more than 100 kills and bond actor is Roger Moore.
# The Man With Golden Gun cast Roger Moore and has minimum kills.
# On Her Majesty's Secret Service cast George Lazenby (casted only in one series)

if genre == 1:
    jb1 = input("Does the movie include pre-title credits action sequence? ") 
    if jb1 == "yes" or jb1 == "YES":
        jb5 = input("Was the movie released after 2000?:")
        if jb5 == "yes" or jb5 == "YES":
            jb6 = input("Is the bond actor Daniel Craig?: ")
            if jb6 == "yes" or jb6 == "YES":
                jb7 = input("Is there 1 love encounter in the film?: ")
                if jb7 == "yes" or "YES":
                    print("The movie is Quantum Of Solace")
                else:
                    print("The movie is Skyfall")
            else:
                print("The movie is Die Another Day") 
        else:
            jb2 = input("In this movie, is the total kills greater than 100?")
            if jb2 == "yes" or jb2 == "YES": 
                jb3 = input("Is the bond actor Sean Connery?: ")
                if jb3 == "yes" or jb3 == "YES":
                    jb4 = input("Does this movie has maximum deaths?: ")
                    if jb4 == "yes" or jb4 == "YES":
                        print("The movie is You Only Live Twice.")
                    else: 
                        print("The movie is Thunderball.")
                else:
                    print("The movie is The Spy Who Loved Me")  
            else:
                jb9 = input("Does the movie has least number of bond kills?: ") 
                if jb9 == "yes" or jb9 == "YES": 
                    print("The movie is On Her The Man With Golden Gun") 
                else:
                    jb10 = input("Has the actor played only in one series?: ") 
                    if jb10 == "yes" or jb10 == "YES": 
                        print("The movie is On Her Majesty's Secret Service") 
                    else:
                        print("The movie is Moonranker")
    else:
        print("The movie is Dr. No")

# Iron Man was released before 2011 and has 3 series.
# Iron Man was also released before 2011.
# The Incredible Hulk was released befoe 2011 and it only has 1 serie.
# Howard The Duck is the only sperhero movie which doesn't have VFX.
# Captian America: The First Avenger was the first movie with avengers.
# In Captain America: Civil War, avengers fight.
# The movie deadpool was released after 2011 and is not an Avenger.

if genre == 2:
    sh1 = input("Was the movie released before 2011?: ")
    if sh1 == "yes" or sh1 =="YES":
        sh2 = input("Do movie have  more than 1 series?: ")
        if sh2 == "yes" or sh2 == "YES":
            sh3 = input("Is it a first movie in the series?: ")
            if sh3 == "yes" or sh3 == "YES":
                print("The movie is Iron Man")
            else:
                print("The movie is Iron Man 2")
        else:
            print("The movie name is The Incredible Hulk")
    else:
        sh4 =input("Do the movie has 3 series?: ")
        if sh4 == "yes" or "YES":
            print("Iron Man 3")
        else:
            sh5 = input("Does the movie has VFX?: ")
            if sh5 == "yes" or sh5 == "YES":
                sh6 = input("Are Avengers there in the movie?: ")
                if sh6 == "yes" or "YES":
                    sh7 = input("Are they fightinging?: ")
                    if sh7 == "yes" or sh7 == "YES":
                        print("The movie is Captain America: Civil War")
                    else:
                        print("The movie is Captian America: The First Avenger")
                else:
                    print("The movie is Deadpool")
            else:
                print("The Movie is Howard The Duck")
                
