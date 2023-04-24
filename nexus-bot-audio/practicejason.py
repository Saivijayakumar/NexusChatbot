import requests

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
# if data['leaveType'] == 'General Leave':
#     print(f"you have {data['displayBalanceLeave']} Avilable Leaves from {data['leaveType']}")

# leavetype_dict = {}
# for data in resp['data']['employeeAvailableLeaveDetails']:
#     if data['displayBalanceLeave'] > 0 :
#         leavetype_dict[data['leaveType']] = data['displayBalanceLeave']
    #print(f"you have {data['displayBalanceLeave']} Avilable Leaves from {data['leaveType']}")


leavetype_dict = {data['leaveType']: data['displayBalanceLeave'] for data in resp['data']['employeeAvailableLeaveDetails'] if data['displayBalanceLeave'] > 0}


if len(leavetype_dict) == 1:
    key, value = next(iter(leavetype_dict.items()))
    print(f"{key}: {value}")
    print(f"You have {value} {key} available, would you like to apply now.")
elif len(leavetype_dict) > 1:
    print("Below are the list of available leaves. Which one would you like to apply?")
    for key, value in leavetype_dict.items():
        print(f"{key}: {value}")
else:
    print("You have no leave balance. I am sorry you can't avail a leave now.\n However, please note that your General Leaves are added incrementally overtime. please check back after sometime. Would you like more info regarding this?")


# General Leave - 5
# Leave without pay - 1
# Sick leave - 2

print(leavetype_dict)
print(len(leavetype_dict))


print("___________________start____________________")
leave_dict = {}  # create an empty dictionary

# add the input values to the dictionary dynamically
leave_dict['General Leave'] = 5
leave_dict['Leave without pay'] = 1
leave_dict['Sick leave'] = 2

# print the resulting dictionary
print(leave_dict)
print("------")
key, value = next(iter(leave_dict.items()))
print(f"{key}: {value}")
print(leave_dict)
#leave_dict = {'General Leave': 5, 'Leave without pay': 1, 'Sick leave': 2}

# iterate over the key-value pairs in the dictionary
for key, value in leave_dict.items():
    print(key + ": " + str(value))

# --------------------------------
import Levenshtein
#pip install python-Levenshtein
leave_dict = {'General Leave': 5, 'Leave without pay': 1, 'Sick leave': 2}

input_str = "leave without" # the input string

# calculate the Levenshtein distance between the input string and each key in the leave_dict
distances = {k: Levenshtein.distance(input_str.lower(), k.lower()) for k in leave_dict.keys()}

# find the key with the minimum Levenshtein distance
closest_key = min(distances, key=distances.get)

# calculate the matching percentage of the closest key
matching_percentage = (1 - (distances[closest_key] / len(closest_key))) * 100

print(f"The closest key in leave_dict for '{input_str}' is '{closest_key}' with a matching percentage of {matching_percentage:.2f}%")
