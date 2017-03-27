import time
import sys

def get_can_message(raw_can_frame):
	can_id = raw_can_frame.split(' ')[4]
	can_data_length = int(raw_can_frame.split(' ')[7].split('[')[1].split(']')[0])
	can_hex_data = raw_can_frame.split(']')[1].strip().split('\n')[0]
	return [can_id,can_data_length,can_hex_data]

def scan_noise():
	noise_ids = []
	startup_moment = time.clock()
	vcanlog_file = open("vcanlog","r")
	for raw_can_frame in vcanlog_file:
		can_frame = get_can_message(raw_can_frame)
		noise_ids.append(can_frame[0])

		if(time.clock() - startup_moment > 0.001 * int(sys.argv[1])):
			return list(set(noise_ids))

if(len(sys.argv) == 1):
	print("Time to scan for noise not provided! Exiting...")
	exit(-1)
noise_ids = scan_noise()
print(noise_ids)
