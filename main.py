# -----------------------------------------------------------------------------
# Name:        Dorotivity (main.py)
# Purpose:     Main part of the Dorotivity program; contains the root window.
#
# Author:      Adam Raway
# Created:     31-Oct-2022
# Updated:     31-Oct-2022
# -----------------------------------------------------------------------------

from tkinter import *

# Creating the root window
root = Tk()
root.title('Dorotivity')
root.iconbitmap('Images/Dorotivity.ico')
root.geometry('800x500')


def activateFrame(frame):
    '''
  Activate the selected frame.

  Pack_forget() all frames, then packs the selected frame onto the root window.

  Parameters
  ----------
  frame : Frame
    The frame to be packed onto the root window.

  Returns
  -------
  None
    '''
    pomodoroFrame.pack_forget()
    flowmodoroFrame.pack_forget()
    dataFrame.pack_forget()
    settingsFrame.pack_forget()
    frame.pack(fill="both", expand=1)


# Creating the root window's menu
rootMenu = Menu(root)
root.config(menu=rootMenu)

# Creating items in the root window's menu
pomodoroMenu = Menu(rootMenu)
rootMenu.add_cascade(label='Pomodoro', menu=pomodoroMenu)
pomodoroMenu.add_command(label='Use Pomodoro Timer',
                         command=lambda: activateFrame(pomodoroFrame))

flowmodoroMenu = Menu(rootMenu)
rootMenu.add_cascade(label='Flowmodoro', menu=flowmodoroMenu)
flowmodoroMenu.add_command(label='Use Flowmodoro Timer',
                           command=lambda: activateFrame(flowmodoroFrame))

dataMenu = Menu(rootMenu)
rootMenu.add_cascade(label='Productivity Data', menu=dataMenu)
dataMenu.add_command(label='View Productivity Data',
                     command=lambda: activateFrame(dataFrame))

settingsMenu = Menu(rootMenu)
rootMenu.add_cascade(label='Settings', menu=settingsMenu)
settingsMenu.add_command(label='Update Personal Settings',
                         command=lambda: activateFrame(settingsFrame))

# Create frames for each menu item
pomodoroFrame = Frame(root, width=800, height=500, bg="#e63a2e")
flowmodoroFrame = Frame(root, width=800, height=500, bg="#5e93eb")
dataFrame = Frame(root, width=800, height=500, bg="#51d65f")
settingsFrame = Frame(root, width=800, height=500, bg="#636569")

root.mainloop()
