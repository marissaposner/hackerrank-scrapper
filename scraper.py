#!/usr/bin/python
# make the categories for which I have to retrieve data in an array
from hr_scrapper import HR_Scrapper
import logging
import threading
import requests
from subprocess import call

logging.basicConfig(filename="logs.txt")
# TRACKS = ['java', 'python', 'tutorials', 'algorithms', 'data-structures', 'mathematics', '10-days-of-statistics', 'c','10-days-of-javascript', 'sql']
TRACKS=['sql']
hr_scrap = HR_Scrapper()
threads = []

for i in TRACKS:
    try:
        # commenting threading for now as error handling has become difficult with it
        # t1 = threading.Thread(target=hr_scrap.get_track, args=(i,))
        # t1.start()
        hr_scrap.get_track(i)
    except Exception as e:
        #raise e
        print('Something went wrong::', str(e))
        logging.warning(e)
        pass

    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
        pass

# call(["node", "notify.js"])
