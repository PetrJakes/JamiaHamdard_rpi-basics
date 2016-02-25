import RPi.GPIO as GPIO

GPIO.setmode( GPIO.BOARD )
GPIO.setup( 13, GPIO.OUT )
GPIO.setup( 15, GPIO.OUT )

try:

	while True:

		GPIO.output( 13, 0 )
		GPIO.output( 15, 1 )

except KeyboardInterrupt:
	
	GPIO.cleanup()


