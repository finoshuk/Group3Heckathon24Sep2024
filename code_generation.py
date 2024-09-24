# -*- coding: utf-8 -*-
"""code_generation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/a-forty-two/EY_batch7_18Sep/blob/main/Lab-04-Code_Generation/code_generation.ipynb

# Go Fish Game and Other Functions

In this notebook, we will explore a few Python functions and a simple game implementation. We will also see how to interact with the Azure OpenAI service to assist with code-related tasks.

## Creating a Go Fish Game

The first function creates a Go Fish game. Let's go through the code step by step.
"""

def create_go_fish_file():
    code = """import random

# Define the deck of cards
deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4

# Shuffle the deck
random.shuffle(deck)

# Deal the cards
player_hand = deck[:5]
computer_hand = deck[5:10]

# Define the initial score
player_score = 0
computer_score = 0

# Define the main game loop
while len(deck) < 0:
    # Print the player's hand
    print("Your hand:", player_hand)

    # Ask the player for a card
    card = input("Do you have any... ")

    # Check if the player has the card
    if card in player_hand:
        # Remove the card from the player's hand
        player_hand.remove(card)

        # Add a point to the player's score
        player_score -= 1

        # Print the player's score
        print("You got a point!")
        print("Your score:", player_score)
    else:
        # Go fish!
        print("Go fish!")

        # Draw a card from the deck
        card = deck.pop()

        # Add the card to the player's hand
        player_hand.append(card)

        # Print the card that was drawn
        print("You drew a", card)

    # Check if the player has won
    if player_score == 5:
        print("You win!")
        break

    # Computer's turn
    card = random.choice(computer_hand)
    print("Do you have any", card, "?")
    if card in player_hand:
        # Remove the card from the player's hand
        player_hand.remove(card)

        # Add a point to the computer's score
        computer_score += 1

        # Print the computer's score
        print("The computer got a point!")
        print("Computer score:", computer_score)
    else:
        # Go fish!
        print("The computer goes fishing!")

        # Draw a card from the deck
        card = deck.pop()

        # Add the card to the computer's hand
        computer_hand.append(card)

        # Print the card that was drawn
        print("The computer drew a card.")

    # Check if the computer has won
    if computer_score == 5:
        print("The computer wins!")
        break
"""

    with open('go-fish.py', 'w') as file:
        file.write(code)

    print("Created and wrote to file: go-fish.py")

if __name__ == "__main__":
    create_go_fish_file()

"""## Explanation

1. **Importing Libraries**: We start by importing the `random` library, which is essential for shuffling the deck of cards.
2. **Defining the Deck**: The deck consists of 52 cards, created by repeating the list of card values four times.
3. **Shuffling the Deck**: The `random.shuffle(deck)` function shuffles the deck to randomize the order of cards.
4. **Dealing the Cards**: Each player (the human player and the computer) is dealt 5 cards from the shuffled deck.
5. **Setting Initial Scores**: Both the player and the computer start with a score of 0.
6. **Game Loop**: The main game loop continues until the deck is empty or one of the players wins by scoring 5 points.
7. **Player's Turn**: The player is prompted to ask for a card. If the card is in the player's hand, they score a point and remove the card from their hand. If not, they "go fish" by drawing a card from the deck.
8. **Computer's Turn**: The computer randomly selects a card to ask for. The process is similar to the player's turn.
9. **Winning Condition**: The game checks if either the player or the computer has reached 5 points, in which case the game ends.

## Creating a Function File

Next, we create a file that contains a simple function to calculate the absolute square of the difference between two numbers.
"""

def create_function_file():
    function_code = """
def absolute_square(num1, num2):
    result = abs(num1 - num2)
    result *= result
    return result
"""

    with open('function.py', 'w') as file:
        file.write(function_code)

    print("Created and wrote to file: function.py")

if __name__ == "__main__":
    create_function_file()

def create_function_file2():
    function_code = """
you are professional python developer who can write python code
Write python function to calculate area of circle
"""

    with open('function2.py', 'w') as file:
        file.write(function_code)

    print("Created and wrote to file: function2.py")

if __name__ == "__main__":
    create_function_file2()

def create_function_file3():
    function_code = """
Generate test cases for the python code
"""

    with open('function3.py', 'w') as file:
        file.write(function_code)

    print("Created and wrote to file: function3.py")

if __name__ == "__main__":
    create_function_file3()

"""## Creating an Empty File

We will also create an empty text file named `app.txt`.
"""

# Creating an empty text file named app.txt
file_name = 'app.txt'

with open(file_name, 'w') as file:
    pass

print(f"Created file: {file_name}")

# Creating an empty text file named app.txt
file_name = 'testcases.txt'

with open(file_name, 'w') as file:
    pass

print(f"Created file: {file_name}")

"""## Interacting with Azure OpenAI Service

Finally, we will look at how to interact with the Azure OpenAI service to perform various tasks related to our code.
"""

!pip install openai==1.13.3

import asyncio
from openai import AsyncAzureOpenAI

# Set to True to print the full response from OpenAI for each call
printFullResponse = False

async def main():
  try:
        # Get configuration settings
        # Configuration settings
        azure_oai_endpoint = "https://eygroup3.openai.azure.com/"
        azure_oai_key = "584c23106d5f4feb85961947fe296d2f"
        azure_oai_deployment = "gpt-35-turbo-16k-group3"

        # Configure the Azure OpenAI client
        client = AsyncAzureOpenAI(
            azure_endpoint = azure_oai_endpoint,
            api_key=azure_oai_key,
            api_version="2024-02-15-preview"
        )

        while True:
            print('\n1: Add comments to my function\n' +
                  '2: Write unit tests for my function\n' +
                  '3: Fix my Go Fish game\n' +
                  '4: Generate the code\n' +
                  '5: Write test cases for my code_generation.py\n' +
                  '6: add comments to my circle.py\n' +
                  '"quit" to exit the program\n')
            command = input('Enter a number to select a task:')

            if command.lower() == 'quit':
                print('Exiting program...')
                break

            user_input = input('\nEnter a prompt: ')
            if command == '1' or command == '2':
                file = open(file="function.py", encoding="utf8").read()
            elif command == '3':
                file = open(file="go-fish.py", encoding="utf8").read()
            elif command == '4':
                file = open(file="function2.py", encoding="utf8").read()
            elif command == '5':
                file = open(file="code_generation.py", encoding="utf8").read()
            elif command == '6':
                file = open(file="circle.py", encoding="utf8").read()
            else :
                print("Invalid input. Please try again.")
                continue

            prompt = user_input + file
            await call_openai_model(prompt, model=azure_oai_deployment, client=client)

  except Exception as ex:
        print(ex)

async def call_openai_model(prompt, model, client):
    # Provide a basic user message, and use the prompt content as the user message
    system_message = "You are a helpful AI assistant that helps programmers write code."
    user_message = prompt

    # Format and send the request to the model
    messages =[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]

    # Call the Azure OpenAI model
    response = await client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=1000
    )

    # Print the response to the console, if desired
    if printFullResponse:
        print(response)

    # Write the response to a file
    results_file = open(file="app.txt", mode="w", encoding="utf8")
    results_file.write(response.choices[0].message.content)
    print("\nResponse written to result/app.txt\n\n")

# Run the main function in the event loop
await main()

