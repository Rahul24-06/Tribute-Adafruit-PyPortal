import time
import board
from adafruit_pyportal import PyPortal

# Set up where we'll be fetching data from
# DATA_SOURCE = "https://www.adafruit.com/api/quotes.php"
# QUOTE_LOCATION = [0, 'text']
# AUTHOR_LOCATION = [0, 'author']
a1 = 'a1.bmp'
a2 = 'a2.bmp'
a3 = 'a3.bmp'
a4 = 'a4.bmp'
a5 = 'a5.bmp'

while True:	
	# the current working directory (where this file is)
	 cwd = ("/"+__file__).rsplit('/', 1)[0]
	 pyportal = PyPortal(status_neopixel=board.NEOPIXEL)

	# pyportal.play_file(audio)
	# speed up projects with lots of text by preloading the font!
	 pyportal.preload_font()
	 pyportal.set_backlight(1.00)
	 i = 2

	 # disp
	 pyportal.set_background(a1)
	 board.DISPLAY.refresh_soon()
	 board.DISPLAY.wait_for_frame()
	 time.sleep(i)

	 pyportal.set_background(a2)
	 board.DISPLAY.refresh_soon()
	 board.DISPLAY.wait_for_frame()
	 time.sleep(i)

	 pyportal.set_background(a3)
	 board.DISPLAY.refresh_soon()
	 board.DISPLAY.wait_for_frame()
	 time.sleep(i)

	 pyportal.set_background(a4)
	 board.DISPLAY.refresh_soon()
	 board.DISPLAY.wait_for_frame()
	 time.sleep(i)

	 pyportal.set_background(a5)
	 board.DISPLAY.refresh_soon()
	 board.DISPLAY.wait_for_frame()
	 time.sleep(i+5)
#    try:
#        value = pyportal.fetch()
#       print("Response is", value)

#    except RuntimeError as e:
#        print("Some error occured, retrying! -", e)