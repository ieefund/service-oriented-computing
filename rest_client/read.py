import requests

if __name__ == "__main__":
    res = requests.get(
        url='http://127.0.0.1:5000/resource/t5'
    )
    print(res.status_code)
    d = res.json()
    print(d["sensor_id"])
    print(d["temperature"])
    print(d["location"])
    print(d["datetime"])

    res = requests.get(
        url='http://127.0.0.1:5000/resource/location/1st'
    )
    print(res.status_code)
    print(type(res.json()))
