import os, re
re_filename = re.compile(r'^(.\S+)*')
re_folder = re.compile(r'[A-Z]:.*')

dict_files = {}
error_list = []
dict_found = {}
list_found = []


def folder_recreator():
    count = 0
    file_containing_data = open("C:\\Users\\kenny\\Desktop\\deleted_files.txt", 'r', encoding='utf-16 LE')
    file_containing_data = file_containing_data.readlines()
    #print(len(file_containing_data))
    for a in range(len(file_containing_data)):
        string = file_containing_data[a]
        filename = re_filename.search(string)
        folder = re_folder.search(string)

        try:
            filename = filename.group()
            folder = folder.group()
        except:
            pass
        try:
            # print(filename.group(), folder.group())
            dict_files[filename] = folder
        except AttributeError:
            error_list.append(string)
            count += 1
    file_dir = r"D:\recover"
    dir_of_files = os.chdir(file_dir)
    file_list = os.listdir(dir_of_files)
    for a in range(len(file_list)):
        filename_folder = file_list[a]
        try:
            # print(file_list[a])
            #print(dict_files[filename_folder])
            print(f"File found: {file_list[a]} located at {dict_files[filename_folder]}")
            file_location_string = dict_files[filename_folder]
            print('a')
            file_location_string = file_location_string[2:]
            print('b')
            dict_found[file_list[a]] = file_location_string
            print('c')
            list_found.append(file_list[a])
        except:
            None
            # print('file not found')
    print(f'files found: {len(list_found)} in folder {file_dir} in a folder containing {len(file_list)} files.')
    print('do you want to continue? Y/N')
    continue_answer = input()
    count_i = 1
    if continue_answer != "Y":
        exit()
    for i in range(len(list_found)):
        print(f'{count_i} out of {len(list_found)} done.')
        count_i += 1
        file_name = list_found[i]
        file_location_name = dict_found.get(file_name)
        print(file_location_name[1:2])
        if file_location_name[1:2] == "?":
            file_location_name = r"\unknown" + str(file_location_name[3:])
        location_of_file = file_dir + "\\sorteret" + str(file_location_name)
        try:
            os.makedirs(location_of_file)
        except FileExistsError:
            pass
        os.rename(file_dir + "\\" + file_name, location_of_file + file_name)





    # print(dict_found)




folder_recreator()