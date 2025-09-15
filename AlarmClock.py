import pygame
import time

def alarm():
    alarm_clock = input("Enter a time for alarm (HH:MM:SS): ")

    busy = True
    while busy:
        now = time.strftime('%H:%M:%S')
        print(now)
        if alarm_clock == now:
            print("Time's up")
            busy = False
        time.sleep(1)

alarm()


pygame.init()
pygame.mixer.music.load('alarm.mp3')
pygame.mixer.music.play()


answer = input("Enter 'r' to resume; 'p' to pause: ").lower()
while answer not in ['r','p']:
    answer = input("Enter 'r' to resume; 'p' to pause: ").lower()
    pygame.mixer.music.play()
    if answer == 'r':
        pygame.mixer.music.stop()
        alarm()
    elif answer == 'p':
        pygame.mixer.music.pause()



