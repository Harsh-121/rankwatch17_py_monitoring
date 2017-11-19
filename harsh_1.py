import os, psutil
from time import time, sleep

start=time()
while True:
	disk_usage=[]
	cpu_usage=[]
	ram_usage=[]
	sleep(1)
	if int(time()-start)%5==0:
		d=psutil.disk_usage('/').used
		c=psutil.cpu_percent()
		r=psutil.virtual_memory().used
		print "CPU Core :", psutil.cpu_count(), "RAM Usage", r, "Disk Usage", d, "CPU Usage", c
		disk_usage.append(d)
		cpu_usage.append(c)
		ram_usage.append(r)
	if int(time()-start)%30==0 or int(time()-start)%60==0 or int(time()-start)%500==0:
		print "Average Disk :", sum(disk_usage)/len(disk_usage), "Average CPU :", sum(cpu_usage)/len(cpu_usage), "Average RAM :", sum(ram_usage)/len(ram_usage)
	

