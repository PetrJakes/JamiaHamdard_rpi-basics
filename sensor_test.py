import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:

	while True:
	
		i = GPIO.input( 3 )
	
		if i == 0:

			print( 'Obstacle Detected on right' , i )
			time.sleep( 0.1 )

		j = GPIO.input( 16 )
	
		if j == 0:

			print( 'Obtacle detected on left' , j )
			time.sleep( 0.1 )

except KeyboardInterrupt:

	GPIO.cleanup()
