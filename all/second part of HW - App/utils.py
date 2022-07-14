import json
def load_candidates_from_json():
    """Функция выгрузки данных кандидатов"""
    with open("candidates.json") as file:
        canditates_data = json.load(file)
        return canditates_data

def get_candidate(candidate_id):
    """Функция поиска кандидата по id"""
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate

def find_candidates_by_name(candidate_name):
    """Функция поиска кандидата по имени"""
    candidates = []
    for candidate in load_candidates_from_json():
        # Приведение имени и фамилии к удобному сравнению с переменной candidate_name
        name_surname = candidate["name"].lower().split(' ')
        # Добавление в список подходящего кандидата
        if candidate_name.lower() in name_surname:
            candidates.append(candidate)
    return candidates

def get_candidates_by_skills(candidate_skill):
    """Функция поиска кандидата по скиллу"""
    candidates_list = []
    # Приведение списка скиллов к удобному сравнению
    for candidate in load_candidates_from_json():
        skills = candidate['skills'].lower().replace(" ","").split(",")
        # Добавление подходящего кандидата по совпедению скилла
        if candidate_skill.lower() in skills:
            candidates_list.append(candidate)
    return candidates_list