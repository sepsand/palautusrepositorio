from statistics import Statistics
from player_reader import PlayerReader
# from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan
from query_builder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # matcher = And(
    #     HasAtLeast(5, "goals"),
    #     HasAtLeast(20, "assists"),
    #     PlaysIn("PHI")
    # )

    # matcher = And(
    #     Not(HasAtLeast(2, "goals")),
    #     PlaysIn("NYR")
    # )

    query = QueryBuilder()
    matcher = (
      query
      .playsIn("NYR")
      .hasAtLeast(10, "goals")
      .hasFewerThan(20, "goals")
      .build()
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
