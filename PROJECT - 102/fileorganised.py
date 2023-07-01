import os , shutil

from_dir = "C:/Users/SANDHYA PASIKANTI/Downloads"
to_dir = "D:/Downloads-segr"

list_d = os.listdir(from_dir)

for file in list_d :
     name , ext = os.path.splitext(file)
     
     if ext == "" :
         continue
     
     if ext in [".pdf" , "jpeg" , ".txt" , ".jpg" , ".png" , ".docx"]:
         source = from_dir + "/" + file
         dstfldr = to_dir + "/" + ext
         dst = to_dir + "/" + ext + "/" + file
         
         if os.path.exists(dstfldr):
             shutil.copy(source , dst)
             
         else :
             os.mkdir(dstfldr)
             shutil.move(source , dst )
             
       
     