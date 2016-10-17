#! /usr/bin/python

import requests
import sys
from st2actions.runners.pythonrunner import Action
from HTMLParser import HTMLParser

class getChuck(Action):

    def run(self, name, surname, explicit):

      url = "http://api.icndb.com/jokes/random"
      queryString = {}

      if explicit is False:
        queryString["exclude"] = "explicit"

      if name is not None:
        queryString["firstName"] = name

      if surname is not None:
        queryString["lastName"] = surname

      qs = "?"
      for param in queryString.keys():
        qs += "{}={}&".format(param, queryString[param]) 

      response = requests.get(url + qs[:-1])
      if response.status_code == 200:
        joke = response.json()
        if joke["type"] == "success":
          h = HTMLParser()
          answer = h.unescape(joke["value"]["joke"])
        else:
          answer = "StackStorm doesn't orchestrate Chuck, Chuck orchestrates StackStorm"

        return answer

