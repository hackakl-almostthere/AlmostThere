#!../env/Scripts/python
import os
import sys

import threading



if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AlmostThere.settings")

    from django.core.management import execute_from_command_line

    # import UpdateVehicleLocations

    # updateThread = threading.Thread(target=UpdateVehicleLocations.UpdateVehicle())

    # updateThread.start()

    execute_from_command_line(sys.argv)
