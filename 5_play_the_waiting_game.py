import random
from datetime import datetime

if __name__ == '__main__':
    target_time = random.randint(0, 10)
    print(f"Your target time is {target_time} seconds.")
    input("--- Please press enter to Begin ---")
    start_time = datetime.now()
    input("--- Please press enter to Stop ---")
    stop_time = datetime.now()
    elapsed_time = (stop_time - start_time).total_seconds()

    if elapsed_time > target_time:
        difference = elapsed_time - target_time
        print(f"Your time was {elapsed_time} s. You were {difference} too slow.")
    elif elapsed_time < target_time:
        difference = target_time - elapsed_time
        print(f"Your time was {elapsed_time} s. You were {difference} too fast.")
    else:
        print("Well done! You pressed Enter exactly on time!")