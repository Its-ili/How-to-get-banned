from time import sleep
from random import randint
from os import system
counter = 1
while counter != 101:
    with open("file.txt", "a+") as f:
        f.write(f"{counter}\n")
    counter += 1
    system("git add .")
    system(f"git commit -m '{counter} day'")
    system("git push")
    print("pushed successfully")
    sleep_time = 24*60*60 + randint(-4,4) * 3600
    print("Sleeping for {} hours".format(sleep_time / 3600))
    sleep(sleep_time)
    system("clear")
