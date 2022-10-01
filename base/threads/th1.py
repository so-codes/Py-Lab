# import the threading module
import threading
class thread(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID
    # helper function to execute the threads
    def run(self):
        print(str(self.thread_name) +" "+ str(self.thread_ID))


thread1 = thread("STUDY", 1000)
thread2 = thread("STUDY", 2000)
thread1.start()
thread2.start()
print("Exit")