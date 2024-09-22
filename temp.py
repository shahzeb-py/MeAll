import time
import sys

def task_1():
    for i in range(5):
        sys.stdout.write(f"Task 1 running: {i + 1}/5\r")
        sys.stdout.flush()
        time.sleep(1)
    print()  # Move to the next line after task 1

def task_2():
    for i in range(5):
        sys.stdout.write(f"Task 2 running: {i + 1}/5\r")
        sys.stdout.flush()
        time.sleep(1)
    print()  # Move to the next line after task 2

# Running tasks
task_1()
task_2()
