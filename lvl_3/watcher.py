import subprocess
from watchfiles import watch
import os
import signal
import sys

def run_script():
    """
    Run the target Python script and return the process.
    Adjust the command as necessary.
    """
    return subprocess.Popen(["python", "src/main.py"])

def restart_script(process):
    """
    Restart the target script by terminating the existing process and starting a new one.
    """
    if process:
        process.terminate()
        process.wait()  # Wait for the process to terminate
    print("Detected changes. Restarting script...")
    return run_script()

if __name__ == "__main__":
    # Initial run of the target script
    process = run_script()

    try:
        for changes in watch('./src'):
            # If changes are detected in the ./src directory, restart the script
            process = restart_script(process)
    except KeyboardInterrupt:
        # Handle graceful exit upon receiving a KeyboardInterrupt (Ctrl+C)
        print("Stopping watcher...")
        if process:
            process.terminate()
            process.wait()
        sys.exit(0)