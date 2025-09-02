import random
magic_ball = {1: "It is certain",
              2: "Concentrate and ask again",
              3: "Without a doubt",
              4: "Reply hazy, try again",
              5: "You may rely on it",
              6: "Outlook good",
              7: "Yes",
              8: "Outlook not so good",
              9: "Most likely",
             10: "As I see it, yes.",
             11: "Yes definitely",
             12: "Ask again later",
             13: "Better not tell you now",
             14: "Cannot predict now",
             15: "It is decidedly so",
             16: "Don't count on it",
             17: "My reply is no",
             18: "My sources say no",
             19: "Signs point to yes",
             20: "Very doubtful"}

question_1 = (str(input("Ask a yes or no type of question: ")))
generate_1 = random.randint (1,20)
print (magic_ball[generate_1])

question_2 = (str(input("Ask a second yes or no type of question: ")))
generate_2 = random.randint (1,20)
print (magic_ball[generate_2])

question_3 = (str(input("Ask a third yes or no type of question: ")))
generate_3 = random.randint (1,20)
print (magic_ball[generate_3])
