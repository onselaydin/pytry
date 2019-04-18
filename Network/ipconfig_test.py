import subprocess
#proc = subprocess.check_output("ipconfig" ).decode('utf-8')
proc = subprocess.call(["ipconfig", "/all"], shell=True)
print(proc)