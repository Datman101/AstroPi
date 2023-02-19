from sense_hat import SenseHat
from datetime import datetime
from csv import writer

sense = SenseHat()

#finds out where to put the file, idk if/how it works i just copy pasted off astro pi website
from pathlib import Path
base_folder = Path(__file__).parent.resolve()
data_file = base_folder / "data.csv"

#function that gets all the data, clue's in the name
def getData():
    data = []
    # orientation
    orientation = sense.get_orientation()
    data.append(orientation["yaw"])
    data.append(orientation["pitch"])
    data.append(orientation["roll"])
    # compass
    mag = sense.get_compass_raw()
    data.append(mag["x"])
    data.append(mag["y"])
    data.append(mag["z"])
    # accelerometer
    acc = sense.get_accelerometer_raw()
    data.append(acc["x"])
    data.append(acc["y"])
    data.append(acc["z"])
    # gyroscope
    gyro = sense.get_gyroscope_raw()
    data.append(gyro["x"])
    data.append(gyro["y"])
    data.append(gyro["z"])
    # time
    data.append(datetime.now())

    return data

#writes data to a csv file, once again copied from astro pi docs, i think all you need to do is call the function every 15 seconds
def writeData():
    with open("data.csv", "w", buffering=1, newline='') as f:
        #idk what a data writer is but i hope it works
        data_writer = writer(f)
        data = getData()
        data_writer.writerow(data)
