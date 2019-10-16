#   Copyright 2019, Joinher
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import os
import hashlib
from datetime import datetime

def file_dir_exists(path):
    return os.path.exists(path)

def dirname2date(dt):
    return datetime.strptime(dt, "%d%b%Y")

def get_md5(msg):
    return hashlib.md5(msg.encode('utf-8')).hexdigest()

def ls(path, ttype="dir", ext=".png"):
    folders = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        if ttype == "dir":
            for folder in d:
                folders.append(os.path.join(r, folder))
        else:
             for ffile in f:
                if ext in ffile:
                    folders.append(os.path.join(r, ffile))
    return folders

def lsdir(path):
    return ls(path)

def lsfile(path, ext=".jpg"):
    return ls(path, ttype="file", ext=ext)

def dir_has_files(path):
    for r, d, f in os.walk(path):
        if len(f) == 0:
            return False
        else:    
            return True