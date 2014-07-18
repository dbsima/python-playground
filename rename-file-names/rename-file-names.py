import os

def rename_files():
    current_path = os.path.dirname(os.path.abspath(__file__)) 
    path_to_dir = current_path + '/prank'

    file_list = os.listdir(path_to_dir)

    os.chdir(path_to_dir)
    for file_name in file_list:
        new_name = ''.join([i for i in file_name if not i.isdigit()])
        
        print "The file " + file_name + " is now named " + new_name
        
        os.rename(file_name, new_name)	

    os.chdir(current_path)
rename_files()
