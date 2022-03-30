import winreg, ctypes

if not ctypes.windll.shell32.IsUserAnAdmin():
   ctypes.windll.user32.MessageBoxW(0, "How tf am I going to screw up your pc if you don't run me as admin ?", "Need Admin privileges", 0)
   exit()

access_registry = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
access_key = winreg.OpenKey(access_registry,r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles")

n = 0
while True:
   try:
      guid = winreg.EnumKey(access_key,n)
      key = winreg.OpenKey(access_registry,r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles\\"+guid)
      name = winreg.EnumValue(key, 0)[1]
      print(name)
   except OSError as e:
      if e.errno == 22: break
   except Exception as e:
      print(e)
   
   n += 1

input()
