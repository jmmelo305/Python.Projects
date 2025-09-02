def pet_func (pet_response):
    """
    This function decides the type of pet the user / player wants and then what kind of breed or species from the type of 
    pet chosen.
    Ex: Dog, Golden retriever
    The argument given to the function is the response to the question 'Do you want a pet?'. if the argument comes out with
    a response that contains the letter 'y' the function itself will run. If the letter contains anything else the function
    will pass and no pet will be chosen
    The return value is 'reply' which states the breed or species of the pet chosen by the user and then is saved as a 
    global variable so it can referenced through later on in the game.
    """
    pet_response = pet_response.lower()
    if "y" in pet_response:
        pet_type_list = ["Dog","Cat","Bird"]
        print("List of types of pets: ", pet_type_list)
        for i in range (3):
            pet_type = input("Choose the type of pet you'd like to have: ")
            pet_type = pet_type.capitalize()
            print("Loading...")
            time.sleep(2)
            if pet_type in pet_type_list:
                pet_type_index = pet_type_list.index(pet_type)
                print("You have chosen the pet type: ", pet_type_list[pet_type_index] + "!")
                if pet_type == pet_type_list[0]:
                    dog_breed_list = ["Havanese","German Shepard","Golden Retriever","Pug"]
                    print("List of dog breeds: ",dog_breed_list)
                    for i in range (3):
                        dog_breed = input("Choose the dog breed you'd like to have: ")
                        dog_breed = dog_breed.title()
                        if dog_breed in dog_breed_list:
                            dog_breed_index = dog_breed_list.index(dog_breed)
                            reply = dog_breed_list[dog_breed_index]
                            print("You have chosen the breed: ", reply)
                            break
                        else:
                            print("Check for mispell or choose another breed from the list")
                if pet_type == pet_type_list[1]:
                    cat_breed_list = ["Siamese","Sphynx","Ragdoll","Persian"]
                    print("List of cat breeds: ", cat_breed_list)
                    for i in range(3):
                        cat_breed = input("Choose the cat breed you'd like to have: ")
                        cat_breed = cat_breed.capitalize()
                        if cat_breed in cat_breed_list:
                            cat_breed_index = cat_breed_list.index(cat_breed)
                            reply = cat_breed_list[cat_breed_index]
                            print("You have chosen the breed: ",reply)
                            break
                        else:
                            print("Check for mispell or choose another breed from the list")
                            
                if pet_type == pet_type_list[2]:
                    bird_type_list = ["Cockatiel","Lovebird","Parrot","Macaw"]
                    print("List of bird types: ", bird_type_list)
                    for i in range (3):
                        bird_type = input("Choose the type of bird you'd like to have: ")
                        bird_type = bird_type.capitalize()
                        if bird_type in bird_type_list:
                            bird_type_index = bird_type_list.index(bird_type)
                            reply = bird_type_list[bird_type_index]
                            print ("You have chosen the bird type: ",reply)
                            break
                        else:
                            print("Check for mispell or choose another type of bird within the list")
                break
            else:
                print("Check for mispell or choose another type of pet within the list")
    elif "no" in pet_response: 
        reply = "None"
    return (reply)




def event_years10 (ind):
    """
    The purpose of this function is to randomly decide an event that the user will have to go through at age 10.
    The argument given is the randomly generated index that will pull out the random event out of a dictionary provided.
    The return value prints out "x" and and that output is then saved into a global variable called "e" so that it can be
    referenced later throughout the program.
    """
    
    if "y" in pet_response:
        event = events_10[ind]
        if ind == 1:
            x = (events_10[1])
        elif ind == 2:
            x = (events_10[2])
        elif ind == 3:
            print(events_10[3])
            x = ("Your parents are furious at you and have grounded you until college!")
        elif ind == 4:
            print(events_10[4])
            new_friend_ques = input("Do you want to be their new friend?: ")
            new_friend_ques = new_friend_ques.lower()
            if "y" in new_friend_ques:
                x = "You are now friends with "+rand_name+"!"
                friend_list.append(rand_name)
            elif "n" in new_friend_ques:
                x = "You said no to the friend invite."
    elif "n" in pet_response:
        event = events_11[ind]
        if ind == 1:
            x = (events_11[1])
        if ind == 2:
            print(events_11[2])
            x = ("Your parents are furious at you and have grounded you till college!")
        if ind == 3:
            print(events_11[3])
            new_friend_ques = input("Do you want to be their new friend?: ")
            new_friend_ques = new_friend_ques.lower()
            if "y" in new_friend_ques:
                x = "You are now friends with "+rand_name+"!"
                friend_list.append(rand_name)
    print(x)
    return 

    
    
    
