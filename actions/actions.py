# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import aiohttp
import json
import logging

logger = logging.getLogger(__name__)

class ActionHaystack(Action):

    def name(self) -> Text:
        return "call_haystack"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = "http://localhost:8000/query"
        payload = {
            "query": str(tracker.latest_message["text"]),
            "params":{"filters": {}, "Retriever": {"top_k": 3}, "Reader": {"top_k": 3}, "Query": {"debug": False}}
        }
        headers = {
            'Content-Type': 'application/json'
        }

        logger.debug(f"Calling {url}, ask: {str(tracker.latest_message['text'])}")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=payload) as response:
                    response = await response.json()
        except aiohttp.ClientConnectorError as e:
            logger.error(f"Haystack service not responding: {str(e)}")
            response = {"answers":[{"answer":f"Haystack service not responding: {str(e)}"}]}

        if response["answers"]:
            logger.debug(f"Answers returned by haystack:\n{response}")
            answer = response["answers"][0]["answer"]
            if not answer:
                answer = response["answers"][1]["answer"]
            logger.debug(f"selected answer: {answer}")
        else:
            answer = "No Answer Found!"

        dispatcher.utter_message(text=answer)

        return []
