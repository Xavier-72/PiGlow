##########################################################
# Custom CPU Activity Monitor ##
# Requires psutil - sudo apt-get install python-psutil ##
# Shifty051 
##########################################################

from piglow import PiGlow
from time import sleep
import psutil

piglow = PiGlow()

while True:
  
  cpu = psutil.cpu_percent()
  piglow.all(0)

  if cpu < 5:
    piglow.red(10)

  elif cpu < 20:
    piglow.red(10)
    piglow.orange(10)

  elif 20 < cpu < 49:
    piglow.red(10)
    piglow.orange(10)
    piglow.yellow(10)

  elif cpu < 60:
    piglow.red(10)
    piglow.orange(10)
    piglow.yellow(10)
    piglow.green(10)

  elif cpu < 80:
    piglow.red(10)
    piglow.orange(`0)
    piglow.yellow(10)
    piglow.green(10)
    piglow.blue(10)

  else:
    piglow.white(20)
    sleep(0.5)
