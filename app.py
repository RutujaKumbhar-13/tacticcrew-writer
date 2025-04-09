from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form["url"]
        # Placeholder for calling your CrewAI pipeline
        return f"Received URL: {url}"
    return '''
        <h2>Welcome to TacticCrew Writer 🚀</h2>
        <form method="POST">
            Enter URL: <input type="text" name="url" />
            <input type="submit" value="Analyze" />
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
