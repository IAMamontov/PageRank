def select_dates(potential_dates):
    result = ""
    for _ in potential_dates:
        if _["age"] > 30 and "art" in _["hobbies"] and _["city"] == "Berlin":
            if len(result) > 0:
                result += ", "
            result += _["name"]
    return result
