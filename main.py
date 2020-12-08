from flask import Flask , render_template , request

app = Flask(__name__)

@app.route("/",methods=["GET"])
def HelloWorld():
        return render_template("index.html")
@app.route("/",methods=["POST"])
def HellowRoldPOST():
        name = request.form["name"]
        return "Hello " + name
if __name__ == "__main__":
    app.run()