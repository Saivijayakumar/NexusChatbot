# import requests

# api_address='https://run.mocky.io/v3/a9a51f3e-cb03-4c16-ac0a-afb46f6a50e3'

# json_data = requests.get(api_address).json() 
# #format_add = json_data['Sai']
# temp1=""

# for person in json_data:
#     name = json_data[person]["Name"]
#     leaves = json_data[person]["Leaves"]
#     temp = (f"{json_data[person]['Name']} has {json_data[person]['Leaves']}.\n")
#     temp1 = temp1+temp 
# print(temp1)
# #print(format_add) 
# print(json_data)

# json_data = requests.get(api_address).json() 
#         format_add = json_data['Test']
#         print(format_add) 
#         # return format_add
#         dispatcher.utter_message(text=format_add)

# import requests

# api_address='https://nexusuat.tvsnext.io:1180/api/Leaves/GetAvailableLeaveDetailsByEmployee?employeeID=1'


# json_data = requests.get(api_address).json() 
# print(json_data)

import requests

# url = "https://nexusuat.tvsnext.io:1180/api/Leaves/GetAvailableLeaveDetailsByEmployee?employeeID=1"


# headers = {
#     'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkVGRjc4NDM0MUMzQTA1REFENEVBODYyNERBRjgzNTEzIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODAyNjUxNzEsImV4cCI6MTY4NDE1MzE3MSwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiTmV4dXNBUEkiLCJjbGllbnRfaWQiOiJuZXh1c191aSIsImp0aSI6IjcwRTZBNDFCMzhFNTIyRjgwNkU3QzlGRTlBMkQxM0YxIiwiaWF0IjoxNjgwMjY1MTcxLCJzY29wZSI6WyJOZXh1c0FQSSJdfQ.pqOG4pU7QqWDZWw2Dz874gMyMw-O0xyrnfSf2L0yjCqv4vJYTb2N9URcrzw75wv6RVW7zsvRabRRiKz8WhKxgHCDWORZZyY_F5pNfRy9kPlcskPBqo3HCezUrWbt1EcgeCRKwT6D1F6tWudKXj9pd8iBj6VuhZVv8XeFiKhF0pn3OYpHofV_IsIRJuYzK895Ckn0w3RHLRR4dFoiHbz_kP1q--FNI7hvexDduzl2BicTu40m5rliZ1kfPyy4_lm9lyHl8b1yn4BMPIccLwjEUrAMzHlTonWUXeV4wG0i3mjWrr1eONfPkyk1ziNtqqIHRBc-r1ZOafJncU-BjSbwtw'
# }


# resp = requests.get(url, headers=headers).json()
# #print(resp)
# for data in resp['data']:
#     if data['leaveType'] == 'Old Earned Leave':
#         print(f"you have {data['availableLeaves']} Avilable Leaves from {data['leaveType']}")
#print(resp.status_code)
# print((requests.get(url, headers=headers)).status_code)
# print(resp['data']['leaveType'])

fromdate = '2023-04-05'
todate = '2023-04-05'
url = "https://nexusuat.tvsnext.io:1180/api/Leaves/InsertorUpdateApplyLeave"


headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkVGRjc4NDM0MUMzQTA1REFENEVBODYyNERBRjgzNTEzIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODAyNjUxNzEsImV4cCI6MTY4NDE1MzE3MSwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiTmV4dXNBUEkiLCJjbGllbnRfaWQiOiJuZXh1c191aSIsImp0aSI6IjcwRTZBNDFCMzhFNTIyRjgwNkU3QzlGRTlBMkQxM0YxIiwiaWF0IjoxNjgwMjY1MTcxLCJzY29wZSI6WyJOZXh1c0FQSSJdfQ.pqOG4pU7QqWDZWw2Dz874gMyMw-O0xyrnfSf2L0yjCqv4vJYTb2N9URcrzw75wv6RVW7zsvRabRRiKz8WhKxgHCDWORZZyY_F5pNfRy9kPlcskPBqo3HCezUrWbt1EcgeCRKwT6D1F6tWudKXj9pd8iBj6VuhZVv8XeFiKhF0pn3OYpHofV_IsIRJuYzK895Ckn0w3RHLRR4dFoiHbz_kP1q--FNI7hvexDduzl2BicTu40m5rliZ1kfPyy4_lm9lyHl8b1yn4BMPIccLwjEUrAMzHlTonWUXeV4wG0i3mjWrr1eONfPkyk1ziNtqqIHRBc-r1ZOafJncU-BjSbwtw'
}

params = {
  "leaveDetails": {
    "leaveId": 0,
    "employeeId": 911,
    "leaveTypeId": 3,
    "fromDate": fromdate+"T00:00:00.000Z",
    "toDate": todate+"T00:00:00.000Z",
    "noOfDays": 1,
    "leaveType": "General Leave",
    "reason": "test",
    "appliedLeaveDetails": [
      {
        "appliedLeaveDetailsID": 0,
        "date": "2023-04-05T00:00:00.000Z",
        "isFullDay": True,
        "isFirstHalf": False,
        "isSecondHalf": False,
        "leaveId": 0,
        "compensatoryOffId": 0,
        "createdBy": 911
      }
    ],
    "createdBy": 911,
    "createdOn": "2023-04-04T06:41:49.405Z",
    "modifiedBy": 911,
    "modifiedOn": "NULL",
    "isActive": True,
    "grantEffectiveFromDate": "null",
    "status": "Pending",
    "isGrantLeave": False
  },
  "listOfDocuments": [],
  "shiftId": 1
}

resp = requests.post(url, headers=headers,json = params).json()
print(resp['statusText'])
# print(params)
# #print(json.loads(params))
print((requests.post(url, headers=headers,json = params ).status_code))

# import datetime
# d = datetime.datetime.strptime("12/10/2020", "%d/%m/%Y")
# s = d.isoformat()
# print(s)

import datetime

today = datetime.date.today()
print(today.year)
print(today)