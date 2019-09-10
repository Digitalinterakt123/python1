import requests
import json


user_name="Raju"
password="Raju@123!"


def login(user_name, password):
    r = requests.post("https://login2.responsys.net/rest/api/v1.3/auth/token",
                      data={"user_name":f"{user_name}", "password":f"{password}", "auth_type":"password"})


# to get status code
#    print(r.status_code)

# to get various status codes
# print(requests.codes["ok"])

    # endpoint = r.json()["endPoint"]
    # authtoken = r.json()["authToken"]
    # return [endpoint,authtoken]

    return r.json()


endpoint_token = login(user_name,password)
print(endpoint_token)



def get_mem_using_riid(endpoint_token1,list_name,riid):
    endPoint = endpoint_token1["endPoint"]
    authToken = endpoint_token1["authToken"]
    r = requests.get(f"{endPoint}/rest/api/v1.3/lists/{list_name}/members/{riid}", headers={"Authorization":f'{authToken}'},params={"fs":"all"})
    # print(req.status_code)
    # response = r.json()
    # return response
    # print(r.json())

    # print(r.json()["recordData"]["fieldNames"])
    print(r.json()["recordData"]["records"][0])



get_mem_using_riid(endpoint_token, "2016 list","50091202")
# print(response["recordData"]["records"][0])