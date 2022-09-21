import ctypes
#Opening a handle to a specific process (using process ID)

k_handle = ctypes.WinDLL("Kernel32.dll") #Alias to open the DLL which the API resides in

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)

dwDesiredAccess  = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessID = 0x1E40 #The process you want to open a handle to (can be checked through task manager), all process ID must first be coverted to hex

response = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessID) #To cal the windows API
error = k_handle.GetLastError()

print (response)
