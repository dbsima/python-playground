import webbrowser
import time

break_counts = 0
total_breaks = 3

print "This program started at " + time.ctime()
while break_counts < total_breaks:
	# time.sleep(2*60*60) # wait for 2 hours
	time.sleep(10)
	webbrowser.open('https://www.youtube.com/watch?v=xHRkHFxD-xY')
	break_counts = break_counts + 1
