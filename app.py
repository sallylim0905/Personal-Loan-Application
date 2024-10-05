from flask import Flask,render_template,request
import google.generativeai as genai
import os
import numpy as np
import textblob

model = genai.GenerativeModel("gemini-1.5-flash")
api = os.getenv("MAKERSUITE")
genai.configure(api_key=api)

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))


@app.route("/faq",methods=["GET","POST"])
def faq():
    return(render_template("faq.html"))

@app.route("/q1",methods=["GET","POST"])
def q1():
    r = model.generate_content("How should I diversify my investment portfolio?")
    return(render_template("q1_reply.html",r=r))

@app.route("/q2",methods=["GET","POST"])
def q2():
    q = request.form.get("q")
    r = model.generate_content(q)
    return(render_template("q2_reply.html",r=r))

if __name__ == "__main__":
    app.run()
