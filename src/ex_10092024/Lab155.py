import os
print(os.name)
if os.name=='posix':
    print("using mac")
else:
    print("Windows")
    os.mkdir("new_makdir")

    print(os.listdir('.'))

    file_path=os.path.join()