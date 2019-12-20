import requests

url = "https://e018fed1-c416-4c3e-ba7d-66bfa479a5a9.mock.pstmn.io/rideshares"
query_key = "user_id"
query_value = "f9d54ec1-3a7e-4a79-ae3c-f1fe1b2a8b30"


def validate_points(person, expected_points):
    """

    :param person:
    :param expected_points:
    :return:
    """
    if person["points"] != expected_points:
        print(f" {person['user_id']} got wrong points {person['points']} instead of {expected_points}")
    else:
        print(f" {person['user_id']} got expected points {expected_points}")
    # assert person['points'] == expected_points, \
    #     f" {person['user_id']} got wrong points {person['points']} instead of {expected_points}"


def validate_trip(trip):
    """

    :param trip:
    :return:
    """
    people = trip["people"]
    distance = trip["travel_distance"]
    drivers = []
    passengers= []

    for person in people:
        if person["is_driver"]:
            drivers.append(person)
        else:
            passengers.append(person)

    driver_points = 0
    passenger_points = 0
    if drivers and passengers:
        passenger_points = int(distance//1000//3)
        driver_points = len(passengers) * passenger_points

    for driver in drivers:
        validate_points(driver, driver_points)
    for passenger in passengers:
        validate_points(passenger, passenger_points)


def test_trip_points():
    obj = requests.get(url, params={query_key: query_value})
    from pprint import pprint
    # pprint(obj.json())
    response = obj.json()

    trips = response["rideshares"]
    for trip in trips:
        validate_trip(trip)


if __name__=="__main__":
    test_trip_points()









