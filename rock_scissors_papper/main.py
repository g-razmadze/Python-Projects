def rock_paper_scissors():
    """
    This function takes no input and plays a game of rock-paper-scissors between two players.

    Returns:
        None
    """
    p1 = input("Player 1: rock, paper, or scissors ")
    p2 = input("Player 2: rock, paper, or scissors ")

    if p1 == p2:
        print("Draw")
    elif p1 == "rock" and p2 == "scissors":
        print("p1 wins")
    elif p1 == "paper" and p2 == "rock":
        print("p1 wins")
    elif p1 == "scissors" and p2 == "paper":
        print("p1 wins")
    else:
        print("p2 wins")


def main():
    """Main Function"""
    rock_paper_scissors()


if __name__ == "__main__":
    main()
