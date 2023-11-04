import os

# to interact with uderlying operating system

# cwd = os.getcwd()
# print("current working directory", cwd)
# f = open("sample.txt",'w')
# f.close()
#
# os.chdir("D:\practise_code")
# f = open("sample2.txt",'w')
# f.close()
#
# print(os.getcwd())

# list_dirs = os.listdir("D:/practise_code")
# # list outs the content from the current directory
# print(list_dirs)

# mkdir and makedirs

# os.chdir("D/practise_code")

# os.mkdir("test_folder1")        # make folder or directory
#
# os.makedirs("first_level/second_level/third_level")


# rmdir=== removedirs

# os.rmdir("test_folder1")

# os.removedirs("first_level/second_level/third_level")

#
# rename
# os.rename("sample.txt", "example.txt")

# stat=== give stats of file

stat = os.stat("datetime_example.py")
print(stat)
print(stat.st_size)
print(stat.st_ctime)
print(stat.st_mtime)

# print(os.environ)
#
if "windows" in os.environ.get("OS").lower():
    print("welcome Windows User")

# print(os.path.join(os.getcwd()))

# print(os.path.isdir("test_folder"))
# print(os.path.isdir("main.py"))






