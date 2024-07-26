from os import rename, listdir

files = listdir("en")
[print(f'\"{file.replace(".ejs", "/")}\",') for file in files]
files = listdir("ro")

# [rename(f"ro/{file}", f"ro/{file.replace(".html", '.ejs')}") for file in files if file.endswith('.html')]

