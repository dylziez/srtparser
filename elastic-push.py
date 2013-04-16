from pysrt import SubRipFile
from pprint import pprint
import json
import requests
import glob

# Change paths where applicable
x = glob.glob('/home/elastictest/srt/*.srt') 

for i in x:
	# This needs to change for the srt paths sonwell has as they are numbers (just get a key/val of the numbers)
	subsName = i
	subsName = subsName[:-4]
	subsName = subsName.replace('/home/elastictest/srt/', '')
	# // end needs to change
	subs = SubRipFile.open(i)
	for i, val in enumerate(subs):
		d = {}
		d['title'] = subsName
		h = str(subs[i].start.hours).zfill(2)
		m = str(subs[i].start.minutes).zfill(2)
		s = str(subs[i].start.seconds).zfill(2)
		ms = str(subs[i].start.milliseconds).zfill(3)
		hms = '%s:%s:%s,%s' % (h, m, s, ms)
		d['startTime'] = hms
		h = str(subs[i].end.hours).zfill(2)
		m = str(subs[i].end.minutes).zfill(2)
		s = str(subs[i].end.seconds).zfill(2)
		ms = str(subs[i].end.milliseconds).zfill(3)
		hms = '%s:%s:%s,%s' % (h, m, s, ms)
		d['endTime'] = hms
		d['text'] = subs[i].text
		headers = {'content-type': 'application/json'}
		r = requests.post("http://192.168.1.48:2600/subtitles/subtitle/", data=json.dumps(d), headers=headers)
		print "Inserted row for "+subsName
