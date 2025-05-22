import os
# Current directory ke sabhi files aur folders dikhao
folder_path = r"D:\project-4-assignments\assignment-01\Online_Class_Project_6_Bulk_File_Re_namer_Python_Project"
items = os.listdir(folder_path)
print(items)

for filename in items:
    if filename.endswith(".txt"):
        old_path = os.path.join(folder_path,filename)
        new_filename = "new" + filename
        new_path = os.path.join(folder_path,new_filename)
        os.rename(old_path,new_path)
        print(f"Renamed: {filename} → {new_filename}")
        
