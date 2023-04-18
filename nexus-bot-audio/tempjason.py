# # import requests

# # api_address='https://run.mocky.io/v3/a9a51f3e-cb03-4c16-ac0a-afb46f6a50e3'

# # json_data = requests.get(api_address).json() 
# # #format_add = json_data['Sai']
# # temp1=""

# # for person in json_data:
# #     name = json_data[person]["Name"]
# #     leaves = json_data[person]["Leaves"]
# #     temp = (f"{json_data[person]['Name']} has {json_data[person]['Leaves']}.\n")
# #     temp1 = temp1+temp 
# # print(temp1)
# # #print(format_add) 
# # print(json_data)

# # json_data = requests.get(api_address).json() 
# #         format_add = json_data['Test']
# #         print(format_add) 
# #         # return format_add
# #         dispatcher.utter_message(text=format_add)

# # import requests

# # api_address='https://nexusuat.tvsnext.io:1180/api/Leaves/GetAvailableLeaveDetailsByEmployee?employeeID=1'


# # json_data = requests.get(api_address).json() 
# # print(json_data)

# import requests

# # url = "https://nexusuat.tvsnext.io:1180/api/Leaves/GetAvailableLeaveDetailsByEmployee?employeeID=1"


# # headers = {
# #     'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkVGRjc4NDM0MUMzQTA1REFENEVBODYyNERBRjgzNTEzIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODAyNjUxNzEsImV4cCI6MTY4NDE1MzE3MSwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiTmV4dXNBUEkiLCJjbGllbnRfaWQiOiJuZXh1c191aSIsImp0aSI6IjcwRTZBNDFCMzhFNTIyRjgwNkU3QzlGRTlBMkQxM0YxIiwiaWF0IjoxNjgwMjY1MTcxLCJzY29wZSI6WyJOZXh1c0FQSSJdfQ.pqOG4pU7QqWDZWw2Dz874gMyMw-O0xyrnfSf2L0yjCqv4vJYTb2N9URcrzw75wv6RVW7zsvRabRRiKz8WhKxgHCDWORZZyY_F5pNfRy9kPlcskPBqo3HCezUrWbt1EcgeCRKwT6D1F6tWudKXj9pd8iBj6VuhZVv8XeFiKhF0pn3OYpHofV_IsIRJuYzK895Ckn0w3RHLRR4dFoiHbz_kP1q--FNI7hvexDduzl2BicTu40m5rliZ1kfPyy4_lm9lyHl8b1yn4BMPIccLwjEUrAMzHlTonWUXeV4wG0i3mjWrr1eONfPkyk1ziNtqqIHRBc-r1ZOafJncU-BjSbwtw'
# # }


# # resp = requests.get(url, headers=headers).json()
# # #print(resp)
# # for data in resp['data']:
# #     if data['leaveType'] == 'Old Earned Leave':
# #         print(f"you have {data['availableLeaves']} Avilable Leaves from {data['leaveType']}")
# #print(resp.status_code)
# # print((requests.get(url, headers=headers)).status_code)
# # print(resp['data']['leaveType'])

# fromdate = '2023-04-05'
# todate = '2023-04-05'
# url = "https://nexusuat.tvsnext.io:1180/api/Leaves/InsertorUpdateApplyLeave"


# headers = {
#     'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkVGRjc4NDM0MUMzQTA1REFENEVBODYyNERBRjgzNTEzIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODAyNjUxNzEsImV4cCI6MTY4NDE1MzE3MSwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiTmV4dXNBUEkiLCJjbGllbnRfaWQiOiJuZXh1c191aSIsImp0aSI6IjcwRTZBNDFCMzhFNTIyRjgwNkU3QzlGRTlBMkQxM0YxIiwiaWF0IjoxNjgwMjY1MTcxLCJzY29wZSI6WyJOZXh1c0FQSSJdfQ.pqOG4pU7QqWDZWw2Dz874gMyMw-O0xyrnfSf2L0yjCqv4vJYTb2N9URcrzw75wv6RVW7zsvRabRRiKz8WhKxgHCDWORZZyY_F5pNfRy9kPlcskPBqo3HCezUrWbt1EcgeCRKwT6D1F6tWudKXj9pd8iBj6VuhZVv8XeFiKhF0pn3OYpHofV_IsIRJuYzK895Ckn0w3RHLRR4dFoiHbz_kP1q--FNI7hvexDduzl2BicTu40m5rliZ1kfPyy4_lm9lyHl8b1yn4BMPIccLwjEUrAMzHlTonWUXeV4wG0i3mjWrr1eONfPkyk1ziNtqqIHRBc-r1ZOafJncU-BjSbwtw'
# }

# params = {
#   "leaveDetails": {
#     "leaveId": 0,
#     "employeeId": 911,
#     "leaveTypeId": 3,
#     "fromDate": fromdate+"T00:00:00.000Z",
#     "toDate": todate+"T00:00:00.000Z",
#     "noOfDays": 1,
#     "leaveType": "General Leave",
#     "reason": "test",
#     "appliedLeaveDetails": [
#       {
#         "appliedLeaveDetailsID": 0,
#         "date": "2023-04-05T00:00:00.000Z",
#         "isFullDay": True,
#         "isFirstHalf": False,
#         "isSecondHalf": False,
#         "leaveId": 0,
#         "compensatoryOffId": 0,
#         "createdBy": 911
#       }
#     ],
#     "createdBy": 911,
#     "createdOn": "2023-04-04T06:41:49.405Z",
#     "modifiedBy": 911,
#     "modifiedOn": "NULL",
#     "isActive": True,
#     "grantEffectiveFromDate": "null",
#     "status": "Pending",
#     "isGrantLeave": False
#   },
#   "listOfDocuments": [],
#   "shiftId": 1
# }

# resp = requests.post(url, headers=headers,json = params).json()
# print(resp['statusText'])
# # print(params)
# # #print(json.loads(params))
# print((requests.post(url, headers=headers,json = params ).status_code))

# # import datetime
# # d = datetime.datetime.strptime("12/10/2020", "%d/%m/%Y")
# # s = d.isoformat()
# # print(s)

# import datetime

# today = datetime.date.today()
# print(today.year)
# print(today)

# input_string = "722 th"
# output_string = input_string.replace("th", "")
# output_number = int(output_string)

# print(output_number)

# import datetime

# month_string = "june"  # Replace this with your input

# # Convert the month string to a datetime object with a dummy day
# month_date = datetime.datetime.strptime(month_string, '%B')

# # Get the month value as an integer
# month_int = month_date.month

# # Print the integer value of the month
# print(month_int)

from datetime import datetime, timedelta

input_day = "6"
input_month = "March"
date = 0
fromdate_date = (datetime.strptime(input_day + " " + input_month + " 2023", "%d %B %Y"))
fromdate=fromdate_date.strftime("%Y-%m-%d")
todate = (datetime.strptime(input_day + " " + input_month + " 2023", "%d %B %Y") + timedelta(days=date)).strftime("%Y-%m-%d")
#output_date_str = todate.strftime("%Y-%m-%d")
print(f"fromdate = {fromdate}")
print(todate)
#print(output_date_str)
today = datetime.now().date()

# Compare dates
if fromdate_date.date() > today:
    print("fromdate is greater than today")
else:
    print("fromdate is not greater than today")

input_day = "2nd"

# Extract only the numeric part of the input
day_number = input_day[:-2]

# Print the result
print(day_number)

a = "1"

if a.isdigit():
    print("integer")
else:
    print("not integer")
