import ctypes #importing the ctypes module for data type used by Windows API

user_handle = ctypes.WinDLL("User32.dll") #handle to user32.dll
k_handle = ctypes.WinDLL("Kernel32.dll") #handle to kernel32.dll

hWnd = None #Handle not needed as per microsoft documentation
lpText = "Hello World" #The text to show on message box
lpCaption = "Hello all" #Text to show as a title of the message box
uType = 0x00000001 #Different types of message box as per Microsoft documentation

response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType) #Calling the API MessageBoxW
error = k_handle.GetLastError() #Getting last error message if any

if error !=0: #If there is an error, then print the error message.
    print("Error code".format(error))
    exit(1)
