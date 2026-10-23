#Create a program capable of displaying questions to the user like KBC
#use list datatype to store the questions and their corect answers.
#display the final amount the person taking home awway.

#lets start KBC
Q = ["Q.Who is the first person to score double hundred in ODI?",
     "Q.Who is the highest run scorer in T20i?",
     "Q.Which IPL team Till date not have a single ipl trophy?",
     "Q.Who is the highest wocket taker in the test interationals?",
     "Q.What is the highest score of Virat Kohli in the test?"]
Options = ["1) Virender Sehwag 2) Chris Gayle 3) Sachin Tendulkar   4) Rohit Sharma",
           "1) Rohit Sharma 2) Virat Kohli 3) Babar Azam  4) Jos Buttler",
           "1) Rajasthan Royals 2) Sunrisers Hyderabad 3) Delhi Capitals 4) Kolkata Knight Riders",
           "1) Shane Warne 2) James Anderson 3) Muttiah Muralitharan 4) Anil Kumble",
           "1)183 2)254*  3)200 4)235"]
Right = [3,3,3,3,2]


for i in range(5):
    print("The question on your screen :")
    print(Q[i])
    print("\nOptions are\n",Options[i])
    x = int(input("Enter the correct answer:"))
    if(x==Right[i]):
        print("You won the:",(i+1)*1000,"Rs")
        print("If you want to take this money out or you want to play next:")
        c = input("y/n: ")
        if(c == "y"):
            print("\nthank you!")
        else:
            print("Thank you bhaisahab for you time:")
            break
    else:
        print("sorry bhaisahab yoour out!")
        break