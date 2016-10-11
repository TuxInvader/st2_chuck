#! /usr/bin/python

import requests
import sys
from st2actions.runners.pythonrunner import Action

class getChuck(Action):

    def run(self):

      response = requests.get("http://api.icndb.com/jokes/random")
      if response.status_code == 200:
        joke = response.json()
        if joke["type"] == "success":
          answer = str(joke["value"]["joke"])
        else:
          answer = "StackStorm doesn't orchestrate Chuck, Chuck orchestrates StackStorm"

        return answer

