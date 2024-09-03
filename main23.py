import random

def choose_animal():
    animals = ['lion', 'elephant', 'giraffe', 'zebra', 'tiger']
    return random.choice(animals)

def animal_description(animal):
    descriptions = {
        'lion': 'This animal is known as the king of the jungle. It has a majestic mane and is a powerful predator.',
        'elephant': 'The largest land animal, known for its long trunk and large ears. It is intelligent and social.',
        'giraffe': 'With its long neck and distinctive spotted coat, this animal is the tallest land mammal.',
        'zebra': 'A black and white striped animal native to Africa. It is known for its distinctive coat pattern.',
        'tiger': 'This big cat has orange fur with black stripes. It is a powerful and stealthy predator.'
    }
    return descriptions.get(animal, 'No description available.')

def play_game():
    print("Welcome to the Animal Guessing Game!")
    print("I will describe an animal, and you have to guess which one it is.")

    chosen_animal = choose_animal()
    animal_desc = animal_description(chosen_animal)

    print("\n" + animal_desc)

    player_guess = input("\nYour guess: ").lower()

    if player_guess == chosen_animal:
        print("Congratulations! You guessed it right. It's a", chosen_animal.capitalize() + "!")
    else:
        print("Sorry, your guess is incorrect. The correct answer is", chosen_animal.capitalize() + ".")

if __name__ == "__main__":
    play_game()