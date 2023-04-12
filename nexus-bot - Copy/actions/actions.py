# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import requests

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_leave_info"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

#         api_address='https://run.mocky.io/v3/a9a51f3e-cb03-4c16-ac0a-afb46f6a50e3'

#         json_data = requests.get(api_address).json() 
#         temp1=""

#         for person in json_data:
#             temp = (f"{json_data[person]['Name']} has {json_data[person]['Leaves']}.")
#             temp1 = temp1+temp 
#         print(temp1)
#         dispatcher.utter_message(text=temp1)
#         return []



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from datetime import datetime
from word2number import w2n

global AvailableLeaves
AvailableLeaves = 0

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_leave_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        url = "https://nexusuat.tvsnext.io:1180/api/Leaves/GetAvailableLeaveDetailsByEmployee?employeeID="


        headers = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkVGRjc4NDM0MUMzQTA1REFENEVBODYyNERBRjgzNTEzIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODAyNjUxNzEsImV4cCI6MTY4NDE1MzE3MSwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiTmV4dXNBUEkiLCJjbGllbnRfaWQiOiJuZXh1c191aSIsImp0aSI6IjcwRTZBNDFCMzhFNTIyRjgwNkU3QzlGRTlBMkQxM0YxIiwiaWF0IjoxNjgwMjY1MTcxLCJzY29wZSI6WyJOZXh1c0FQSSJdfQ.pqOG4pU7QqWDZWw2Dz874gMyMw-O0xyrnfSf2L0yjCqv4vJYTb2N9URcrzw75wv6RVW7zsvRabRRiKz8WhKxgHCDWORZZyY_F5pNfRy9kPlcskPBqo3HCezUrWbt1EcgeCRKwT6D1F6tWudKXj9pd8iBj6VuhZVv8XeFiKhF0pn3OYpHofV_IsIRJuYzK895Ckn0w3RHLRR4dFoiHbz_kP1q--FNI7hvexDduzl2BicTu40m5rliZ1kfPyy4_lm9lyHl8b1yn4BMPIccLwjEUrAMzHlTonWUXeV4wG0i3mjWrr1eONfPkyk1ziNtqqIHRBc-r1ZOafJncU-BjSbwtw'
        }

        resp = requests.get(url+"1", headers=headers).json()
        global AvailableLeaves

        for data in resp['data']:
            if data['leaveType'] == 'Old Earned Leave':
                AvailableLeaves = data['availableLeaves']
                print(f"you have {data['availableLeaves']} Avilable Leaves from {data['leaveType']}")
                dispatcher.utter_message(text=f"you have {data['availableLeaves']} Avilable Leaves from {data['leaveType']}")
                dispatcher.utter_message(text="Would you like to apply?")
        return []

class ActionWelcome(Action):

    def name(self) -> Text:
        return "action_welcome"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print(f"date value {tracker.get_slot('dateValue')}")
        print(tracker.get_slot("monthValue"))
        return []

# class ActionWelcome(Action):

#     def name(self) -> Text:
#         return "action_welcome"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         print("Hello world")

      
#         fromdatevalue = tracker.get_slot("fromdate")
#         todatevalue = tracker.get_slot("todate")

#         try:
#             fromdate = datetime.strptime(fromdatevalue, '%d/%m/%y')
#             todate = datetime.strptime(todatevalue, '%d/%m/%y')
#         except ValueError:
#             print("Invalid date format!")
#             dispatcher.utter_message(text="Invalid date format!")
#             return[]
#         else:
#             fromdatevalue = fromdate.strftime('%Y-%m-%d')
#             todatevalue = todate.strftime('%Y-%m-%d')

#         print(fromdatevalue)
#         print(todatevalue)
#         print("---------------------------")
#         print(tracker.get_slot("fromdate"))
#         print(tracker.get_slot("todate"))

#         # fromdatevalue = fromdatevalue #'2023-04-05'
#         # todatevalue = todatevalue #'2023-04-05'
#         url = "https://nexusuat.tvsnext.io:1180/api/Leaves/InsertorUpdateApplyLeave"


#         headers = {
#             'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkVGRjc4NDM0MUMzQTA1REFENEVBODYyNERBRjgzNTEzIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODAyNjUxNzEsImV4cCI6MTY4NDE1MzE3MSwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiTmV4dXNBUEkiLCJjbGllbnRfaWQiOiJuZXh1c191aSIsImp0aSI6IjcwRTZBNDFCMzhFNTIyRjgwNkU3QzlGRTlBMkQxM0YxIiwiaWF0IjoxNjgwMjY1MTcxLCJzY29wZSI6WyJOZXh1c0FQSSJdfQ.pqOG4pU7QqWDZWw2Dz874gMyMw-O0xyrnfSf2L0yjCqv4vJYTb2N9URcrzw75wv6RVW7zsvRabRRiKz8WhKxgHCDWORZZyY_F5pNfRy9kPlcskPBqo3HCezUrWbt1EcgeCRKwT6D1F6tWudKXj9pd8iBj6VuhZVv8XeFiKhF0pn3OYpHofV_IsIRJuYzK895Ckn0w3RHLRR4dFoiHbz_kP1q--FNI7hvexDduzl2BicTu40m5rliZ1kfPyy4_lm9lyHl8b1yn4BMPIccLwjEUrAMzHlTonWUXeV4wG0i3mjWrr1eONfPkyk1ziNtqqIHRBc-r1ZOafJncU-BjSbwtw'
#         }

#         params = {
#         "leaveDetails": {
#             "leaveId": 0,
#             "employeeId": 911,
#             "leaveTypeId": 3,
#             "fromDate": fromdatevalue+"T00:00:00.000Z",
#             "toDate": todatevalue+"T00:00:00.000Z",
#             "noOfDays": 1,
#             "leaveType": "General Leave",
#             "reason": "test",
#             "appliedLeaveDetails": [
#             {
#                 "appliedLeaveDetailsID": 0,
#                 "date": "2023-04-05T00:00:00.000Z",
#                 "isFullDay": True,
#                 "isFirstHalf": False,
#                 "isSecondHalf": False,
#                 "leaveId": 0,
#                 "compensatoryOffId": 0,
#                 "createdBy": 911
#             }
#             ],
#             "createdBy": 911,
#             "createdOn": "2023-04-04T06:41:49.405Z",
#             "modifiedBy": 911,
#             "modifiedOn": "NULL",
#             "isActive": True,
#             "grantEffectiveFromDate": "null",
#             "status": "Pending",
#             "isGrantLeave": False
#         },
#         "listOfDocuments": [],
#         "shiftId": 1
#         }
#         print(f"requested leave {tracker.get_slot('daycount')}")
#         RequestedLeaves = w2n.word_to_num(tracker.get_slot("daycount"))
#         print(RequestedLeaves)
#         # RequestedLeaves = tracker.get_slot("daycount")
#         if int(RequestedLeaves) <= AvailableLeaves:
#             resp = requests.post(url, headers=headers,json = params).json()
#             dispatcher.utter_message(text=resp['statusText'])
#             print(resp['statusText'])
#         else:
#             dispatcher.utter_message(text=f"You have {AvailableLeaves} days but requested {RequestedLeaves} days \nTry Again")
#         return []