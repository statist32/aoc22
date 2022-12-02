from pprint import pprint
from dataclasses import dataclass, field
from typing import ClassVar, List


@dataclass()
class Choice():
    choice: str
    value: int = field(init=False)

    def __post_init__(self):
        choice_table = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
        self.value = choice_table[self.choice]


@dataclass()
class Round():
    opponent_choice: Choice
    own_choice: Choice
    task_1: bool = True

    @property
    def score_outcome(self):
        if self.task_1:
            score_outcome_table = {"loss": 0, "draw": 3, "win": 6}
            result = self.opponent_choice.value - self.own_choice.value
            if result == 0:
                return score_outcome_table["draw"]
            elif result == -1 or result == 2:
                return score_outcome_table["win"]
            elif result == 1 or result == -2:
                return score_outcome_table["loss"]
        else:
            score_outcome_table = {"X": 0, "Y": 3, "Z": 6}
            return score_outcome_table[self.own_choice.choice]

    @property
    def score_shape(self):
        if self.task_1:
            return self.own_choice.value
        else:
            if self.own_choice.choice == "X":
                loss_table = {"A": 3, "B": 1, "C": 2}
                return loss_table[self.opponent_choice.choice]
            elif self.own_choice.choice == "Y":
                return self.opponent_choice.value
            elif self.own_choice.choice == "Z":
                win_table = {"A": 2, "B": 3, "C": 1}
                return win_table[self.opponent_choice.choice]

    @property
    def score(self):
        return self.score_outcome + self.score_shape


@dataclass
class StrategyGuide():
    rounds: List[Round] = field(default_factory=list)

    @property
    def total_score(self):
        return sum(round.score for round in self.rounds)

    def add_round(self, round):
        self.rounds.append(round)

    @classmethod
    def create_from_file(cls, filename, task_1=True):
        strategy_guide = cls()
        with open(filename) as file:
            for line in file.readlines():
                opponent_choice, own_choice = line.strip().split(" ")
                round = Round(Choice(opponent_choice),
                              Choice(own_choice), task_1)
                strategy_guide.add_round(round)
        return strategy_guide


def solve(filename="input.txt"):
    strategy_guide = StrategyGuide.create_from_file(
        filename, task_1=False)

    return strategy_guide.total_score


if __name__ == "__main__":
    result = solve()
    pprint(result)
