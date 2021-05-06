from datetime import datetime
from time import sleep

if __name__ == '__main__':
    t0 = datetime.now()
    try:
        while True:
            t = datetime.now()
            print(t-t0)
            sleep(1)
    except KeyboardInterrupt:
        print("\nFinished:", datetime.now() - t0)
