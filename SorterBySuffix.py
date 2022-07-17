import os
import shutil

scriptfile = os.path.abspath(__file__)
script_path, scriptname = os.path.split(scriptfile)
all_files = os.listdir(script_path)

for file in all_files:
    filename, file_suffix = os.path.splitext(script_path + file)
    
    
    #Создание папок с новыми расширениями 
    try:
        if file != scriptname:
            os.mkdir(script_path + "/" + file_suffix[1:].upper())
    except FileExistsError:
        pass

    # Сортировка файлов по созданным папкам
    path_destination = script_path + '/' + file_suffix[1:].upper()
    if path_destination != script_path:
        try:
            print(file)
            if file != scriptname:
                print(path_destination)
                shutil.move(script_path + "/" + file,path_destination)
        except shutil.Error:
            pass
    
 

