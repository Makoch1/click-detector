import csv
from datetime import datetime
import os
from pynput import mouse

# Define the output CSV file name
CSV_FILE = "mouse_clicks_log.csv"

def init_csv():
  if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
      writer = csv.writer(f)
      writer.writerow(
          ["Username", "Timestamp"]
      )

def on_click(x, y, button, pressed):
  if pressed:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
      writer = csv.writer(f)
      writer.writerow([participant, timestamp])

    print(f"\nLogged click for '{participant}' at {timestamp}")

    return False # stop listner loop


if __name__ == "__main__":
  participant = input("Enter participant id / name: ").strip()

  if not participant:
    participant = "anon"

  init_csv()

  print(f"\nWaiting for click ('{participant}')...")

  with mouse.Listener(on_click=on_click) as listener:
    listener.join()
