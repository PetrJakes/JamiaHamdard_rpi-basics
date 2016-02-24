import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BOARD )
GPIO.setup( 12, GPIO.OUT )

count = 15

while count > 0 :

	GPIO.output( 12, 1 )
	time.sleep( 0.5 )
	GPIO.output( 12, 0 )
	time.sleep( 0.5 )
	count = count - 1

GPIO.cleanup()
