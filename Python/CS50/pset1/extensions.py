"""
# implement a program that prompts the user for the name of a file
# output that files media type if the files name ends,
    case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
"""

name = input("File name: ")
name.lower()

if name.endswith("gif"):
    print("image/gif")
if name.endswith("jpg" or "jpeg"):
    print("image/jpeg")
if name.endswith("png"):
    print("image/png")
if name.endswith("pdf"):
    print("application/pdf")
if name.endswith("txt"):
    print("text/plain")
if name.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")
    