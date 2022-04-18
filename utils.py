import json


def get_candidates(path):
    """Получает список кандидатов"""
    with open(path, 'r', encoding='utf-8') as candidates:
        return json.load(candidates)


def format_candidates(candidates_list):
    """Форматирует список кандидатов"""
    result = '<pre>'
    for candidate in candidates_list:
        result += (
            f'Имя кандидата - {candidate["name"]}\n'
            f'Позиция кандидата - {candidate["position"]}\n'
            f'Навыки через запятую - {candidate["skills"]}\n\n'
        )

    result += '</pre>'

    return result


def get_candidate_by_id(candidates_list, candidate_id):
    """Возвращает данные кандидата по его id"""
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidate_by_skill(candidates_list, candidate_skill):
    """Возвращает список скиллов кандидата"""
    result = []

    for candidate in candidates_list:
        candidate_skills = candidate['skills'].lower().split(', ')

        if candidate_skill in candidate_skills:
            result.append(candidate)

    return result
