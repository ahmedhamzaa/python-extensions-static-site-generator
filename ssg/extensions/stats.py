from ssg import hooks
import time

start_time=None
total_written=0

def start_build():
    global start_time
    start_time=time.time()
