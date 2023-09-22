import os

def search_path(keyword):
    found_paths = []
    for folders, subfolders, files in os.walk('C:/Users/user/OneDrive/Desktop/'):
        for name in subfolders:
            if keyword in name:
                found_paths.append(os.path.join(folders, name))
        for name in files:
            if keyword in name:
                found_paths.append(os.path.join(folders, name))
    return found_paths
keyword = input("Search for: ")
results = search_path(keyword)
if len(results) > 0:
    print("I founded:\n")
    for path in results:
        print(path)
else:
    print("I can't found")
