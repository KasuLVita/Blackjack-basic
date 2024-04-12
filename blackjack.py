import random

player_deck = []
computer_deck = []
sign = ''

while True:
    def check_who_won(p_score, c_score):
        if p_score > 21 and c_score < 21:
            return f'Computer wins! Player busted. Computer deck: {computer_deck}, Score: {c_score}'
        elif p_score < 21 and c_score > 21:
            return f'Player wins! Computer busted. Player deck: {player_deck}, Score: {p_score}' 
        elif p_score >= 21 or c_score >= 21 or len(player_deck) == 3 or len(computer_deck) == 3:
            if p_score == 21 and c_score == 21:
                return "It's a draw! Both players got a blackjack!"
            elif p_score == 21:
                return f'Player wins with a blackjack! Player deck: {player_deck}, Score: {p_score}'
            elif c_score == 21:
                return f'Computer wins with a blackjack! Computer deck: {computer_deck}, Score: {c_score}'
            elif p_score > c_score:
                return f'Player wins! Player deck: {player_deck}, Score: {p_score} Computer deck: {computer_deck}, Score: {c_score}'
            elif c_score > p_score:
                return f'Computer wins! Computer deck: {computer_deck}, Score: {c_score} Player deck: {player_deck}, Score: {p_score}'
            else:
                return "It's a draw!"
        return None

    # Random card generator
    arr = [10] * 4 + list(range(2, 11))
    p_card = random.choice(arr)
    c_card = random.choice(arr)
    sign = sign + 'X'

    # Program starts here
    player_deck.append(p_card)
    computer_deck.append(c_card)

    # Summing total score from deck 
    p_score = sum(player_deck)
    c_score = sum(computer_deck)

    print(f'Your deck: {player_deck}')

    # Who won?
    winner = check_who_won(p_score, c_score)
    if winner:
        print(winner)
        break

    player_choice = input('Draw another one? Y/N: ')

    if len(player_deck) < 3:
        print("Computer's deck:", end=" ")
        print(f"[{computer_deck[0]}]", end=" ")
        for _ in range(1, len(computer_deck)):
            print("[X]", end=" ")
        print(sign)
    else:
        print("Computer's deck:", end=" ")
        print(f"[{computer_deck[0]}]", end=" ")
        for _ in range(1, len(computer_deck)):
            print("[X]", end=" ")

    if player_choice != 'Y':
        if c_score > p_score:
            print(f'Computer won! {c_score} > {p_score}')
        elif c_score < p_score:
            print(f'Player won! {c_score} < {p_score}')
        else:
            print('Draw!')
        break
