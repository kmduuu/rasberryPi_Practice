import time
import board  # BCM 핀 배열 사용
import adafruit_dht
import psutil

# We first check if a libgpiod process is running. If yes,
# we kill it!
for proc in psutil.process_iter():
    print(proc)
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

sensor = adafruit_dht.DHT11(board.D23)  # BCM23 -> 16번핀

while True:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print("Temperature: {}*C Humidity: {}% ".format(temp, humidity))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(3.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(3.0)