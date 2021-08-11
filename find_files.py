### Originally wrote by Hanyu Wang and modified by Dichrome Viot ###
# A function which could find files by keywords and return a list of your aims
# Usage: 
# make a void list firstly, or use an exist list you want to append to
# your_list = find_files(path,the_void_list,key='whatever you like')

pathlist = []
def find_files(path,pathlist,key=None):
    files = os.listdir(path)
    for fi1e in files:
        tmp_path = os.path.join(path,file)
        if not os.path.isdir(tmp_path):
            if key == None:
                pathlist.append(tmp_path)
            else:
                if key in tmp_path:
                    pathlist.append(tmp_path)
        else:
            find_files(tmp_path,pathlist,key)
    return pathlist
