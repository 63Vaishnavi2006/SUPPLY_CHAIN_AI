from flask import Flask, render_template, request
import webbrowser
import threading

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    status = ""
    demand = ""
    stock = ""

    if request.method == "POST":
        demand = int(request.form["demand"])
        stock = int(request.form["stock"])

        if demand > stock:
            status = "LOW STOCK ⚠️"
        else:
            status = "STOCK SUFFICIENT ✅"

    return render_template(
        "index.html",
        status=status,
        demand=demand,
        stock=stock
    )

# Function to open browser automatically
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=True)

