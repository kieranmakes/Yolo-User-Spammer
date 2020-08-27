import os
import time
import json

usersFile = open("users.json","r")
users = json.load(usersFile)



if input("add user: ") == 'yes': 
    name = input("name: ")
    code = input("code: ")
    with open("users.json", "r+") as file:
        data = json.load(file)
        data.update({name: code})
        file.seek(0)
        json.dump(data, file)
    file.close()

user = str(input("enter the user you would like to chose: "))
user = users[user]
for i in range (0,100):
    tunaFile = open("tuna.txt", "r")
    for line in tunaFile:
        text = line.rstrip()
        command = """curl 'https://onyolo.com/""" + user +"""/message' -H 'Connection: keep-alive' -H 'Accept: application/json, text/plain, */*' -H 'Sec-Fetch-Dest: empty' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36' -H 'Content-Type: application/json;charset=UTF-8' -H 'Origin: https://onyolo.com' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Referer: https://onyolo.com/m/""" + user + """?w=Send%20honest%20messages%20%F0%9F%98%87' -H 'Accept-Language: en-US,en;q=0.9' -H 'Cookie: popshow-temp-id=fi6awvm3b1ftikepnk0k6c' --data-binary '{"text":\"""" + text + """\","cookie":"fi6awvm3b1ftikepnk0k6c","wording":"- tuna man"}' --compressed """
        os.system(command)
        time.sleep(4)
    time.sleep(20)
