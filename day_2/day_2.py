# Read input data
with open("day_2/input.txt", "r") as f:
    lines = f.read().strip().split("\n")


def parse_game(game_line: str) -> list[dict[str, int]]:
    _, game_draws = game_line.split(": ")
    draw_sets = [draw_set.split(", ") for draw_set in game_draws.split("; ")]
    return [
        {
            color_number_pair.split(" ")[1]: int(color_number_pair.split(" ")[0])
            for color_number_pair in draw_set
        }
        for draw_set in draw_sets
    ]


def is_game_possible(game: list[dict[str, int]]) -> bool:
    return all(
        [
            draw_set.get("red", 0) <= 12
            and draw_set.get("green", 0) <= 13
            and draw_set.get("blue", 0) <= 14
            for draw_set in game
        ]
    )


def get_minimum_set(game: list[dict[str, int]]) -> dict[str, int]:
    minimum_set = {"red": 0, "green": 0, "blue": 0}
    for draw_set in game:
        if draw_set.get("red", 0) >= minimum_set["red"]:
            minimum_set["red"] = draw_set.get("red", 0)
        if draw_set.get("green", 0) >= minimum_set["green"]:
            minimum_set["green"] = draw_set.get("green", 0)
        if draw_set.get("blue", 0) >= minimum_set["blue"]:
            minimum_set["blue"] = draw_set.get("blue", 0)
    return minimum_set


games = [parse_game(line) for line in lines]

# Part 1
possible_games: list[int] = []
for i, game in enumerate(games):
    if is_game_possible(game):
        possible_games.append(i+1)    

print(f"Part 1: answer is: {sum(possible_games)}")

# Part 2
minimum_sets = [get_minimum_set(game) for game in games]
powers = [minimum_set.get("red", 0) * minimum_set.get("green", 0) * minimum_set.get("blue", 0) for minimum_set in minimum_sets]

print(f"Part 2: answer is: {sum(powers)}")
