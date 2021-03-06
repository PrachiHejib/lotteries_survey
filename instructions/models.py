from otree.api import (
    models,
    # widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    # Currency as c,
    # currency_range,
)


author = 'Prachi Hejib'

doc = "Lotteries_survey"
"Investment decisions modelled as lottery choices"


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer1 = models.IntegerField(
        label="How much would you earn if the number 38 was drawn?"
    )
    answer2 = models.IntegerField(
        label="How much would you earn if the number drawn was between 61 and 100?"
    )
    answer3 = models.IntegerField(
        label="How likely is the number 4 to be drawn?"
    )
    answer4 = models.IntegerField(
        label="How likely is it is that you might earn £10?"
    )
    answer8 = models.IntegerField(
        label="How many rounds will be selected for payment?"
    )
    answer9 = models.IntegerField(
        label="How likely is a round to be selected?"
    )

    def answer1_error_message(self, answer):
        if answer != 10:
            return [
                f"Your earnings in this case would not be £{answer}.",
                f"Look again at the bar."
            ]

    def answer2_error_message(self, answer):
        if answer != 20:
            return (
                f"Your earnings in this case would not be {answer}. "
                f"Look again at the bar."
            )


    def answer3_error_message(self, answer):
        if answer!=1:
            return 'Answer is incorrect, please try again'


    def answer4_error_message(self, answer):
        if answer!=25:
            return 'Answer is incorrect, please try again'


    def answer8_error_message(self, answer):
        if answer!=1:
            return 'Answer is incorrect, please try again'


    def answer9_error_message(self, answer):
        if answer!=4:
            return 'Answer is incorrect, please try again'