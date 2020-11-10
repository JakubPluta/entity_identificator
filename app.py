from flask import Flask, render_template, url_for, request
import re
import pandas as pd
import spacy
import en_core_web_sm
from spacy import displacy
from named_entity_extractor.ner import NER


app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/extract', methods=["POST"])
def extractor():
    if request.method == "POST":
        choice = request.form['choice']
        text = request.form['text']

        results, n_of_records = NER(text,choice).process_text()

        return render_template("index.html", results=results, num_of_results = n_of_records)