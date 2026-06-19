import os
from datetime import date

today = date.today()

current_working_directory = os.getcwd()
new_derectory = "new_derectory"

dir_path = os.path.join(current_working_directory, new_derectory)

try:
    os.mkdir(dir_path)
except:
    pass
finally:
    os.chdir(dir_path)
