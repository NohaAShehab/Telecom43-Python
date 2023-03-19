
""" when you try to open file with write mode --->
if file doesn't exist will try to create it ?"""
try:
    fileobj = open("names.txt", 'w')  # stream-object ---> TextIOWrapper
    # # once you open file with write mode ---> old content will be removed
except Exception as e:
    print(e)
else:
    print(fileobj)
    # fileobj.write('Israa\n')
    # fileobj.write("Aya\n")
    # fileobj.write("Basant\n")

    """ writelines """
    fileobj.writelines(['Ahmed\n', 'Israa\n', 'Basant\n', 'Salma'])

    """ seek position in the file """
    fileobj.seek(10)  # count bytes from the beginning of the file.
    fileobj.write('\nNice to have this course with you.')
    fileobj.write("-usgdfkjyq4iotf")
    fileobj.close()  # close stream -->
    # make sure that the updated are saved to the stream ,
    # security-wise

