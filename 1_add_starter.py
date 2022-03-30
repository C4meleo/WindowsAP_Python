import winreg, ctypes

if not ctypes.windll.shell32.IsUserAnAdmin():
   ctypes.windll.user32.MessageBoxW(0, "How tf am I going to screw up your pc if you don't run me as admin ?", "Need Admin privileges", 0)
   exit()

access_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(access_key, "Calc", 0,winreg.REG_SZ, r"C:\Windows\System32\calc.exe")

print("Done")
input()
