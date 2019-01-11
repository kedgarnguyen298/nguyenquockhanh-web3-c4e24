import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds147354.mlab.com:47354/user_data

host = "ds147354.mlab.com"
port = 47354
db_name = "user_data"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())