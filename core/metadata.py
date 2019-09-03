from flask import request

class Metadata:
    
    def facebook(cls, artwork, kind):
        if len(artwork.artworks):
            return """ 
                <meta property="og:image" content="{}" />
                <meta property="og:image:secure_url" content="{}" />
                <meta property="og:image:type" content="image/jpeg" />
                <meta property="og:image:width" content="400" />
                <meta property="og:image:height" content="300" /> 
                <meta property="og:image:alt" content="{}" />
                """.format(
                    cls.get_art_image(artwork, kind),
                    cls.get_art_image(artwork, kind),
                    artwork.name
                )
        return ""
    
    def get_domain(cls,):
        return request.url_root
    
    def get_art_url(cls, artwork, kind):
        return cls.get_domain() + kind + "/" + artwork.id 
    
    def get_art_image(cls, artwork, kind, secure=False):
        image = cls.get_domain() + kind +"/image/"+ artwork.id +"/"+artwork.artworks[0].name
        return image
        
    def twitter(cls, artwork, kind):
        if len(artwork.artworks):
            return"""
                <meta name="twitter:card" content="summary_large_image" />
                <!--<meta name="twitter:site" content="@nytimesbits" />
                <meta name="twitter:creator" content="@nickbilton" />-->
                <meta property="og:url" content="{}" />
                <meta property="og:title" content="{}" />
                <meta property="og:description" content="demo" />
                <meta property="og:image" content="{}" />
                """.format(
                    cls.get_art_url(artwork, kind),
                    artwork.name,
                    cls.get_art_image(artwork, kind)
                )
        return ""