from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("templates_html/lang.html")

@app.route("/top_tweets")
def top_tweets():
    return render_template("templates_html/top_tweets.html")

@app.route("/trends")
def trends():
    return render_template("templates_html/trends.html")

if __name__ == "__main__":
    app.run(debug = True)    