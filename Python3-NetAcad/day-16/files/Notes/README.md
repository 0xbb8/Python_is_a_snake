'''		'''
Processing Files
'''		'''

1) Files are represented differently in Unix/Linux and Windows systems.
2) Canocial File name: File name that uniquely defines the location of the file regardless the location of the said file in the directory tree.
3) File names in Unix/Linux are case sensitive but not in the windows systems.
4) File seperators in Unix/Linux is '/' but '\' in Windows.

Python is able to convert / to \ when it is required by the OS.
i.e. Any of the following assessments will work on Windows system.
###
dir = '/dir/file'
dir = 'cd:/dir/file'
###

# Python programs communicate with files indirectly through abstract entities known as 'handles' or 'streams'

To connect (bind) the stream with the file, it's necessary to perform an explicit operation.
The operation of connecting the stream with a file is called opening the file, while disconnecting this link is named closing the file.
# Conclusion: The first and last operation performed on the stream are 'open' and 'close' respectively.
# Opening of stream fails when:
	1) File with the name doesn't exist.
	2) Number of streams is limited by the OS.
	3) Permission issue

--- 
File Streams 
---
Two basic operations performed on the string:
1) read: portions of data from the file to a memory location
3) write: portions of data from a memory location to the file.

---
Three basic modes to open the stream
---
1) read mode: read only operations are permitted or exception is raised :UnsupportedOperation:->:OSError:->:ValueError: from the io module.
2) write mode: write only operations are permitted.
3) update mode: both read and write operations are permitted.

---
File Handles
---
* Python assumes that every file is hidden behind an object of adequate class.
* An object of adequate class is created when you open the file and annihilate it at the time of closing.
The Object comes from one of the classes below:

---
IOBase : RawIOBase, BufferedIOBase, TextIOBase
---
* An object of this class is not instantiated by constructors but by invovation of the functions 'open()' and 'close()' to get rid of the object.

* All streams are divided into text or binary streams.
-> Text: arranged line by line (read mostly character by character/line by line)
-> Binary: sequence of bytes (read/written byte by byte / block-by-block:block can be defined)

Problem is presesnted:
* Unix/Linux: Line ends are marked by a single Char named 'LF' (ASCII:10) equivalent of Python's \n
* Windows: They are marked by a pait of chars named 'CR' and 'LF' (ASCII:13 and 10) equivalent of Python's \r\n
---
This makes the Programs non-portable.
---
Resolve: Translation of new-line characters.
---

* Opening of a stream:
	stream = open(file, mode = 'r', encoding = None)

Opening Streams : Modes
---
r -> read mode; if no file:raise exception
w -> write mode; if no file:create file; if file exists:truncate to length of Zero(erase)
a -> append mode; if no file:create file; if file exists:untouch file-move virtual recording header to the end
r+ -> read and update mode; file == exists and file == writable; read and write operations are allowed.
w+ -> write and update mode; if no file:create file else:update file(untouch contents); read and write ops are allowed.

---
Text mode(t)	Binary mode(b)	Description
---

   rt		   rb		read
   wt		   wb		write
   at		   ab		append
   r+t		   r+b		read and update
   w+t		   w+b		write and update

---
NOTE: You can use 'x' mode for the exclusive creation and opening of file. But if file exists:raises exception
---

There are three well-defined streams already open: You can check them out using the 'sys' module.
-> sys.stdin: Associated with Keyboard : input() : (Standard Input)
-> sys.stdout: With Screen : print() : (Standard Output)
-> sys.stderr: With Screen: (Standard Error Output)

* stream.close() - closes the stream: if it fails (rarely), it raises IOError exception. May happen due to caching or buffering.

::: IOError :::
The IOError exception has a property called 'errno' (error number).

try:
    # stream op code
except Exception as e:
    print(e.errno)

---
Some Constants useful for detecting stream errors
---
**$
errno.EACCES: Permision Denied
errno.EBADF: Bad file number
errno.EEXIST: File Exists
errno.EFBIG: File too large
errno.EISDIR: Is a directory
errno.EMFILE: Too many files
errno.ENOENT : No such file or directory
errno.ENOSPC: No space left on device
$**

*$
 Error handling is simplified by using strerror() function from 'os' module.
 Syntax: strerror(exc.errno) # exc is the exception.
*$

