def ytterm_extracter(query):
    search_term = query.replace("play", "").replace("on youtube", "").strip()
    return search_term
