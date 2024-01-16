import requests

API_KEY = "0cb40cd157e6db21578293599dd2e848"


def get_data(place, forcast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forcast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forcast_days=3, kind="Sky"))
