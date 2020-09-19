from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", x=8, y=8)


@app.route('/<int:y>')
def index_y(y):
    return render_template("index.html", x=8, y=y)


@app.route('/<int:x>/<int:y>')
def index_x_y(x, y):
    return render_template("index.html", x=x, y=y)


@app.route('/<int:x>/<int:y>/<clr_1>/<clr_2>')
def index_x_y_colors(x, y, clr_1, clr_2):
    return render_template("index.html", x=x, y=y, color_1=clr_1, color_2=clr_2)


if __name__ == "__main__":
    app.run(debug=True)
