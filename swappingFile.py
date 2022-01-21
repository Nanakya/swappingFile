def swapFileData():
    file1=input("enter file name:")
    file2=input("enter the file name to swap with:")
    with open(file1, 'r') as a:
        data_a=a.read()
    with open(file2, 'r') as b:
        data_b=b.read()
    with open(file1, 'w') as a:
        data_a=a.read()
    with open(file2, 'w') as b:
        data_b=b.read()
swapFileData()