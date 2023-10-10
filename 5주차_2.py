import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18 # GPIO 12 pin
GPIO_ECHO = 24 # GPIO 18 pin

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
            TimeElapsed = StopTime - StartTime
            distance = (TimeElapsed * 34300) / 2
            return distance

def bt_led_on():
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(22, GPIO.HIGH)
    print("LED Works!")

def bt_led_off():
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(22, GPIO.LOW)
    print("LED Not Works!")

try:
    while True:
        # Trig 핀에 초음파 신호 발신
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        # Echo 핀에서 초음파 수신
        while GPIO.input(GPIO_ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(GPIO_ECHO) == 1:
            pulse_end = time.time()

        # 초음파 신호의 왕복 시간 계산
        pulse_duration = pulse_end - pulse_start

        # 거리 계산 (음속: 343m/s)
        distance = (pulse_duration * 34300) / 2

        if distance is not None:
            print("Distance: {:.2f} cm".format(distance))
            if distance < 30:
                print("LED ON")
                bt_led_on()
            else:
                print("LED OFF")
                bt_led_off()
        else:
            print("Measurement failed")

        time.sleep(0.2)  # 측정 주기 설정

except KeyboardInterrupt:
    GPIO.cleanup()
        
        
        
        