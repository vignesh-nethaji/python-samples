# Python File Methods
# Method	Description
# close()	Close an open file. It has no effect if the file is already closed.
# detach()	Separate the underlying binary buffer from the TextIOBase and return it.
# fileno()	Return an integer number (file descriptor) of the file.
# flush()	Flush the write buffer of the file stream.
# isatty()	Return True if the file stream is interactive.
# read(n)	Read atmost n characters form the file. Reads till end of file if it is negative or None.
# readable()	Returns True if the file stream can be read from.
# readline(n = -1)	Read and return one line from the file. Reads in at most n bytes if specified.
# readlines(n = -1)	Read and return a list of lines from the file. Reads in at most n bytes/characters if specified.
# seek(offset,from=SEEK_SET)	Change the file position to offset bytes, in reference to from (start, current, end).
# seekable()	Returns True if the file stream supports random access.
# tell()	Returns the current file location.
# truncate(size=None)	Resize the file stream to size bytes. If size is not specified, resize to current location.
# writable()	Returns True if the file stream can be written to.
# write(s)	Write string s to the file and return the number of characters written.
# writelines(lines)	Write a list of lines to the file.



import io
f = open("test.txt")    # open file in current directory
f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
# f = open("img.bmp",'r+b') # read and write in binary mode

f = io.open("test.txt",mode = 'r',encoding = 'utf-8')

f = io.open("test.txt",encoding = 'utf-8')
# perform file operations
f.close()

try:
   f = io.open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
   
fs = open("test.txt",'w')
fs.write("my first file\n")
fs.write("This file\n\n")
fs.write("contains three lines\n")
fs.close();

f = io.open("test.txt",'r',encoding = 'utf-8')
f.read(4) # read the first 4 data
f.read(4) # read the next 4 data
print(f.read()) # read in the rest till end of file
print(f.tell())    # get the current file position
print(f.seek(0))   # bring file cursor to initial position
print(f.readlines())
#for line in f:
 #   print(line, end='')