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
from datetime import datetime, timedelta, timezone
from word2number import w2n
import Levenshtein

global AvailableLeaves,leavetype_dict
AvailableLeaves = 0


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_leave_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        url = "https://nexusuat.tvsnext.io:1180/api/Leaves/GetEmployeeLeavesBalanceDetails"


        headers = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkVGRjc4NDM0MUMzQTA1REFENEVBODYyNERBRjgzNTEzIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODAyNjUxNzEsImV4cCI6MTY4NDE1MzE3MSwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiTmV4dXNBUEkiLCJjbGllbnRfaWQiOiJuZXh1c191aSIsImp0aSI6IjcwRTZBNDFCMzhFNTIyRjgwNkU3QzlGRTlBMkQxM0YxIiwiaWF0IjoxNjgwMjY1MTcxLCJzY29wZSI6WyJOZXh1c0FQSSJdfQ.pqOG4pU7QqWDZWw2Dz874gMyMw-O0xyrnfSf2L0yjCqv4vJYTb2N9URcrzw75wv6RVW7zsvRabRRiKz8WhKxgHCDWORZZyY_F5pNfRy9kPlcskPBqo3HCezUrWbt1EcgeCRKwT6D1F6tWudKXj9pd8iBj6VuhZVv8XeFiKhF0pn3OYpHofV_IsIRJuYzK895Ckn0w3RHLRR4dFoiHbz_kP1q--FNI7hvexDduzl2BicTu40m5rliZ1kfPyy4_lm9lyHl8b1yn4BMPIccLwjEUrAMzHlTonWUXeV4wG0i3mjWrr1eONfPkyk1ziNtqqIHRBc-r1ZOafJncU-BjSbwtw'
        }
        
        params = {
            "employeeId": 245,
            "fromDate": "2023-04-01",
            "toDate": "2024-03-31",
            "departmentId": 15,
            "shiftId": 1,
            "LocationId": 1,
            "dateOfJoining": "2021-06-21T00:00:00"
        }

        request_obj = requests.post(url, headers=headers,json = params)
        resp = request_obj.json()
        print(request_obj.status_code)
        global AvailableLeaves,leavetype_dict

        # ------------------
        leavetype_dict = {data['leaveType']: data['displayBalanceLeave'] for data in resp['data']['employeeAvailableLeaveDetails'] if data['displayBalanceLeave'] > 0}


        if len(leavetype_dict) == 1:
            key, value = next(iter(leavetype_dict.items()))
            print(f"{key}: {value}")
            print(f"You have {value} {key} available, would you like to apply now.")
            dispatcher.utter_message(text=f"You have {value} {key} available, would you like to apply now.")
        elif len(leavetype_dict) > 1:
            leave_msg = f"Below are the list of available leaves. Which one would you like to apply?"
            print("Below are the list of available leaves. Which one would you like to apply?")
            for key, value in leavetype_dict.items():
                print(f"{key}: {value}")
                leave_msg = leave_msg + f" \n{key}: {value} "
            dispatcher.utter_message(text=leave_msg)
        else:
            print("You have no leave balance. I am sorry you can't avail a leave now.\n However, please note that your General Leaves are added incrementally overtime. please check back after sometime. Would you like more info regarding this?")
            dispatcher.utter_message(text="You have no leave balance. I am sorry you can't avail a leave now.\n However, please note that your General Leaves are added incrementally overtime. please check back after sometime. Would you like more info regarding this?")
        return []


