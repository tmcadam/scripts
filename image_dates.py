
from os import listdir, utime
from os.path import isfile, join
from PIL import Image
from datetime import datetime, timedelta
import time
import piexif
import sys

mypath = sys.argv[1]
start_time = datetime(2017, 12, 30, 11, 0, 0)
interval = timedelta(seconds=20)
onlyfiles = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]

curr_time = start_time
for f in sorted(onlyfiles):
    #change Exif using PIL and piexif
    im = Image.open(f)
    exif_dict = {"Exif": {}}
    if "exif" in im.info:
        exif_dict = piexif.load(im.info["exif"])
    exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = curr_time.strftime("%Y:%m:%d %H:%M:%S")
    exif_bytes = piexif.dump(exif_dict)
    im.save(f, exif=exif_bytes)
    #change accessed and modified in filesystem
    t = time.mktime(curr_time.timetuple())
    utime(f,(t, t))
    #increment time
    curr_time += interval
