import tkinter as tk
from datetime import datetime, timedelta

class StopWatch:
    def __init__(self, master):
        self.master = master
        self.master.title("Stopwatch")
        self.time_var = tk.StringVar()
        self.time_var.set("00:00:00.000")
        self.time_label = tk.Label(self.master, textvariable=self.time_var, font=("Helvetica", 30))
        self.time_label.pack()
        self.start_button = tk.Button(self.master, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT)
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT)
        self.running = False
        self.elapsed_time = timedelta()

    def update_time(self):
        if self.running:
            self.elapsed_time += timedelta(milliseconds=100)
        time_str = str(self.elapsed_time).split(".")[0].zfill(8) + "." + str(self.elapsed_time.microseconds)[:3]
        self.time_var.set(time_str)
        self.master.after(100, self.update_time)

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def reset(self):
        self.elapsed_time = timedelta()
        self.time_var.set("00:00:00.000")

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("300x100")
    stopwatch = StopWatch(root)
    stopwatch.update_time()
    root.mainloop()
