print("Hello World!")

tickets = 10
while tickets > 0:
    print("Sale!")
    tickets = -1

TICKET = 50
TICKET = 31
print(TICKET)

import datetime

# This script simply logs the current date and time
with open("activity_log.txt", "a") as f:
    f.write(f"Commit pulse at: {datetime.datetime.now()}\n")

print("Activity logged successfully!")

name = "Alex"
print(name)

import random
import time

creatures = [
    "Goblin Accountant",
    "Disco Lizard",
    "Haunted Microwave",
    "Cyber Possum",
    "Wizard Crab",
    "Tax Evading Frog",
]

actions = [
    "stole the moon",
    "opened a yogurt shop",
    "challenged a toaster to combat",
    "started beatboxing aggressively",
    "became self aware",
    "ate an ethernet cable",
]

for i in range(4):
    creature = random.choice(creatures)
    action = random.choice(actions)

    print(f"{creature} {action}")

    with open("chaos.txt", "a") as file:
        file.write(f"{creature} {action}\n")

    time.sleep(1)
