from iqoptionapi.stable_api import IQ_Option
import logging
import time
import pandas as pd

# Créer une instance de l'API d'IQ Option


class trading_core:
    "class contient permet de faire la connection avec l'api iq_option et faire les confuguration de trading"

    def __init__(
        self,
        goal="EURUSD",
        Money=10,
        ACTIVES="EURUSD",
        ACTION="call",
        expirations_mode=1,
    ):
        self.goal = goal
        self.Money = 10
        self.ACTIVES = "EURUSD"
        self.ACTION = "call"  # or "put"
        self.expirations_mode = 1

        Iq = IQ_Option("elouafimed2@gmail.com", "2002****Med")
        Iq.connect()
        check, id = Iq.buy(Money, ACTIVES, ACTION, expirations_mode)
        if check:
            print("!buy!")
        else:
            print("buy fail")
