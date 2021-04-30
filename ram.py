import psutil
import time

while True:
	if psutil.virtual_memory().percent > 90:
		try:
			print("Ram is now ",psutil.virtual_memory().percent)

			high = 0
			pid = 0

			for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
				vms = proc.memory_info().vms
				if vms > high:
					high = vms
					pid = proc.pid

			print("killed pid",pid)

			psutil.Process(pid).terminate()
			time.sleep(10)
			
		except:
			pass

