# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_leave_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        api_address='https://run.mocky.io/v3/a9a51f3e-cb03-4c16-ac0a-afb46f6a50e3'

        json_data = requests.get(api_address).json() 
        temp1=""

        for person in json_data:
            temp = (f"{json_data[person]['Name']} has {json_data[person]['Leaves']}.")
            temp1 = temp1+temp 
        print(temp1)
        dispatcher.utter_message(text=temp1)
        return []