def hobby_40 (hobby_y_n):
    """
    The purpose of this function is to let the user decided if they want to have a hobby once they reach their 40's
    The argument given is the response of "yes" or "no" that determines if the functions continues the hobby offers or 
    just continues to the next part of the game.
    The return of the function is the result of which hobby the player chose.
    """
    hobby_list = ["Painting","Book Club","Rob Banks"]
    print ("List of hobbies are",hobby_list)
    if "y" in hobby_y_n:
        for i in range (3):
            hobby_choice = input ("Enter the hobby you would like to begin: ")
            hobby_choice = hobby_choice.title()
            print("Loading...")
            time.sleep(2)
            if hobby_choice in hobby_list:
                x = hobby_list.index(hobby_choice)
                if hobby_list[x] == hobby_list[0]:
                    y = "You have chosen "+hobby_list[0]
                    happiness + 10
                    karma + 5
                    break
                if hobby_list[x] == hobby_list[1]:
                    y = "You have chosen "+hobby_list[1]
                    happiness + 5
                    karma + 10
                    break
                if hobby_list[x] == hobby_list[2]:
                    y = "You have chosen "+hobby_list[2]
                    happiness + 10
                    karma - 10
                    break
            else:
                print("Enter a valid hobby from the list provided.")
    elif "n" in hobby_y_n:
        y = "No hobby"
    return (print(y))
import random
import time

#This is the code for the password system of the game

