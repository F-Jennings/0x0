#!/usr/bin/env python3

import os, sys, time, datetime
from fhost import app

os.chdir(os.path.dirname(sys.argv[0]))
os.chdir(app.config["FHOST_STORAGE_PATH"])

files = [f for f in os.listdir(".")]

maxs = app.config["MAX_CONTENT_LENGTH"]

for f in files:
    stat = os.stat(f)
    systime = time.time()
    age = datetime.timedelta(seconds = systime - stat.st_mtime).days

    maxage = 5

    if age >= maxage:
        os.remove(f)
