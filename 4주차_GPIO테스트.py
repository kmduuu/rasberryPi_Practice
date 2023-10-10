import RPi.GPIO as GPIO
import time

print("GPIO Test")

# GPIO 핀 번호 설정 (BCM 모드)

led_pin_2 = 5

# GPIO 핀 설정
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

try:
    while True:
        
        # LED 2 켜기
        print("Led 2 ON")
        GPIO.setup(led_pin_2, GPIO.OUT)
        GPIO.output(led_pin_2, GPIO.HIGH)
        time.sleep(5)
        
        # LED 2 끄기
        print("Led 2 OFF")
        GPIO.setup(led_pin_2, GPIO.OUT)
        GPIO.output(led_pin_2, GPIO.LOW)
        time.sleep(5)

except KeyboardInterrupt:
    # 프로그램 종료 시 GPIO 설정 초기화
    GPIO.cleanup()
