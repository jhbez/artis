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

from  flask import render_template
from db import drawing, photography

def home_page():
    aw = [
        {
            'imgSrc': '/static/images/cover.jpg',
            'captionText': "I'm artist, showing in art those that many hide, those who know and do not speak, see it and do not show",
        }
    ]
    
    a = drawing.Drawing().get_all(limit=1)
    if len(a) and len(a[0].artworks):
        a = a[0]
        aw.append({
            'imgSrc': "/drawing/image/{}/{}".format(a.id, a.artworks[0].name),
            'captionText': "Artwork is the concep"
        })

    p = photography.Photography.get_all(limit=1)
    if len(p) and len(p[0].artworks):
        p = p[0]
        aw.append({
            'imgSrc': "/photography/image/{}/{}".format(p.id, p.artworks[0].name),
            'captionText': "It is not the camera or the lens, it is the right time to take a picture"
        })
    return render_template("index.html", artworks = aw);