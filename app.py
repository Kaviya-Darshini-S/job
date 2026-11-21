from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    message = ""

    if request.method == "POST":
        job = request.form["job"].lower()

        suspicious_words = [
            "registration fee",
            "pay money",
            "bank details",
            "otp",
            "guaranteed income",
            "pay upfront"
        ]

        if any(word in job for word in suspicious_words):
            result = "Suspicious Job!"
            message = "This job contains suspicious indicators. Be careful!"
        else:
            result = "No Common Warning Signs Found"
            message = "No listed warning words were detected. Verify the company before applying."

    return render_template("index.html", result=result, message=message)

if __name__ == "__main__":
    app.run(debug=True)