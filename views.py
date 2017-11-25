from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
from django.conf import settings


class Sum(Page):
    form_model = models.Player
    form_fields = ['answer']

    def vars_for_template(self):
        self.player.initialize()

        return {
        }

    def before_next_page(self):
        if self.player.answer == self.player.solution:
            self.player.answer_correct = 1

class Wait(WaitPage):
    pass


page_sequence = [Sum]
