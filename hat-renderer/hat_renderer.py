import time
import json
import atexit

from dotstar import Adafruit_DotStar

NUM_PIXELS = 240

DATA_PIN = 23
CLOCK_PIN = 24
ANIMATION_PATH = "/opt/hat_server/animations/"
STATUS_FILE = "{}current.status".format(ANIMATION_PATH)

hat = Adafruit_DotStar(NUM_PIXELS, DATA_PIN, CLOCK_PIN, order='bgr')

hat.begin()
hat.setBrightness(16)


while True:

    status = None
    with open(STATUS_FILE, 'r') as statusfile:
        status = json.loads(statusfile.read())

    if (status['type'] == "off"):
        hat.clear()
        hat.show()
        time.sleep(2)
        continue
    
    annimation = None
    animation_file = "{}{}.json".format(ANIMATION_PATH, status['name'])
    with open(animation_file, 'r') as infile:
        annimation = json.loads(infile.read())

    fps = 1
    for frame in annimation['frames']:
        # munge frame array into list of pixels
        frame_width = len(frame)
        frame_height = len(frame[0])
        pixel_index = 0
        for y in range(frame_height - 1, -1, -1):
          for x in range(0, frame_width):
            pixel = frame[x][y].split(",")
            hat.setPixelColor(pixel_index, int(pixel[0]), int(pixel[1]), int(pixel[2]))
            pixel_index += 1
        hat.show()
        time.sleep(1.0/fps)


@atexit.register
def shutdown():
    hat.clear()
    hat.show()
