# -*- coding: utf-8 -*-

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
from core.utils import lsdir, lsfile, dir_has_files, get_md5, dirname2date, file_dir_exists
import json as simplejson

from  db.artwork import Artwork


    
class Drawing(object):
    id = None
    name = None
    path = None
    cover = None
    created_at = None
    artworks = None
    
    PATH = "artwork/drawing/"
    TABLE = "drawing"
    
    def __init__(self):
        self.artworks = []
        
    def __str__(self):
        return("Id:{} Name:{} Path:{} Cover:{} CreateAt: {}, Artworks:{}".format(
            self.id,
            self.name,
            self.path,
            self.cover,
            self.created_at,
            str(self.artworks)
        ))
        
    def to_dict(self):
        _dict = self.__dict__
        _artworks = []
        for a in self.artworks:
            _artworks.append(a.to_dict())
        _dict.update({'artworks':_artworks})
        return _dict
    
    @classmethod
    def get_all(cls, json=False, limit=0):
        path = os.path.join(os.getcwd(),cls.PATH)
        folders = lsdir(path)
        artworks = []
        _limit = 0
        for folder in folders:
            if dir_has_files(folder):
                d = Drawing()
                dir_name = str(folder.rsplit('/',1)[1]).strip()
                d.id = get_md5(dir_name)
                d.path = folder
                dir_name_list = dir_name.split("-")
                d.created_at = dirname2date(str(dir_name_list[0]).strip())
                d.name = str(dir_name_list[1]).strip()
                images = lsfile(folder)
                for image in images:
                    image_name = str(image.rsplit('/',1)[1]).strip()
                    a = Artwork()
                    a.id = get_md5(image_name)
                    a.name = image_name
                    d.artworks.append(a)
                if limit == _limit and limit != 0 :
                    break
                _limit += 1
                if json:
                    artworks.append(d.to_dict())
                else:
                    artworks.append(d)
        return artworks
    
    def get_by_id(cls, id):
        artworks = cls.get_all()
        for artwork in artworks:
            if artwork.id == id:
                return artwork
        return False
            
    def get_image(cls, id, name):
        artworks = cls.get_all()
        for artwork in artworks:
            if artwork.id == id:
                image = os.path.join(artwork.path,name)
                if file_dir_exists(image):
                    return image
        return False
    
    
    