from flask import Flask, render_template, request, redirect, url_for, session
from app.main import generateImg

# Initializing a Flask app
app = Flask(__name__)
app.secret_key = "key"  

# Defining a route for the home page
@app.route("/")
def home():
    return render_template("base.html")

# Defining a route for generating an image
@app.route("/generate", methods=["POST", "GET"])
def generate():
    prmpt = ""
    sz = ""
    if request.method == "POST":
        if request.form["prompt"] and request.form["size"]:  # Checking if the required form data is present
            prmpt = request.form["prompt"]
            sz = request.form["size"]
            session["prompt"] = prmpt # removing data from the session
            session["size"] = sz
            
            return redirect(url_for("success"))
    
    # Redirecting to the home route if the required form data is not present
    return redirect(url_for("home"))
        
    
    
@app.route("/success")
def success():
    if "prompt" in session:
        prmpt = session["prompt"]
        sz = session["size"]
        url = generateImg(prmpt, sz)
        session.pop("prompt", None)  
        session.pop("size", None)

        return render_template("index.html", imgUrl = url) # Rendering the success template with the image URL
    else:
        return redirect(url_for("home")) # Redirect to the home route of prompt text is not present in the session 

# run the app
if __name__ == "__main__":
    app.run()
