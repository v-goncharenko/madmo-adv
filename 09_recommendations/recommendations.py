# Получить список фильмов, оцененных обоими
def similar_films(critics_dict, person1, person2):
    # создаем пустой список фильмов
    sim_film = []

    # для всех фильмов у person1...
    for film in critics_dict[person1]:
        # если такой фильм оценивался person 2...
        if film in critics_dict[person2]:
            # добавляем этот фильм в список sim_film
            sim_film.append(film)

    return sim_film


# обращает матрицу предпочтений, чтобы строки соответствовали образцам
def transform_prefs(critics_dict):
    # инициилизируем новый словарь с фильмами и их оценками
    result = {}

    # для каждого критика в словаре
    for person in critics_dict:
        # для каждого оцененного им фильма
        for item in critics_dict[person]:
            # добавляем такой объект в словарь
            result.setdefault(item, {})
            # меняеи местами человека и предмет
            result[item][person] = critics_dict[person][item]
    return result


# Функция для загрузки данных MovieLens
def load_movie_lens():
    # получить названия фильмов
    movies = {}
    for line in open("u.item", encoding="ISO-8859-1"):
        (id, title) = line.split("|")[0:2]
        movies[id] = title

    # загрузить данные
    prefs = {}
    for line in open("u.data"):
        (user, movieid, rating, ts) = line.split("\t")
        prefs.setdefault(user, {})
        prefs[user][movies[movieid]] = float(rating)

    return prefs
