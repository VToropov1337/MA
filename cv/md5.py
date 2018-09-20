import os
import hashlib


rootdir = os.getcwd()
unique = [] #названия файлов, хэши которых есть в дайджесте
digests = [] #уникальные хэши
dublicate = set()
for root, dirs, files in os.walk(rootdir):
    for name in dirs:
        for filename in files:
            if filename.endswith(".json"):
                hasher = hashlib.md5()
                with open(filename, 'rb') as f:
                    item = f.read()
                    hasher.update(item)
                    a = hasher.hexdigest()
                    if a not in digests:
                        digests.append(a)
                        unique.append(filename)
                        #print(a,' ',os.path.join(root,filename)) #выводит хэш + путь до файла
                    else:
                        if filename not in unique:
                            dublicate.add(filename)


# print(digests) # выводим уникальные хэши
# print(unique) # названия файлов, хэши который есть в дайджесте

for i in dublicate:
    print("Можно удалить файл: ",i)
