from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Tailwind CSS with Flask", description="A simple example of using Tailwind CSS with Flask")

if __name__ == '__main__':
    app.run(debug=True)
