from utils import get_candidate
from utils import get_candidates_by_skills
from utils import find_candidates_by_name
from utils import load_candidates_from_json
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def all_candidates():
    items = load_candidates_from_json()
    return render_template('list.html', items=items)

@app.route("/candidate/<int:x>")
def profile(x):
    candidate = get_candidate(x)
    return render_template('single.html', candidate=candidate)

@app.route("/search/<candidate_name>")
def search_by_name(candidate_name):
    candidates = find_candidates_by_name(candidate_name)
    count = len(candidates)
    return render_template('search.html', candidates=candidates, count=count )

@app.route("/skill/<skill_name>")
def search_by_skill(skill_name):
    candidates = get_candidates_by_skills(skill_name)
    count = len(candidates)
    return render_template('skill.html', candidates=candidates, count=count)


app.run()



