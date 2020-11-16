from plyer import notification
import os
import time

def main():
    # Icon must be .ICO format
    icon_path = os.getcwd() + "/warning.jpg"

    while True:
        notification.notify(title="Title 1", message="Content 1", app_icon=None, timeout=3)
        notification.notify(title="Title 02", message="Content 02", app_icon=None, timeout=4)

        time.sleep(10)


if __name__ == "__main__":
    main()

