import requests
                                  
                                  # prduction url
# url = "https://nexus.tvsnext.io:1080/api/Leaves/GetEmployeeLeaveAndRestrictionDetails"


# headers = {
#     'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkVGRjc4NDM0MUMzQTA1REFENEVBODYyNERBRjgzNTEzIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODAyNjUxNzEsImV4cCI6MTY4NDE1MzE3MSwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiTmV4dXNBUEkiLCJjbGllbnRfaWQiOiJuZXh1c191aSIsImp0aSI6IjcwRTZBNDFCMzhFNTIyRjgwNkU3QzlGRTlBMkQxM0YxIiwiaWF0IjoxNjgwMjY1MTcxLCJzY29wZSI6WyJOZXh1c0FQSSJdfQ.pqOG4pU7QqWDZWw2Dz874gMyMw-O0xyrnfSf2L0yjCqv4vJYTb2N9URcrzw75wv6RVW7zsvRabRRiKz8WhKxgHCDWORZZyY_F5pNfRy9kPlcskPBqo3HCezUrWbt1EcgeCRKwT6D1F6tWudKXj9pd8iBj6VuhZVv8XeFiKhF0pn3OYpHofV_IsIRJuYzK895Ckn0w3RHLRR4dFoiHbz_kP1q--FNI7hvexDduzl2BicTu40m5rliZ1kfPyy4_lm9lyHl8b1yn4BMPIccLwjEUrAMzHlTonWUXeV4wG0i3mjWrr1eONfPkyk1ziNtqqIHRBc-r1ZOafJncU-BjSbwtw'
# }
 
# params = {
#     "employeeId": 245,
#     "fromDate": "2023-04-01",
#     "toDate": "2024-03-31",
#     "departmentId": 1065,
#     "shiftId": 1,
#     "LocationId": 1015,
#     "dateOfJoining": "2022-06-06T00:00:00"
# }

# resp = requests.post(url, headers=headers,json = params).json()

# # print(resp['data']['employeeAvailableLeaveDetails'])

# for data in resp['data']['employeeAvailableLeaveDetails']:
#     print(f"employee id = {data['employeeID']} - {data['leaveType']} - {data['displayBalanceLeave']}")

   
                              # UAT data
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


# # resp = requests.post(url, headers=headers,json = params).json()
# # print(requests.post(url, headers=headers,json = params).status_code)

# request_obj = requests.post(url, headers=headers,json = params)
# resp = request_obj.json()
# print(request_obj.status_code)
# # print(resp['data']['employeeAvailableLeaveDetails'])

# for data in resp['data']['employeeAvailableLeaveDetails']:
#     if data['leaveType'] == 'General Leave':
#         print(f"employee id = {data['employeeID']} - {data['leaveType']} - {data['displayBalanceLeave']}")

                                                       # UAT inser leaves

import requests
from datetime import datetime, timedelta, timezone
from word2number import w2n

AvailableLeaves = 16
RequestedLeaves = 1
print("------------start-----------------------")


print(f"Days count = {RequestedLeaves}")
print(f"Requested Leaves = {RequestedLeaves}")


Datevalue_str = "17th"
Datevalue = Datevalue_str[:-2]

input_day = Datevalue
input_month = "april"
date = RequestedLeaves - 1
fromdate_datetime = (datetime.strptime(input_day + " " + input_month + " 2023", "%d %B %Y"))
fromdate = fromdate_datetime.strftime("%Y-%m-%d")
todate = (datetime.strptime(input_day + " " + input_month + " 2023", "%d %B %Y") + timedelta(days=date)).strftime("%Y-%m-%d")

print(f"From date = {fromdate}")
print(f"To date = {todate}")
today = datetime.now().date()
today_str = today.strftime("%Y-%m-%d")
print(f"Today = {today}")
now = datetime.now(timezone.utc)
date_string = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-4] + 'Z'
print(date_string)
print("------------------End-----------------")

url = "https://nexusuat.tvsnext.io:1180/api/Leaves/InsertorUpdateApplyLeave"


headers = {
'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkVGRjc4NDM0MUMzQTA1REFENEVBODYyNERBRjgzNTEzIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODAyNjUxNzEsImV4cCI6MTY4NDE1MzE3MSwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiTmV4dXNBUEkiLCJjbGllbnRfaWQiOiJuZXh1c191aSIsImp0aSI6IjcwRTZBNDFCMzhFNTIyRjgwNkU3QzlGRTlBMkQxM0YxIiwiaWF0IjoxNjgwMjY1MTcxLCJzY29wZSI6WyJOZXh1c0FQSSJdfQ.pqOG4pU7QqWDZWw2Dz874gMyMw-O0xyrnfSf2L0yjCqv4vJYTb2N9URcrzw75wv6RVW7zsvRabRRiKz8WhKxgHCDWORZZyY_F5pNfRy9kPlcskPBqo3HCezUrWbt1EcgeCRKwT6D1F6tWudKXj9pd8iBj6VuhZVv8XeFiKhF0pn3OYpHofV_IsIRJuYzK895Ckn0w3RHLRR4dFoiHbz_kP1q--FNI7hvexDduzl2BicTu40m5rliZ1kfPyy4_lm9lyHl8b1yn4BMPIccLwjEUrAMzHlTonWUXeV4wG0i3mjWrr1eONfPkyk1ziNtqqIHRBc-r1ZOafJncU-BjSbwtw'
}

params = {
"leaveDetails": {
    "leaveId": 0,
    "employeeId": 245,
    "leaveTypeId": 3,
    "fromDate": fromdate+"T00:00:00.000Z",
    "toDate": todate+"T00:00:00.000Z",
    "noOfDays": RequestedLeaves,
    "leaveType": "General Leave",
    "reason": "Applied Form bot",
    "appliedLeaveDetails": [
        {
            "appliedLeaveDetailsID": 0,
            "date": fromdate+"T00:00:00.000Z",
            "isFullDay": True,
            "isFirstHalf": False,
            "isSecondHalf": False,
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
    print("Future day")
    resp = requests.post(url, headers=headers,json = params).json()
    print(resp['statusText'])
else:
    print("past")
# resp = requests.post(url, headers=headers,json = params).json()
# dispatcher.utter_message(text=resp['statusText'])
# print(resp['statusText'])
