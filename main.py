import machine
import hcsr04
import time
#from umqtt.simple import MQTTClient
from time import sleep
from uthingsboard.client import TBDeviceMqttClient
client = TBDeviceMqttClient('194.233.89.191', access_token='b6ugDW2BPyjmJnTGRNl1')

ultrasonic = hcsr04.HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=1000000)
led = machine.Pin(2, machine.Pin.OUT)
buzzer = machine.PWM(machine.Pin(32, machine.Pin.OUT))
buzzer.freq(4186)
buzzer.duty(0)


#CLIENT_NAME = 'freshconsole'
#BROKER_ADDR = '155.133.22.253'
#mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive=60)
#mqttc.connect()
#mqttc.publish(b"iot_topic", b"hello")
client.connect()

while True:
    distance = ultrasonic.distance_cm()
    #mqttc.publish( b"iot_topic", str(distance) )
    # Sending telemetry
    telemetry = {'temperature': distance, 'enabled': False}
    client.send_telemetry(telemetry)
    sleep(0.5)
    print('Distance:', distance, 'cm', '|', distance/2.54, 'inch')
    
    if distance <= 10:
        buzzer.duty(512)
        led.on()
    else:
        buzzer.duty(0)
        led.off()
    time.sleep_ms(1000)