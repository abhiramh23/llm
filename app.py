from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = "your_secret_key"
API_BASE_URL = "http://localhost:8000"

users = {"user1": "password1", "user2": "password2"}


@app.route("/", methods=["GET", "POST"])
def home():
    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        pipeline_name = request.form.get("pipeline_name")
        input_data = request.form.get("input_data")
        max_length = request.form.get("max_length", 50)

        response = requests.post(
            f"{API_BASE_URL}/run_pipeline",
            json={
                "name": pipeline_name,
                "input_data": input_data,
                "max_length": int(max_length),
            },
        )

        result = response.json()

        if "summary_text" in result["output"][0]:
            result_text = result["output"][0]["summary_text"]
        elif "label" in result["output"][0]:
            result_text = (
                f"{result['output'][0]['label']}: {result['output'][0]['score']}"
            )
        elif "translation_text" in result["output"][0]:
            result_text = result["output"][0]["translation_text"]

        return render_template("index.html", result=result_text)

    return render_template("index.html", result=None)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username] == password:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return "Invalid credentials, please try again."

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run()
