def TictactoeGrid(value):
    print("\n")
    print("\t      |      |")
    print("\t    {} |  {}   |  {}".format(value[0], value[1], value[2]))
    print('\t______|______|______')
    print("\t      |      |")
    print("\t   {}  |  {}   |  {}".format(value[3], value[4], value[5]))
    print('\t______|______|______')
    print("\t      |      |")
    print("\t  {}   |  {}   |  {}".format(value[6], value[7], value[8]))
    print("\t      |      |")
    print("\n")


def Scoreboard(score_board):
    list_of_the_two_players = list(score_board.keys())
    print("\t   ", list_of_the_two_players[0],
          "\t    ", score_board[list_of_the_two_players[0]])
    print("\t   ", list_of_the_two_players[1],
          "\t    ", score_board[list_of_the_two_players[1]])

    print("\t--------------------------------\n")


def WinValidate(position_player, player_current):
    win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [
        1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for i in win_combinations:
        if all(j in position_player[player_current] for j in i):
            return True
    return False


def TieValidate(position_player):
    if len(position_player['X']) + len(position_player['O']) == 9:
        return True
    return False


def game_single(player_current):
    value = [' ' for i in range(9)]
    position_player = {'X': [], 'O': []}
    while True:
        TictactoeGrid(value)
        try:
            print("The player ", player_current,
                  " turn.  choose your block : ", end="")
            chance = int(input())
        except ValueError:
            print("This is an Invalid Input!!! Please try again!")
            continue

        if chance < 1 or chance > 9:
            print("This is an Invalid Input!!! Please try again!")
            continue

        if value[chance - 1] != ' ':
            print("The position is already filled, try again!")
            continue

        value[chance - 1] = player_current
        position_player[player_current].append(chance)
        if WinValidate(position_player, player_current):
            TictactoeGrid(value)
            print(player_current, " has won the tic tac toe game!")
            print("\n")
            return player_current

        if TieValidate(position_player):
            TictactoeGrid(value)
            print("Game is Tied")
            print("\n")
            return 'D'

        if player_current == 'X':
            player_current = 'O'
        else:
            player_current = 'X'


if __name__ == "__main__":

    print("The First Player's name")
    player_first = input("name: ")
    print("\n")
    print("The Second Player's name")
    player_second = input("name:  ")
    print("\n")

    player_current = player_first
    player_choice = {'X': "", 'O': ""}
    option = ['X', 'O']

    score_board = {player_first: 0, player_second: 0}
    Scoreboard(score_board)

    while True:
        print(player_current)
        print(" press 1 for X")
        print(" press 2 for O")
        print(" press 3 for Exit")

        try:
            the_choice = int(input())
        except ValueError:
            print("This input is Invalid!!! Please Try Again\n")
            continue

        if the_choice == 1:
            player_choice['X'] = player_current
            if player_current == player_first:
                player_choice['O'] = player_second
            else:
                player_choice['O'] = player_first

        elif the_choice == 2:
            player_choice['O'] = player_current
            if player_current == player_first:
                player_choice['X'] = player_second
            else:
                player_choice['X'] = player_first

        elif the_choice == 3:
            Scoreboard(score_board)
            break

        else:
            print("This is an Invalid choice!! try again\n")

        winner = game_single(option[the_choice - 1])

        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

            Scoreboard(score_board)

        if player_current == player_first:
            player_current = player_second
        else:
            player_current = player_first