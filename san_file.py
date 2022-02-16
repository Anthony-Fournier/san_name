import os

def cleanFilename(sourceString,  removeString =" %:/,\\[]'()'<>*?"):
    return ''.join([c for c in sourceString if c not in removeString])

path = input("Full folder path:")
 
directory_list = os.listdir(path)
  
for f in directory_list:
    
        dst = cleanFilename(f)
        os.rename (path + f, path + dst)
