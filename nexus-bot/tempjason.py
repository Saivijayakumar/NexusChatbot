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

url = "https://nexusuat.tvsnext.io:1180/api/Leaves/GetAvailableLeaveDetailsByEmployee?employeeID=1"


headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkVGRjc4NDM0MUMzQTA1REFENEVBODYyNERBRjgzNTEzIiwidHlwIjoiYXQrand0In0.eyJuYmYiOjE2ODAyNjUxNzEsImV4cCI6MTY4NDE1MzE3MSwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiTmV4dXNBUEkiLCJjbGllbnRfaWQiOiJuZXh1c191aSIsImp0aSI6IjcwRTZBNDFCMzhFNTIyRjgwNkU3QzlGRTlBMkQxM0YxIiwiaWF0IjoxNjgwMjY1MTcxLCJzY29wZSI6WyJOZXh1c0FQSSJdfQ.pqOG4pU7QqWDZWw2Dz874gMyMw-O0xyrnfSf2L0yjCqv4vJYTb2N9URcrzw75wv6RVW7zsvRabRRiKz8WhKxgHCDWORZZyY_F5pNfRy9kPlcskPBqo3HCezUrWbt1EcgeCRKwT6D1F6tWudKXj9pd8iBj6VuhZVv8XeFiKhF0pn3OYpHofV_IsIRJuYzK895Ckn0w3RHLRR4dFoiHbz_kP1q--FNI7hvexDduzl2BicTu40m5rliZ1kfPyy4_lm9lyHl8b1yn4BMPIccLwjEUrAMzHlTonWUXeV4wG0i3mjWrr1eONfPkyk1ziNtqqIHRBc-r1ZOafJncU-BjSbwtw'
}


resp = requests.get(url, headers=headers).json()
print(resp)
#print(resp.status_code)
print((requests.get(url, headers=headers)).status_code)


