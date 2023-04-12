import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = str(input("Input the path for Tracking File System Events"))
from_dir = r"C:\Users\tarak\Downloads\Downloaded_Files"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"New file, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

    def on_modified(self, event):
        print(f"{event.src_path} has been modified")
    
    def on_moved(self, event):
        print(f"{event.src_path} has been moved to {event.dest_path}")

event_handler = FileEventHandler()

observer = Observer()
observer.schedule(event_handler, from_dir, recursive = True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped!/n Keyboard Interrupt. ")
    observer.stop()
    