import random

questions = [
  "Will I win the lottery?",
  "Is it going to rain today?",
  "Will I get a promotion?",
  "Is my friend going to visit me?",
  "Will I pass my exam?",
  "Is it a good day to travel?",
  "Will I find my lost item?",
  "Is it a good time to invest?",
  "Will I meet someone new?",
  "Is my favorite team going to win?"
]

answers = [
  "Yes - definitely",
  "It is decidedly so",
  "Without a doubt",
  "Reply hazy, try again",
  "Ask again later",
  "Better not tell you now",
  "My sources say no",
  "Outlook not so good",
  "Very doubtful"
]

def get_random_value(input_list):
  start_index = 0
  end_index = len(input_list) - 1
  random_index = random.randint(start_index, end_index)
  random_value = input_list[random_index]
  return random_value

name = "Jio"
question = get_random_value(questions)
answer = get_random_value(answers)

if question == "":
  print("Please provide a valid question")
  exit()

if name == "":
  print(f"Question: {question}")
else:
  print(f"{name} asks: {question}")
print(f"Magic 8-Ball's answer: {answer}")