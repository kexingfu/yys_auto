import win32gui

hwnd = win32gui.FindWindow("Qt5QWindowIcon","MuMu模拟器")
win32gui.MoveWindow(hwnd,20,20,405,756,True)