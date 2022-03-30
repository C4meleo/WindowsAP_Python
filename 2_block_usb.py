import winreg

access_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Services\USBSTOR", 0, winreg.KEY_SET_VALUE)

try:
    winreg.SetValueEx(access_key,"Start", 0, winreg.REG_DWORD, 4)
except Exception as e:
    print(e)

print("Done")
input()