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