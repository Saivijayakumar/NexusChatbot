# import requests

# url = "https://nexusuat.tvsnext.io:1180/api/Leaves/GetEmployeeLeavesBalanceDetails"


# headers = {
#     'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkVGRjc4NDM0MUMzQTA1REFENEVBODYyNERBRjgzNTEzIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODAyNjUxNzEsImV4cCI6MTY4NDE1MzE3MSwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiTmV4dXNBUEkiLCJjbGllbnRfaWQiOiJuZXh1c191aSIsImp0aSI6IjcwRTZBNDFCMzhFNTIyRjgwNkU3QzlGRTlBMkQxM0YxIiwiaWF0IjoxNjgwMjY1MTcxLCJzY29wZSI6WyJOZXh1c0FQSSJdfQ.pqOG4pU7QqWDZWw2Dz874gMyMw-O0xyrnfSf2L0yjCqv4vJYTb2N9URcrzw75wv6RVW7zsvRabRRiKz8WhKxgHCDWORZZyY_F5pNfRy9kPlcskPBqo3HCezUrWbt1EcgeCRKwT6D1F6tWudKXj9pd8iBj6VuhZVv8XeFiKhF0pn3OYpHofV_IsIRJuYzK895Ckn0w3RHLRR4dFoiHbz_kP1q--FNI7hvexDduzl2BicTu40m5rliZ1kfPyy4_lm9lyHl8b1yn4BMPIccLwjEUrAMzHlTonWUXeV4wG0i3mjWrr1eONfPkyk1ziNtqqIHRBc-r1ZOafJncU-BjSbwtw'
# }
        
# params = {
#     "employeeId": 245,
#     "fromDate": "2023-04-01",
#     "toDate": "2024-03-31",
#     "departmentId": 15,
#     "shiftId": 1,
#     "LocationId": 1,
#     "dateOfJoining": "2021-06-21T00:00:00"
# }
# request_obj = requests.post(url, headers=headers,json = params)
# resp = request_obj.json()
# print(request_obj.status_code)
# # if data['leaveType'] == 'General Leave':
# #     print(f"you have {data['displayBalanceLeave']} Avilable Leaves from {data['leaveType']}")

# # leavetype_dict = {}
# # for data in resp['data']['employeeAvailableLeaveDetails']:
# #     if data['displayBalanceLeave'] > 0 :
# #         leavetype_dict[data['leaveType']] = data['displayBalanceLeave']
#     #print(f"you have {data['displayBalanceLeave']} Avilable Leaves from {data['leaveType']}")


# leavetype_dict = {data['leaveType']: data['displayBalanceLeave'] for data in resp['data']['employeeAvailableLeaveDetails'] if data['displayBalanceLeave'] > 0}


# if len(leavetype_dict) == 1:
#     key, value = next(iter(leavetype_dict.items()))
#     print(f"{key}: {value}")
#     print(f"You have {value} {key} available, would you like to apply now.")
# elif len(leavetype_dict) > 1:
#     leave_msg = "Below are the list of available leaves. Which one would you like to apply?"
#     print("Below are the list of available leaves. Which one would you like to apply?")
#     for key, value in leavetype_dict.items():
#         print(f"{key}: {value}")
#         leave_msg = leave_msg + f" \n{key}: {value} " 
#     print(leave_msg)
# else:
#     print("You have no leave balance. I am sorry you can't avail a leave now.\n However, please note that your General Leaves are added incrementally overtime. please check back after sometime. Would you like more info regarding this?")


# # General Leave - 5
# # Leave without pay - 1
# # Sick leave - 2

# print(leavetype_dict)
# print(len(leavetype_dict))


# print("___________________start____________________")
# leave_dict = {}  # create an empty dictionary

# # add the input values to the dictionary dynamically
# leave_dict['General Leave'] = 5
# leave_dict['Leave without pay'] = 1
# leave_dict['Sick leave'] = 2

# # print the resulting dictionary
# print(leave_dict)
# print("------")
# key, value = next(iter(leave_dict.items()))
# print(f"{key}: {value}")
# print(leave_dict)
# #leave_dict = {'General Leave': 5, 'Leave without pay': 1, 'Sick leave': 2}

# # iterate over the key-value pairs in the dictionary
# for key, value in leave_dict.items():
#     print(key + ": " + str(value))

# # --------------------------------
# # import Levenshtein
# # #pip install python-Levenshtein
# # leave_dict = {'General Leave': 5, 'Leave without pay': 1, 'Sick leave': 2}

# # input_str = "leave without" # the input string

# # # calculate the Levenshtein distance between the input string and each key in the leave_dict
# # distances = {k: Levenshtein.distance(input_str.lower(), k.lower()) for k in leave_dict.keys()}

# # # find the key with the minimum Levenshtein distance
# # closest_key = min(distances, key=distances.get)

# # # calculate the matching percentage of the closest key
# # matching_percentage = (1 - (distances[closest_key] / len(closest_key))) * 100

# # print(f"The closest key in leave_dict for '{input_str}' is '{closest_key}' with a matching percentage of {matching_percentage:.2f}%")


# import datetime

# # Get the current date and time in UTC timezone
# now_utc = datetime.datetime.utcnow()

