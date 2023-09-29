import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Flashing Square")
        self.geometry('1920x1080')

        self.center_x = self.winfo_screenwidth() // 2
        self.center_y = self.winfo_screenheight() // 2

        self.canvas = tk.Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight(), bg='black')
        self.canvas.pack()

        self.flash_state = False

        self.draw_square()

    def draw_square(self):
        start_x = self.center_x - 50
        start_y = self.center_y - 50
        end_x = self.center_x + 50
        end_y = self.center_y + 50

        if self.flash_state:
            self.square = self.canvas.create_rectangle(start_x, start_y, end_x, end_y, outline='white', fill='white')
        else:
            self.square = self.canvas.create_rectangle(start_x, start_y, end_x, end_y, outline='white', fill='black')
        
        self.flash_state = not self.flash_state
        # 120 beats per minute is 2 beats per second
        # Therefore, the square should flash every 500 milliseconds (half a second) to match this tempo
        self.canvas.after(500, self.update_square)

    def update_square(self):
        self.canvas.delete(self.square)
        self.draw_square()

if __name__ == "__main__":
    Application().mainloop()