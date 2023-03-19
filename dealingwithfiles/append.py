
""" when you try to open file with append mode --->
if file doesn't exist will try to create it ?"""
try:
    fileobj = open("names.txt", 'a')  # stream-object ---> TextIOWrapper
    # # once you open file with write mode ---> old content will be kept ???
except Exception as e:
    print(e)
else:
    print(fileobj)
    fileobj.write('Aisha\n')
    fileobj.write("Aya\n")
    fileobj.write("Esraa\n")

    """ writelines """
    fileobj.writelines(['Ahmed\n', 'Israa\n', 'Basant\n', 'Salma'])

    # """ seek position in the file """
    """ seek function has no effect while openning file with append mode"""
    # fileobj.seek(10)  # count bytes from the beginning of the file.
    fileobj.write('\nNice to have this course with you.')
    # fileobj.close()

