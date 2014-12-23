import Tkinter
import ttkcalendar

import tkSimpleDialog

class CalendarDialog(tkSimpleDialog.Dialog):
    """Dialog box that displays a calendar and returns the selected date"""
    def body(self, master):
        self.calendar = ttkcalendar.Calendar(master)
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.selection
        
# Demo code:
def main():
    root = Tkinter.Tk()
    root.wm_title("CalendarDialog Demo")
    
    def onclick():
        cd = CalendarDialog(root)
        print cd.result

    button = Tkinter.Button(root, text="Click me to see a calendar!", command=onclick)
    button.pack()
    root.update()

    root.mainloop()
    

if __name__ == "__main__":
    main()
