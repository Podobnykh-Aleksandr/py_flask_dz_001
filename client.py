import requests


HOST = "http://127.0.0.1:5000/"


# method GET
def method_get(variable):
    resp = requests.get(f"{HOST}/api/{variable}")
    return resp.json()


# method POST
def method_post(json_data):
    requests.post(f"{HOST}/api/post", json=json_data)


# method DELETE
def method_del(variable):
    requests.delete(f"{HOST}/api/{variable}")


# method PATCH
def method_patch(variable, json_data):
    resp = requests.patch(f"{HOST}/api/{variable}", json=json_data)
    return resp.json()


