import os 
import random
p = r"C:\Users\Asus\OneDrive\Desktop\Movies "
os.chdir(p)
folder_name = random.choice(os.listdir())
folder_path = os.path.realpath(folder_name)
os.chdir(folder_path)
file_name = random.choice(os.listdir(folder_path))
print("enjoy!!")
os.startfile(file_name)

