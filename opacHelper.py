import os
# Locate the directory and files in the directory
# Complete or relative path of the directory
basePath = input("Enter the path of folder: ")
bookList = [
    i for i in os.listdir(basePath)
    if os.path.isfile(os.path.join(basePath, i))
]


# function to encode the text in URL friendly format
def encodeToUrl(s):
    return s.replace(" ", "%20")


# the relative path to be used in KOHA
relativePath = encodeToUrl(input("Enter the relative path: "))
book = '<li><a href="{2}{0}">{1}</a></li>'
html = ""

# for each file: get the file name and create its HTML
for i in bookList:
    inputPrompt = 'Enter the new name of the file or . to use this: {0}\n'.format(
        i.replace(".pdf", ""))
    name = input(inputPrompt)
    if name == ".":
        name = i.replace(".pdf", "")
    html = html + book.format(encodeToUrl(i), name, relativePath) + "\n"

# print the resulting html
print(html)