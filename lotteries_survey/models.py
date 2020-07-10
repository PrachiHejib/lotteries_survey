import random
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Prachi Hejib'

doc = "Lotteries_survey"
"Investment decisions modelled as lottery choices"


class Constants(BaseConstants):
    name_in_url = 'lotteries_survey'
    players_per_group = None
    num_rounds = 2
    payoff = currency_range(c(0), c(20), c(10))


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    @property
    def lottery_image_A(self):
        return f"lotteries_survey/lottery_p{self.round_number}.jpg"

    @property
    def lottery_image_B(self):
        return f"lotteries_survey/lottery_q{self.round_number}.jpg"

class Player(BasePlayer):
    lotterychoice = models.StringField()

    @property
    def dieroll(self):
        return random.randint(1,100)

    @property
    def payoff(self):
        if self.lotterychoice == 'A' and self.dieroll in range(1,11):
            return c(0)
        else:
            return c(20)




