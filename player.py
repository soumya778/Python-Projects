import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        
        self.current_song = ""
        self.paused = False
        
        self.create_widgets()
    
    def create_widgets(self):
        # Song selection button
        self.select_button = tk.Button(self.master, text="Select Song", command=self.select_song)
        self.select_button.pack(pady=10)
        
        # Play/Pause button
        self.play_button = tk.Button(self.master, text="Play", state=tk.DISABLED, command=self.toggle_play_pause)
        self.play_button.pack(pady=10)
        
    def select_song(self):
        filetypes = (("MP3 files", "*.mp3"), ("All files", "*.*"))
        song_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Song", filetypes=filetypes)
        
        if song_path:
            self.current_song = song_path
            self.play_button.config(state=tk.NORMAL)
    
    def toggle_play_pause(self):
        if not self.current_song:
            return
        
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.current_song)
            pygame.mixer.music.play()
            self.play_button.config(text="Pause")
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
            self.play_button.config(text="Pause")
        else:
            pygame.mixer.music.pause()
            self.paused = True
            self.play_button.config(text="Play")

if __name__ == "__main__":
    pygame.mixer.init()
    
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
    
    pygame.mixer.quit()
