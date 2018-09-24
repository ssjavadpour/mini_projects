import webbrowser
import time

i = 1;
while i<=3:
    print("Start the clock - Round ", i, ": %s" % time.ctime())
    time.sleep(10)
    #webbrowser opens system's default webbrowser
    webbrowser.open("https://youtu.be/FtbrwGidqR8")
    print("round ", i, "completed")
    i= i+1
print("Exiting now")
