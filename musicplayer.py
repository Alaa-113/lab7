import pygame
import keyboard
import os
import time

pygame.mixer.init()

music_folder = "music/"
playlist = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
current_track = 0
is_paused = False
music_stopped = False

def play_music():
    global current_track, is_paused, music_stopped
    pygame.mixer.music.load(os.path.join(music_folder, playlist[current_track]))
    pygame.mixer.music.play()
    is_paused = False
    music_stopped = False
    print(f"Playing: {playlist[current_track]}")

def stop_music():
    global is_paused, music_stopped
    pygame.mixer.music.stop()
    is_paused = False
    music_stopped = True
    print("Music Stopped")

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()

if playlist:
    play_music()
else:
    print("No music files found in the folder!")

while True:
    if not pygame.mixer.music.get_busy() and not is_paused and not music_stopped:
        next_track()

    if keyboard.is_pressed("space"):
        time.sleep(0.2)
        if is_paused:
            pygame.mixer.music.unpause()
            is_paused = False
            print("Music Resumed")
        else:
            pygame.mixer.music.pause()
            is_paused = True
            print("Music Paused")

    elif keyboard.is_pressed("s"):
        time.sleep(0.2)
        stop_music()

    elif keyboard.is_pressed("n"):
        time.sleep(0.2)
        next_track()

    elif keyboard.is_pressed("p"):
        time.sleep(0.2)
        prev_track()

    time.sleep(0.1)
