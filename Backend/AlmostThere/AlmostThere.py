import json
import urllib.request

from User import User
from Stop import Stop

from Math import Calculate_Distance_Between_Two_LatLong

API_KEY_AT = "api_key=d0efe139-8e8d-4ff1-b020-7a71c9bbcb8e"

def main():
    print("starting")

    user = User(-36.854134, 174.767841)
    stop = Stop(-36.843574, 174.766931)

    print(user.calculate_walking_time(stop))


if __name__ == "__main__":
    main()