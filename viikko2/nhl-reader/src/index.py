import requests
from player import Player


def sortByPoints(player):
    return player.goals + player.assists

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == "FIN":
            players.append(player)

    print("Players from FIN\n")

    players = sorted( players,
                      reverse=True,
                      key=sortByPoints)

    for player in players:
        print(player)

if __name__ == "__main__":
    main()