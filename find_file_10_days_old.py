from datetime import datetime
import os 
import datetime

max_age = 10 
current_date = datetime.datetime.now()

for dirpath, direname, filename in os.walk("/etc"):
    for file in filename:
        comp_path = os.path.join(dirpath, file)
        filestat = os.stat(comp_path)
        #print(filestat)
        file_ctime = filestat.st_ctime
       #print(file_ctime)
        file_creation = datetime.datetime.fromtimestamp(file_ctime)
        #print(file_creation)
        diff_in_days = (current_date - file_creation).days
        #print(diff_in_days)
        if diff_in_days > max_age:
            print(f"Print files older than 10 days:", comp_path, diff_in_days)


