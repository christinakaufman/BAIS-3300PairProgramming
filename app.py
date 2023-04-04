from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "alsknq3rAg$GernaeasSEF^woei4r098HRFYUKioq73498"


friends_dict = [
    {"name": "Test", "flavor": "Soccer", "read": "yes", "activities": "ESPN"}
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


###### Routes ######

# Home page
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Web form template", friends=friends_dict
    )


# /add route for form submission
@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        fname = form["fname"]
        flavor = form["flavor"]
        read = form["read"]
        activities = form.getlist("activites")  # this is a PYthon list

        print(fname)
        print(flavor)
        print(read)
        print(activities)

        activities_string = ", ".join(activities)  # make the Python list into a string

        friend_dict = {
            "name": fname,
            "flavor": flavor,
            "read": read,
            "activities": activities_string,
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


# About page
@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", pageTitle="Pair programming team")


if __name__ == "__main__":
    app.run(debug=True)

