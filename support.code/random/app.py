import tkinter as tk
import time

class TimestampApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timestamp Recorder")
        
        self.start_time = None
        self.timestamps = []
        
        self.label = tk.Label(root, text="Press the button to record a timestamp", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer, font=("Arial", 12))
        self.start_button.pack(pady=5)
        
        self.record_button = tk.Button(root, text="Record Timestamp", command=self.record_timestamp, font=("Arial", 12), state=tk.DISABLED)
        self.record_button.pack(pady=5)
        
        self.reset_button = tk.Button(root, text="Reset Timer", command=self.reset_timer, font=("Arial", 12))
        self.reset_button.pack(pady=5)
        
        self.timer_label = tk.Label(root, text="Time: 0.00 sec", font=("Arial", 14))
        self.timer_label.pack(pady=5)
        
        self.text = tk.Text(root, height=10, width=40, font=("Arial", 12))
        self.text.pack(pady=10)
        
        self.update_timer()
        
    def start_timer(self):
        self.start_time = time.time()
        self.record_button.config(state=tk.NORMAL)

    def record_timestamp(self):
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            mins = elapsed_time/60
            timestamp = f"Timestamp: {elapsed_time:.2f} /{mins:.2f}mins\n"
            self.timestamps.append(timestamp)
            self.text.insert(tk.END, timestamp)
            self.text.see(tk.END)
            self.start_time = time.time()  # Reset the timer after recording a timestamp
    
    def reset_timer(self):
        self.start_time = None
        self.timer_label.config(text="Time: 0.00 sec")
        self.text.delete(1.0, tk.END)
        self.record_button.config(state=tk.DISABLED)
    
    def update_timer(self):
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            self.timer_label.config(text=f"Time: {elapsed_time:.2f} sec")
        self.root.after(100, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimestampApp(root)
    root.mainloop()