class ActionWelcome(Action):

    def name(self) -> Text:
        return "action_welcome"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print("------------start-----------------------")
        daycount = tracker.get_slot('daycount')
        if daycount.lower() == "first":
            RequestedLeaves = 0.5
            isFullDay= False
            isFirstHalf= True
            isSecondHalf= False
        elif daycount.lower() == "second":
            RequestedLeaves = 0.5
            isFullDay= False
            isFirstHalf= False
            isSecondHalf= True
        else:
            print(f"Input Days count = {daycount}")
            daycount_str = str(daycount)
            print(daycount_str)
            isFullDay= True
            isFirstHalf= False
            isSecondHalf= False
            
            if daycount_str.isdigit():
                RequestedLeaves = int(daycount_str)
                print("condition true it is integer")
            else:
                RequestedLeaves = w2n.word_to_num(daycount_str)
                print(f"condition false it is string")
                
                
        print("------leave type---------")
        print(f"Leave Type = {tracker.get_slot('LeaveType')}")
        # leave type and its id
        Leavetype_id_dict = {'General Leave': 3, 'Leave Without Pay': 4,
         'Old Earned Leave' : 2, 'Miscarriage Leave' : 5,'Covid Leave' : 7,
        'Compensatory off' : 8,'Permission' : 9,'Earned Leave': 10,'Special or Causal Leave': 11,'Sick Leave': 12,'Bereavement Leave': 13,'Paternity Leave' : 14,
        'Special Leave' : 15,'Flexi - Work From Home' : 16,'Optional Holiday' : 17,'Maternity Leave' : 18,'Emergency GL' : 19,'Relocation Leave' : 21,'Testing' : 24,'Restricted Leave' : 28,'Summer leave' : 29
        }
        print(leavetype_dict)
        input_leave_type = tracker.get_slot('LeaveType')
        distances = {k: Levenshtein.distance(input_leave_type.lower(), k.lower()) for k in leavetype_dict.keys()}
        closest_key = min(distances, key=distances.get)
        AvailableLeaves = leavetype_dict[closest_key]
        print(Leavetype_id_dict)
        print(closest_key)
        leavetype_id = Leavetype_id_dict[closest_key]
        print(f"user select leave type ::: {closest_key} {AvailableLeaves}")

        print(f"leave type id ::: {Leavetype_id_dict} --> {leavetype_id}")

        print("------end leave type ----------")       

        print(f"Requested Leaves = {RequestedLeaves}")
        print(f"Input Day = {tracker.get_slot('dateValue')}")
        print(f"Input Month = {tracker.get_slot('monthValue')}")
        

        Datevalue_str = tracker.get_slot('dateValue')
        if Datevalue_str.isdigit():
            Datevalue = Datevalue_str
            print("condition true it is integer day")
        else:
            Datevalue = Datevalue_str[:-2]
            print("condition false it is string day")

        input_day = Datevalue
        input_month = tracker.get_slot("monthValue")

        if RequestedLeaves == 0.5:
            date = 0
        else:
            date = RequestedLeaves - 1

        fromdate_datetime = (datetime.strptime(input_day + " " + input_month + " 2023", "%d %B %Y"))
        fromdate = fromdate_datetime.strftime("%Y-%m-%d")
        todate = (datetime.strptime(input_day + " " + input_month + " 2023", "%d %B %Y") + timedelta(days=date)).strftime("%Y-%m-%d")
        
        print(f"From date = {fromdate}")
        print(f"To date = {todate}")
        today = datetime.now().date()
        # today_str = today.strftime("%Y-%m-%d")
        print(f"Today = {today}")
        now = datetime.now(timezone.utc)
        date_string = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-4] + 'Z'
        print("------------------End-----------------")
        
        url = "https://nexusuat.tvsnext.io:1180/api/Leaves/InsertorUpdateApplyLeave"


        headers = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkVGRjc4NDM0MUMzQTA1REFENEVBODYyNERBRjgzNTEzIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODAyNjUxNzEsImV4cCI6MTY4NDE1MzE3MSwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiTmV4dXNBUEkiLCJjbGllbnRfaWQiOiJuZXh1c191aSIsImp0aSI6IjcwRTZBNDFCMzhFNTIyRjgwNkU3QzlGRTlBMkQxM0YxIiwiaWF0IjoxNjgwMjY1MTcxLCJzY29wZSI6WyJOZXh1c0FQSSJdfQ.pqOG4pU7QqWDZWw2Dz874gMyMw-O0xyrnfSf2L0yjCqv4vJYTb2N9URcrzw75wv6RVW7zsvRabRRiKz8WhKxgHCDWORZZyY_F5pNfRy9kPlcskPBqo3HCezUrWbt1EcgeCRKwT6D1F6tWudKXj9pd8iBj6VuhZVv8XeFiKhF0pn3OYpHofV_IsIRJuYzK895Ckn0w3RHLRR4dFoiHbz_kP1q--FNI7hvexDduzl2BicTu40m5rliZ1kfPyy4_lm9lyHl8b1yn4BMPIccLwjEUrAMzHlTonWUXeV4wG0i3mjWrr1eONfPkyk1ziNtqqIHRBc-r1ZOafJncU-BjSbwtw'
        }

        params = {
            "leaveDetails": {
                "leaveId": 0,
                "employeeId": 245,
                "leaveTypeId": leavetype_id,
                "fromDate": fromdate+"T00:00:00.000Z",
                "toDate": todate+"T00:00:00.000Z",
                "noOfDays": RequestedLeaves,
                "leaveType": closest_key,
                "reason": "testing for chatbot",
                "appliedLeaveDetails": [
                    {
                        "appliedLeaveDetailsID": 0,
                        "date": fromdate+"T00:00:00.000Z",
                        "isFullDay": isFullDay,
                        "isFirstHalf": isFirstHalf,
                        "isSecondHalf": isSecondHalf,
                        "leaveId": 0,
                        "compensatoryOffId": 0,
                        "createdBy": 245
                    }
                ],
                "createdBy": 245,
                "createdOn": date_string,
                "modifiedBy": 245,
                "modifiedOn": "null",
                "isActive": True,
                "grantEffectiveFromDate": "null",
                "status": "Pending",
                "isGrantLeave": False
            },
            "listOfDocuments": [],
            "shiftId": 1
        }
        
        
        if int(RequestedLeaves) <= AvailableLeaves and fromdate_datetime.date() >= today:
            resp = requests.post(url, headers=headers,json = params).json()
            dispatcher.utter_message(text=resp['statusText'])
            if len("Leave submitted successfully.") == len(resp['statusText']):
                # dispatcher.utter_message(text=f"")
                dispatcher.utter_message(text=f"You have {AvailableLeaves - (RequestedLeaves)} {closest_key} available.")
            print(resp['statusText'])
            print("Future day")
        else:
            dispatcher.utter_message(text=f"You have {AvailableLeaves} days but requested {RequestedLeaves} days.\nMake sure you are applying for future days. \nTry Again")
        
        return []

class trainingClass(Action):

    def name(self) -> Text:
        return "action_training"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        print(f"Leave Type = {tracker.get_slot('LeaveType')}")
        print(tracker.get_slot('daycount'))
        
        return []