import time
import random
import tkinter as tk

class SpeedTypingTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Speed Typing Test")
        
        self.sentence = "The quick brown fox jumps over the lazy dog."
        self.current_sentence = ""
        self.start_time = None
        
        self.create_widgets()
    
    def create_widgets(self):
        self.sentence_label = tk.Label(self.master, text=self.sentence, font=("Arial", 12), wraplength=400)
        self.sentence_label.pack(pady=10)
        
        self.text_entry = tk.Entry(self.master, font=("Arial", 12))
        self.text_entry.pack(pady=10)
        
        self.text_entry.bind('<Return>', self.check_sentence)
        
    def check_sentence(self, event):
        user_input = self.text_entry.get()
        
        if self.start_time is None:
            self.start_time = time.time()
        
        if user_input == self.sentence:
            elapsed_time = time.time() - self.start_time
            words_typed = len(user_input.split())
            typing_speed = words_typed / elapsed_time * 60
            
            result_text = f"Time elapsed: {elapsed_time:.2f} seconds\n"
            result_text += f"Words typed: {words_typed}\n"
            result_text += f"Typing speed: {typing_speed:.2f} words per minute"
            
            result_label = tk.Label(self.master, text=result_text, font=("Arial", 12))
            result_label.pack(pady=10)
            
            self.text_entry.unbind('<Return>')
        else:
            self.text_entry.delete(0, tk.END)
            self.text_entry.insert(tk.END, "Incorrect! Try again.")
            self.text_entry.configure(fg="red")
            self.master.after(1500, self.clear_entry)
    
    def clear_entry(self):
        self.text_entry.delete(0, tk.END)
        self.text_entry.configure(fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTypingTest(root)
    root.mainloop()