for i in range(3):
    password = input ("Enter the password to unlock the game: ")
    password = str(password)
    password = password.lower()
    print("Loading...")
    time.sleep(1)
    if password == "ab04cd08":
        print ('Welcome to "5 Decades Game"!')
        time.sleep(1)
        print ("")
        
        
        
        #PERSONAL AND FAMILY INFORMATION
        friend_list = []
        global age, karma, happiness
        age = 0
        karma = 0
        happiness = 0
        kid_list = []
        gender_pref = input("Enter whether you like Women or Men: ")
        gender_pref = gender_pref.lower()
        print("You are",age,"years old!")
        name = input("You have just been born, what will your name be?: ")
        print("")
        mothers_name = str(input("Enter your mother's name, or whatever name you want her to have!: "))
        mothers_name = mothers_name.capitalize()
        print("")
        fathers_name = str(input("Enter your father's name, or whatever name you want him to have!: "))
        fathers_name = fathers_name.capitalize()
        print("")
        pet_response = str(input("Do you want a pet?: "))
        pet_answer = pet_func(pet_response)
        print("")
        print("")
            
        
        
        #The questions for the first 10 years
        time.sleep(2)
        age += 10
        print ("You are now 10 years old!")
        print("")
        print("")
        elementary_school = input("You have begun school!, Enter your Elementary School's name!: ")
        elementary_school = elementary_school.title()
        rand_name_ind = random.randint(1,3)
        rand_name_list = ["Adam","Kayla","Jackson","Ashley"]
        rand_name = rand_name_list[rand_name_ind]
        events_10 = {1:"Your parents have divorced each other!",
                        2:"Your "+pet_answer+" has ran away!",
                        3:'You "accidentally" burned your house down!',
                        4:rand_name+" wants to be your friend!"}
        events_11 = {1:"Your parents have divorced each other!",
                    2:'You "accidentally" burned your house down!',
                    3: rand_name+" wants to be your friend!",
                    4: "empty"}
        if "y" in pet_response:
            event_ind = random.randint (1,4)
        elif "n" in pet_response:
            event_ind = random.randint (1,3) 
        e = event_years10(event_ind)
        if event_ind == 1:
            happiness -= 25
        if event_ind == 2:
            happiness -= 10
        if events_10[event_ind] == 'You "accidentally" burned your house down!':
            happiness -= 5
            karma -= 3
        if event_ind == 4 or events_11[event_ind] == rand_name+" wants to be your friend!":
            happiness += 5
        
        print("")
        print("")
       
    
        #The questions for the 20s.
        time.sleep(2)
        age +=10
        print("You are now 20 years old!")
        print("")
        print("")
        if "y" in pet_response:
            if event_ind == 3:
                print("You are no longer grounded!")
                happiness += 5
        elif "n" in pet_response:
            if event_ind == 2:
                print("You are no longer grounded!")
                happiness += 5
        if 1 == 1:
            print("You have began college!")
            college_options = ["Duke University","University Of Hawaii At Manoa", "University Of Toronto", "Ucla"]
            print(college_options)
            for i in range (2+1):
                college_answer = input("Choose a college within the list to attend: ")
                college_answer = college_answer.title()
                if college_answer in college_options:
                    print("You are now attending:",college_answer)
                    break
                else:
                    print("Enter a valid college option")
            for i in range(4-1):
                college_behavior = input("Are you going to study hard or party hard?: ")
                college_behavior = college_behavior.title()
                if college_behavior == "Study Hard":
                    print("Good choice!")
                    karma += 5
                    happiness += 2
                    break
                if college_behavior == "Party Hard":
                    print("Okay, Your choice.")
                    karma -= 5
                    happiness += 25
                    break
                else:
                    print('Enter "study hard" or "party hard"')
            
        print("")
        print("A soup kitchen nearby is looking for volunteers during the holiday season...")
        for i in range (7-4):
            volunteer_response = input("Are you going to sign up to volunteer?: ")
            volunteer_response = volunteer_response.lower()
            if "y" in volunteer_response:
                karma += 20
                happiness += 15
                print("You are a good citizen!", end='')
                print(" Thanks to you they're less people starving and freezing to death this holiday season!")
                break
            if "n" in volunteer_response:
                karma-=15
                print("Many people this holiday season were alone, freezing, and, starving in the streets...")
            break
        else:
            print("Please enter a valid response.")
        print("")
        print("")
        
        
        
        #The questions for the 30s.
        time.sleep(2)
        age += 10
        print("You are now 30 years old")
        print("")
        print("")
        if "y" in pet_response and event_ind != 2:
            print("Your",pet_answer,"has sadly passed away...")
        print("You have graduated from",college_answer)
        print("Time to find a partner!")
        if "women" in gender_pref:
            print("This beautiful woman has asked you out on a date!!")
            for i in range (3):
                date_acceptance = input("Do you accept this invitation?: ")
                date_acceptance = date_acceptance.lower()
                if "y" in date_acceptance:
                    print("You are now dating the love of your life!")
                    happiness += 7
                    break
                if "n" in date_acceptance:
                    print("Someday maybe you'll find love...")
                    break
                else:
                    print("Please enter a valid response.")
        elif "men" in gender_pref:
            print("This handsome man has asked you out on a date!!")
            for i in range (3):
                date_acceptance = input("Do you accept this invitation?: ")
                date_acceptance = date_acceptance.lower()
                if "y" in date_acceptance:
                    print("You are now dating the love of your life!")
                    break
                if "n" in date_acceptance:
                    print("Someday maybe you'll find love...")
                    break
                else:
                    print("Please enter a valid response.")
        print("5 years have passed (you're now 35)")
        for i in range(3):
            settle_down = input("Do you want to settle down with your partner? or cheat and leave them for someone else: ")
            settle_down = settle_down.lower()
            if settle_down == "settle":
                karma += 10
                print("Great Choice!")
                kids_answer = input("Would you like to have kids?: ")
                kids_answer = kids_answer.lower()
                if "y" in kids_answer:
                    for i in range (3):
                        num_kids = input("Have 2 or 3 kids?: ")
                        if num_kids == "2":
                            kid1 = input("Enter child 1 name: ")
                            kid1 = kid1.capitalize()
                            kid2 = input("Enter child 2 name: ")
                            kid2 = kid2.capitalize()
                            kid_list.append(kid1)
                            kid_list.append(kid2)
                            break
                        elif num_kids == "3":
                            kid1 = input("Enter child 1 name: ")
                            kid1 = kid1.capitalize()
                            kid2 = input("Enter child 2 name: ")
                            kid2 = kid2.capitalize()
                            kid3 = input("Enter child 3 name: ")
                            kid3 = kid3.capitalize()
                            kid_list.append(kid1)
                            kid_list.append(kid2)
                            kid_list.append(kid3)
                            break
                        else:
                            print("Enter either 2 or 3.")
                break
            if settle_down == "cheat":
                karma -= 10
                happiness -= 10
                print("That's really dumb but okay.")
                break
            else:
                print('Enter "settle" or "cheat".')
        print("")
        print("")
        
                
                
        #The questions for the 40s.
        time.sleep(2)
        age += 10
        print("You are now 40 years old!")
        print("")
        print("")
        if settle_down == "settle":
            if "y" in kids_answer:
                print("Your kids have begun playing sports!")
                coach_team = input ("Would you like to coach their team?: ")
                if "y" in coach_team:
                    happiness += 7
                    karma += 7
                    print("You're a great parent! Your kids soccer team won every game this season due to your help!")
                if "n" in coach_team:
                    happiness -= 3
                    karma -= 3
                    print ("Thats fine, your kids soccer team did not succeed much this season.")
            elif "n" in kids_answer:
                print("Find yourself a hobby!")
                hobby_y_n = input("Would you like to do a hobby?: ")
                h = hobby_40(hobby_y_n)
                
        if settle_down == "cheat":
            print("You feel very lonely and miss your ex")
            happiness -= 10
            print("Find yourself a hobby!")
            hobby_y_n = input("Would you like to do a hobby?: ")
            h = hobby_40(hobby_y_n)
        print("")
        print("")

    
        
        #The questions for the 50s and final years.
        time.sleep(2)
        age += 50 
        print("You are now 50 years old!")
        print("")
        print("")
        if "settle" in settle_down:
            if "y" in kids_answer:
                print("Your kids have grown up!")
                for i in range (3):
                    kids_enjoy = input("Did you enjoy seeing them grow up?: ")
                    kids_enjoy = kids_enjoy.lower()
                    if "y" in kids_enjoy:
                        happiness += 10
                        break
                    elif "n" in kids_enjoy:
                        happiness -= 5
                        break
                    else:
                        print("Enter a valid response.")
            print("You're starting to feel a lot slower and tired more often...")
            time.sleep(2)
            print("You have passed away from old age...")
            print("Your funeral was attended by those close to you.")    
        if "cheat" in settle_down:
            print("You're starting to feel a lot slower and tired more often...")
            time.sleep(2)
            print("You've fallen into a deep depression...")
            time.sleep(2)
            print("Eventually you passed away...")
            time.sleep(2)
            print("Your funeral was attended by those close to you.")
            happiness = 0

        #Scores of Karma and Happiness.
        print("")
        print("")
        print("Karma Score: ",karma)
        print("Happiness Score: ",happiness)
         
        #User gives rating of the game.
        rating = input("Rate the game from 1 to 5, 5 being the best game you've ever played: ")
        while type(rating) == type('str') :
            try:
                rating = int(rating)    
            except ValueError:
                print('Invalid rating. Please try again.')
                rating = input("Rate the game from 1 to 5, 5 being the best game you've ever played: ")
            except: 
                print("An error has occured.")
        #Program ends.       
        print("Thank you for playing the game!")    
        break
    else:
        print("Wrong!")
print("Game Over!")      
