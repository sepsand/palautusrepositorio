from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or
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

    # matcher2 = And(
    #     Not(HasAtLeast(2, "goals")),
    #     PlaysIn("NYR")
    # )

    # matcher1 = And(
    #         PlaysIn("PHI"),
    #         HasAtLeast(10, "assists"),
    #         HasFewerThan(5, "goals")
    #     )

    # matcher2 = And(PlaysIn("EDM"),
    #                HasAtLeast(50, "points"),
    #                )


    # matcher3 = Or(matcher1, matcher2)
    # for player2 in stats.matches(matcher3):
    #     print(player2)


    

    query = QueryBuilder()
    # matcher = (
    #   query
    #   .playsIn("NYR")
    #   .hasAtLeast(10, "goals")
    #   .hasFewerThan(20, "goals")
    #   .build()
    # )

    m1 = (
    query
        .playsIn("PHI")
        .hasAtLeast(10, "assists")
        .hasFewerThan(5, "goals")
        .build()
    )

    m2 = (
    query
        .playsIn("EDM")
        .hasAtLeast(50, "points")
        .build()
    )

    matcher = query.oneOf(m1, m2).build()



    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
