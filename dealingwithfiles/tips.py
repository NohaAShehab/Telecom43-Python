""" you can open file option r+ """

""" r+ open file for reading and writing ? """

try:
    fileobj=open("telecom.txt", 'r+')
except Exception as e:
    print(e)
    exit()
else:
    print(fileobj)
    print(fileobj.read())
    fileobj.write("\n-----###################-----")
    fileobj.close()  ### when you close  stream ---> save  content to the file