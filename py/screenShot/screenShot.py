import pyautogui
import tkinter as tk

myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'C:\Users\Administrator\Desktop\screenshot.png')

root = tk.Tk()
root.title('Sc taker')

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def myscreenshot():
    myscreenshot = pyautogui.screenshot()
    myScreenshot.save(r'C:\Users\Administrator\Desktop\screenshot1.png')


myButton = tk.Button(text='Take Screenshot', command=myScreenshot, bg='green', fg='white', font=15)
canvas1.create_window(150, 150, window=myButton)

root.mainloop()
