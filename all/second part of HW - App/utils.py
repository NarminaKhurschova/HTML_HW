import json
def load_candidates_from_json():
    with open("candidates.json") as file:
        canditates_data = json.load(file)
        return canditates_data

def get_candidate(candidate_id):
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate

def find_candidates_by_name(candidate_name):
    candidates = []
    for candidate in load_candidates_from_json():
        name_surname = candidate["name"].lower().split(' ')
        if candidate_name.lower() in name_surname:
            candidates.append(candidate)
    return candidates

def get_candidates_by_skills(candidate_skill):
    candidates_list = []
    for candidate in load_candidates_from_json():
        skills = candidate['skills'].lower().replace(" ","").split(",")
        if candidate_skill.lower() in skills:
            candidates_list.append(candidate)
    return candidates_list