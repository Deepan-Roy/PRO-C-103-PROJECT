import sys
import time as tm
import random as rnd
import os
import shutil as stl
import watchdog as wd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler as FSEH
from_dir="C:/Users/mail2/Documents/ESP 8266"
class FileEventHandler(FSEH):
    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created!")
    def on_deleted(self,event):
        print(f"Hey, {event.src_path} has been deleted")
    def on_moved(self,event):
        print(f"Hey, {event.src_path} has been moved")
    def on_modified(self,event):
        print(f"Hey,{event.src_path} has been modified")

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        tm.sleep(2)
        print("Code is Running successfully!")
except KeyboardInterrupt:
    print("The code has stopped running")
    observer.stop()