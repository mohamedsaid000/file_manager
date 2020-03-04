import os
import shutil 
import pathlib




path = os.chdir(r"C:\Users\progl\Downloads")
os.listdir(path) 

image_types = ['.jpg', '.JPG', '.png' ,'.PNG' ,'.jpeg' ,'.JPEG']
   
video_types = ['.mp4', '.mov', '.mpg', '.flv'] 


folder_application = pathlib.Path("applications")
folder_images = pathlib.Path("images")
folder_videos = pathlib.Path("videos")
folder_sql = pathlib.Path("sql files")
folder_zip = pathlib.Path("zip files")

if folder_application.exists ():
    print ("The applications Folder exist")
else:
    newpath = r'C:\Users\progl\Downloads\applications' 
    os.makedirs(newpath) 



if folder_images.exists ():  
    print ("The images Folder exist")
else:
    newpath = r'C:\Users\progl\Downloads\images' 
    os.makedirs(newpath) 


if folder_videos.exists ():  
    print ("The videos Folder exist")
else:
    newpath = r'C:\Users\progl\Downloads\videos' 
    os.makedirs(newpath)    

if folder_sql.exists ():  
    print ("The sql Folder exist")
else:
    newpath = r'C:\Users\progl\Downloads\sql files' 
    os.makedirs(newpath) 

if folder_zip.exists ():  
    print ("The zip Folder exist")
else:
    newpath = r'C:\Users\progl\Downloads\zip files' 
    os.makedirs(newpath)       



for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)

    file_full_name = file_name + file_ext

    final_file = os.path.abspath(file_full_name)


    #image types
    if file_ext == ".jpg":
        final_file = os.path.abspath(file_full_name)
        destination = r'C:\Users\progl\Downloads\images'
        shutil.move(final_file, destination)  
    elif file_ext == ".png":
        final_file = os.path.abspath(file_full_name)
        destination = r'C:\Users\progl\Downloads\images'
        shutil.move(final_file, destination) 
    elif file_ext == ".jpeg":
        final_file = os.path.abspath(file_full_name)
        destination = r'C:\Users\progl\Downloads\images'
        shutil.move(final_file, destination)  
    #image types ends     


    #video types
    elif file_ext == ".mp4":
        final_file = os.path.abspath(file_full_name)
        destination = r'C:\Users\progl\Downloads\videos'
        shutil.move(final_file, destination)  
    elif file_ext == ".mov":
        final_file = os.path.abspath(file_full_name)
        destination = r'C:\Users\progl\Downloads\videos'
        shutil.move(final_file, destination)      
    elif file_ext == ".mpg":
        final_file = os.path.abspath(file_full_name)
        destination = r'C:\Users\progl\Downloads\videos'
        shutil.move(final_file, destination) 
    elif file_ext == ".flv":
        final_file = os.path.abspath(file_full_name)
        destination = r'C:\Users\progl\Downloads\videos'
        shutil.move(final_file, destination) 
    #video types ends


    #zip files
    elif file_ext == ".zip":
        final_file = os.path.abspath(file_full_name)
        destination = r'C:\Users\progl\Downloads\zip files'
        shutil.move(final_file, destination)  

    #zip files
    elif file_ext == ".sql":
        final_file = os.path.abspath(file_full_name)
        destination = r'C:\Users\progl\Downloads\sql files'
        shutil.move(final_file, destination)       

    #applications files
    elif file_ext == ".exe":
        final_file = os.path.abspath(file_full_name)
        destination = r'C:\Users\progl\Downloads\applications'
        shutil.move(final_file, destination)                

  

   

 




