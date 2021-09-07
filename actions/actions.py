# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionHaystack(Action):

    def name(self) -> Text:
        return "call_haystack"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = "http://localhost:8000/query"
        payload = {"query": str(tracker.latest_message["text"])}
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, json=payload).json()

        if response["answers"]:
            answer = response["answers"][0]["answer"]
        else:
            answer = "No Answer Found!"

        dispatcher.utter_message(text=answer)

        return []
