import os.path
import time

# Задача 1

file_names = [r'D:\Python212\Python\21homework_python\21.txt', r'D:\Python212\Python\21homework_python\22.txt']

with open(r'D:\Python212\Python\21homework_python\output.txt', 'w') as outfile:
    for file_name in file_names:
        with open(file_name) as infile:
            for line in infile:
                outfile.write(line)

with open(r'D:\Python212\Python\21homework_python\output.txt') as f:
    print(f.read())

# Задача 2

# file_path = r'D:\Python212\Python\21homework_python\test.txt'
# # file_path = r'test.txt'
#
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     atime = os.path.getmtime(file_path)
#     print(f"{name} ({dirs}) - last access time {time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(atime))}")
# else:
#     print(f"File {file_path} does not exist!")
