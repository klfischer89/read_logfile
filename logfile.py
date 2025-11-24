import os
import zipfile

if not os.path.exists("./data/syslog"):
    with zipfile.ZipFile("./data/syslog.zip", "r") as z:
        z.extractall("./data/syslog")
    
    
with open("./data/syslog/syslog", mode="r", encoding="utf-8") as file:
    log = file.read()

log_lines = log.split("\n")    

print(len([line for line in log_lines if line != '']))

print(log.count("[UFW BLOCK]"))

print(log.count("SRC=94.102.51.28"))