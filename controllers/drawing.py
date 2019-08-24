from  flask import render_template, send_file, abort
from db import drawing
from core.metadata import Metadata 

class Drawing:
    NAME = "drawing"
    
    TEMPLATE_PAGE = "drawing.html"
    TEMPLATE_ARTWORK = "artwork.html"
    DB = drawing.Drawing()
    
    def drawing_page(cls):
        artworks = cls.DB.get_all()
        aw = []
        i = 0
        for artwork in artworks:
            aw.append({
                'index': i,
                'artwork': artwork
            })
            if i == 5: # 0,1,2, 3,4 5
                i = -1
            i += 1
        return render_template(cls.TEMPLATE_PAGE, name=cls.NAME, artworks = aw)

    def drawing_artwork_page(cls, id):
        artwork = cls.DB.get_by_id(id)
        metadata = Metadata().facebook(artwork, kind=cls.NAME)
        metadata = metadata + Metadata().twitter(artwork, kind=cls.NAME)
        if artwork:
            return render_template(
                cls.TEMPLATE_ARTWORK, 
                name=cls.NAME, 
                artwork=artwork,
                metadata=metadata,
            )
        return abort(404)

    def drawing_image(cls, id, name):
        image = cls.DB.get_image(id, name)
        if image:
            return send_file(image, mimetype='image/jpg')
        return abort(404)