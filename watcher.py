import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the file to monitor
file = '/Users/andreychernenko/Documents/bp/bp.tex'

command = 'xelatex ' + file


class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == file:
            print(f"File {file} has been modified.")
            print(f"Event type: {event.event_type}")
            print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            print("Standard Output:")
            print(result.stdout)

            print("\nStandard Error:")
            print(result.stderr)

            if result.returncode == 0:
                print("Command executed successfully")
            else:
                print(f"Command failed with return code {result.returncode}")


if __name__ == "__main__":
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)  # Monitor the current directory
    observer.start()
    print('Observer started: listening for file ' + file)

    try:
        while True:
            time.sleep(5)

    finally:
        observer.stop()
        observer.join()
