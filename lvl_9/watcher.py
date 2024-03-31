import subprocess
from watchfiles import watch
import sys

def run_script():
    return subprocess.Popen(["python", "src/main.py"])

def restart_script(process):
    if process:
        process.terminate()
        process.wait()  # Wait for the process to terminate
    print("Detected changes. Restarting...")
    return run_script()

if __name__ == "__main__":
    process = run_script()
    try:
        for changes in watch('./src'): # IF changes are detected...
            process = restart_script(process) # THEN restart script
    except KeyboardInterrupt:
        print("Stopping watcher...")
        if process:
            process.terminate()
            process.wait()
        sys.exit(0)