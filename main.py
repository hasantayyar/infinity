from flask import Flask,render_template
import core
app = Flask(__name__)

@app.route("/map/")
def siemap_index():
	return sitemap("")

@app.route("/map/<path:x>")
def sitemap(x):
	elrange = range(ord("a"),ord("z"))+range(ord("A"),ord("Z"))
	return render_template("sitemap.html",title=x,links=[x+chr(c) for c in elrange])

@app.route("/")
def index():
    return generator("Hello")

@app.route("/<path:x>")
def generator(x):
    return render_template("content.html",title=x,content=core.generate(x))

if __name__ == "__main__":
    app.run(debug=True)
