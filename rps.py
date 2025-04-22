import os, time, random
from rich.console import Console

console = Console()

choices = ["rock", "paper", "scissors"]

os.system("cls||clear")

while True:
    console.print("Welcome to the Rock, Paper, Scissors game!", end="\n\n", style="bold underline green")
    console.print("You can choose between [bold blue](1)[/bold blue] rock, [bold blue](2)[/bold blue] paper, and [bold blue](3)[/bold blue] scissors.")

    # Get user input
    console.print("Please enter your choice (1, 2, or 3): ", end="", style="bold blue")
    user_choice_numeric = input()

    if user_choice_numeric not in ["1", "2", "3"]:
        os.system("cls||clear")
        console.print("Invalid choice. Please try again.", end="\n\n", style="bold red")
        continue

    user_choice = "rock" if user_choice_numeric == "1" else "paper" if user_choice_numeric == "2" else "scissors" if user_choice_numeric == "3" else None

    console.print()

    # Simulate the other end's decision making process
    with console.status("[bold blue]Deciding...[/bold blue]", spinner_style="blue") as status:
        time.sleep(random.randint(1, 3))

    computer_choice = random.choice(choices)

    # Compare choices
    if user_choice == "rock":
        # Rock
        response = "It's a tie!" if computer_choice == "rock" else "You lose!" if computer_choice == "paper" else "You win!" if computer_choice == "scissors" else "Are you supposed to see this?"
        response_color = "yellow" if computer_choice == "rock" else "red" if computer_choice == "paper" else "green"
        console.print(f"[bold]{response}[/bold]\nYou chose: [bold]{user_choice}[/bold].\nComputer chose: [bold]{computer_choice}[/bold].", end="\n\n", style=response_color)
    elif user_choice == "paper":
        # Paper
        response = "It's a tie!" if computer_choice == "paper" else "You lose!" if computer_choice == "scissors" else "You win!" if computer_choice == "rock" else "Are you supposed to see this?"
        response_color = "yellow" if computer_choice == "paper" else "red" if computer_choice == "scissors" else "green"
        console.print(f"[bold]{response}[/bold]\nYou chose: [bold]{user_choice}[/bold].\nComputer chose: [bold]{computer_choice}[/bold].", end="\n\n", style=response_color)
    elif user_choice == "scissors":
        # Scissors
        response = "It's a tie!" if computer_choice == "scissors" else "You lose!" if computer_choice == "rock" else "You win!" if computer_choice == "paper" else "Are you supposed to see this?"
        response_color = "yellow" if computer_choice == "scissors" else "red" if computer_choice == "rock" else "green"
        console.print(f"[bold]{response}[/bold]\nYou chose: [bold]{user_choice}[/bold].\nComputer chose: [bold]{computer_choice}[/bold].", end="\n\n", style=response_color)
    else:
        # Invalid choice
        os.system("cls||clear")
        console.print("Invalid choice. Please try again.", end="\n\n", style="bold red")
        continue

    time.sleep(2)
    console.print("Would you like to try again? (yes/no): ", end="", style="bold blue")
    play_again = input().lower()

    if play_again == "yes":
        os.system("cls||clear")
    elif play_again == "no":
        break

    continue
