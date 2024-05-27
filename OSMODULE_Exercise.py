# import os
# i=0
# folders=sorted(os.listdir("C:\\Users\\ashra\\OneDrive\\Desktop\\Python_Learning\\image"))
# for folder in folders:
#     #print(folder)
#     if folder.endswith('.jpg',18,24):
#         i+=1
#         result=folder
#         os.rename("C:\\Users\\ashra\\OneDrive\\Desktop\\Python_Learning\\image/result",f"C:\\Users\\ashra\\OneDrive\\Desktop\\Python_Learning\\image/{i}.png") 
    
        
   # os.rename(f"C:\\Users\\ashra\\OneDrive\\Desktop\\Python_Learning\\image/folder",f"C:\\Users\\ashra\\OneDrive\\Desktop\\Python_Learning\\image/1.png")
# From ChatGPT
# import os

# i = 0
# folder_path = "C:\\Users\\ashra\\OneDrive\\Desktop\\Python_Learning\\image"
# folders = sorted(os.listdir(folder_path))

# for folder in folders:
#     if folder.endswith('.pangi'):
#         i += 1
#         os.rename(os.path.join(folder_path, folder), os.path.join(folder_path, f"{i}.png"))
#     else:
#         print(folder)
#         os.remove(os.path.join(folder_path, folder))
zu=['MS','PHD']
name,rll=zu
print(name)