import tkinter as tk
import time
import threading

class EMUAIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EMUAI Emulator")
        self.geometry("320x240")  # Set the window to the size of the image
        self.bootup_messages = [
            "Loading image... Super Mario 64 (USA).z64",
            "Done!",
            "Initializing plug-ins...",
            "Personalizer Plug-in v1.9",
            "Debugger v1.2",
            "Done!",
            "boot..."
        ]
        self.create_bootup_screen()
        self.after(1000, self.run_bootup_sequence)

    def create_bootup_screen(self):
        self.canvas = tk.Canvas(self, width=320, height=240)
        self.canvas.pack()
        self.text_id = self.canvas.create_text(
            160, 120, 
            text="", 
            fill="white", 
            font=('TkDefaultFont', 10),
            anchor="center"
        )
        self.canvas['bg'] = 'black'

    def update_bootup_text(self, message):
        self.canvas.itemconfig(self.text_id, text=message)

    def run_bootup_sequence(self):
        for message in self.bootup_messages:
            self.update_bootup_text(message)
            self.update()  # Force the window to update
            time.sleep(1)  # Wait a second before the next message
        self.after(1000, self.show_emulator_gui)

    def show_emulator_gui(self):
        # Hide the bootup screen
        self.canvas.pack_forget()
        # Now create the emulator GUI elements
        self.label = tk.Label(self, text="EMUAI Emulator GUI")
        self.label.pack(pady=20)
        # Add other GUI elements here

if __name__ == "__main__":
    app = EMUAIApp()
    app.mainloop()
