

""" save --> data simple text files  =txt files= // json // databases """

"""
    file modes  ---> read , write , append 
    read ==> read file content 
    write ---> remove old content --> open file for write starting from the beginning of the file 
    append --> keep old content ---> open file for writing starting from the end of the file 
    
    ### open (filename, mode ) ---> mode r ---> read , mode w ==> write , mode ---> append
    
    ### operation  ---> 
    --> read content form the file 
    --> write content to the file 
    --> close the file 
"""

""" read content the file """

# fileobj =open("mycv.txt", 'r')  #steamobject ---> TextIOWrapper
# print(fileobj)

""" use try ---> except mandetory """

try:
    fileobj = open("mycv.txt", 'r')  # stream-object ---> TextIOWrapper
except Exception as e:
    print(e)
else:
    print(fileobj)
    """--- read file content from the beginning of the file ---"""
    # data = fileobj.read()  # read content of the file into one string
    # print(data, type(data))
    #

    """ fileobject ---> refer bytes 000> in file """
    # lines = []
    # for line in fileobj:  # expect that \n ---> means the end of this line
    #     # print(f"line={line}")
    #     lines.append(line)

    """ read file line by line """
    # lines = fileobj.readlines()
    # print(lines)

    """ move cursor of the file to the 10th byte."""
    # fileobj.seek(8)
    # print(f"data ={fileobj.read()}#")
    """ read part of the file """
    # fileobj.seek(8)
    # print(f"data ={fileobj.read(10)}#")
    # # read you can specify the number of bytes you want to read.

    """ example """
    # fileobj.seek(1000)
    # print(f"data={fileobj.read()}#")

    """ another example"""
    data = fileobj.read()  # after this operation --> cursor --> at the end of the file .
    print(f"data={data}#")
    ## you need to move the file cursor again to the beginning of the database
    # fileobj=open("mycv.txt")  # default --> open
    fileobj.seek(0)
    lines = fileobj.readlines() # empty lines
    ll=[]
    ll.append(lines)
    print(ll)
    """close filestream  """
    fileobj.close()