# #now_utc = now_utc.replace(microsecond=now_utc.microsecond // 1000 * 1000)

# # Format the datetime as a string in ISO 8601 format with UTC timezone
# iso_stringt = now_utc.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
# iso_string = now_utc.strftime('%Y-%m-%d')
# print(iso_string)
# print(iso_stringt)


# import datetime
# import json

# start_date = datetime.date(2023, 5, 3)
# end_date = datetime.date(2023, 5, 3)
# print(start_date)
# # Define a function to create a dictionary for a given date and leave details
# def create_leave_dict(date, is_full_day, is_first_half, is_second_half):
#     return {
#         "appliedLeaveDetailsID": 0,
#         "date": date.isoformat() + "T00:00:00.000Z",
#         "isFullDay": is_full_day,
#         "isFirstHalf": is_first_half,
#         "isSecondHalf": is_second_half,
#         "leaveId": 0,
#         "compensatoryOffId": 0,
#         "createdBy": 245
#     }

# # Initialize an empty list to hold the leave dictionaries
# leave_list = []

# # Iterate over the range of dates and create a leave dictionary for each date
# for date in range((end_date - start_date).days + 1):
#     current_date = start_date + datetime.timedelta(date)
#     # print(f"date = {date}")
#     # print(f"current day {current_date}")
    
#     # Check if the current date is a weekday (Monday = 0, Sunday = 6)
#     if current_date.weekday() < 5:
#         # If the current date is a weekday, create a full day leave dictionary
#         leave_list.append(create_leave_dict(current_date, True, False, False))
#         print(current_date.isoformat())
#         print(f"current day {current_date}")
#     else:
#         # If the current date is a weekend, skip it
#         continue



# result_json = json.dumps(leave_list)
# print(result_json)

# from datetime import datetime, timedelta

# date = "2023-05-03"
# number = 4-1

# date_format = "%Y-%m-%d"
# date_obj = datetime.strptime(date, date_format).date()

# # loop through the number of days and skip weekends
# for i in range(number):
#     next_date = date_obj + timedelta(days=1)
#     print(f" next day {next_date}")
#     while next_date.weekday() in [5, 6]:
#         next_date += timedelta(days=1)
#         print(f" next day in loop{next_date}")
#     date_obj = next_date
#     print(f" date obj {date_obj}")


# # convert the result back to string format
# result = date_obj.strftime(date_format)
# print(result)

# import requests
# import datetime

# now_utc = datetime.datetime.utcnow()
# today = now_utc.strftime('%Y-%m-%d')
# url = "https://nexusuat.tvsnext.io:1180/api/Attendance/GetDailyAttendanceDetails"


# headers = {
#     'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkVGRjc4NDM0MUMzQTA1REFENEVBODYyNERBRjgzNTEzIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODAyNjUxNzEsImV4cCI6MTY4NDE1MzE3MSwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiTmV4dXNBUEkiLCJjbGllbnRfaWQiOiJuZXh1c191aSIsImp0aSI6IjcwRTZBNDFCMzhFNTIyRjgwNkU3QzlGRTlBMkQxM0YxIiwiaWF0IjoxNjgwMjY1MTcxLCJzY29wZSI6WyJOZXh1c0FQSSJdfQ.pqOG4pU7QqWDZWw2Dz874gMyMw-O0xyrnfSf2L0yjCqv4vJYTb2N9URcrzw75wv6RVW7zsvRabRRiKz8WhKxgHCDWORZZyY_F5pNfRy9kPlcskPBqo3HCezUrWbt1EcgeCRKwT6D1F6tWudKXj9pd8iBj6VuhZVv8XeFiKhF0pn3OYpHofV_IsIRJuYzK895Ckn0w3RHLRR4dFoiHbz_kP1q--FNI7hvexDduzl2BicTu40m5rliZ1kfPyy4_lm9lyHl8b1yn4BMPIccLwjEUrAMzHlTonWUXeV4wG0i3mjWrr1eONfPkyk1ziNtqqIHRBc-r1ZOafJncU-BjSbwtw'
# }

# params = {
#     "employeeId": 245,
#     "shiftDate": today,
#     "shiftDetailsId": 1
# }
# resp_attendance = requests.post(url, headers=headers,json = params)
# resp = resp_attendance.json()
# print(resp['attendanceWithBreakDetail']['weeklyMonthlyAttendanceDetail'])

# for data in resp['attendanceWithBreakDetail']['weeklyMonthlyAttendanceDetail']:
#     print(data['workLocation'])


import difflib

#home_list = ["workfromhome","work from home","wfh","WFH","Work From Home","home","Home"]
home_list = ["client","client site","client place","clientsite","clientplace"]
input_word = "office"

# convert input word to lowercase
input_word = input_word.lower()

# loop through each string in home_list and check if input_word is similar
for string in home_list:
    # convert string to lowercase
    string = string.lower()
    print(difflib.SequenceMatcher(None, input_word, string).ratio())
    # check if input_word and string have a similarity score of at least 0.6
    if difflib.SequenceMatcher(None, input_word, string).ratio() >= 0.6:
        print("remote")
        break
else:
    print("not remote")
