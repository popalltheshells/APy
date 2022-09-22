import ctypes

user_handle = ctypes.WinDLL("User32.dll") #FindWindowA, GetWindowThreadProcessID
k_handle = ctypes.WinDLL("Kernel32.dll")

######Grabbing handle
lpWindowName = ctypes.c_char_p(input("Window name to kill: ").encode('utf-8'))
hWnd = user_handle.FindWindowA(None, lpWindowName)

#######Grabbing Process ID
lpdwProcessId = ctypes.c_ulong()
#These types is noted as LPDWORD on MSDN, we need to know what c conversion to use, 
#in this case, we use ctypes.c_ulong as denoted on the ctypes github conversion page.

response = user_handle.GetWindowThreadProcessId(hWnd, ctypes.byref(lpdwProcessId))
#print (procid)
#print (lpWindowName)

#OpenProcess
dwDesiredAccess = (0x000F0000 | 0x00100000 | 0xFFF) #dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
procid = lpdwProcessId 
#We have to assign the process ID to the new value of 
#lpdwProcessId because we passed by reference in earlier function. 

hProcess = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, procid)

#TerminateProcess
uExitCode = None
response = k_handle.TerminateProcess(hProcess, uExitCode)
