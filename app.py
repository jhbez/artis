from flask import Flask, abort, render_template
from controllers import home, drawing, photography

app = Flask(__name__)

@app.route("/")
def _home():
    return home.home_page()

# Route Drawing
@app.route("/drawing")
def _drawing():
    return drawing.Drawing().drawing_page()

@app.route("/drawing/<string:id>")
def _drawing_artwork(id):
    return drawing.Drawing().drawing_artwork_page(id)

@app.route("/drawing/image/<string:id>/<string:name>")
def _drawing_image(id, name):
    return drawing.Drawing().drawing_image(id, name)

#Route Photography
@app.route("/photography")
def _photography():
    return photography.Photography().drawing_page()

@app.route("/photography/<string:id>")
def _photography_artwork(id):
    return photography.Photography().drawing_artwork_page(id)

@app.route("/photography/image/<string:id>/<string:name>")
def _photography_image(id, name):
    return photography.Photography().drawing_image(id, name)


if __name__ == "__main__":
    app.config.from_pyfile("app.cfg")
    app.run()