from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

friends_dict = [
    {"Name": "Test", "Favorite Sport": "Football", "Do You Stream": "yes", "Favorite Streaming Servce": "ESPN"}
]


###### Custom Error Pages ######
# Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404


# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Web form template", friends=friends_dict
    )

 
@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        fname = form["fname"]
        sport = form["sport"]
        stream = form["stream"]
        favorite = form.getlist("favorite")  # this is a PYthon list

        print(fname)
        print(sport)
        print(stream)
        print(favorite)

        activities_string = ", ".join(favorite)  # make the Python list into a string

        friend_dict = {
            "fname": fname,
            "sport": flavor,
            "stream": read,
            "favorite": activities_string,
        }

        print(friend_dict)
        friends_dict.append(
            friend_dict
        )  # append this dictionary entry to the larger friends dictionary
        print(friends_dict)

            flash(
            "The friend ;" + fname + " has been added to the database.",
            "success",
        )
        
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

@app.route('/about', methods=["GET","POST"])
def about():
    return render_template(
        "about.html", pageTitle="About"
    )

if __name__ == "__main__":
    app.run(debug=True)
