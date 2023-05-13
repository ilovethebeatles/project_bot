my_token = 'YOUR TOKEN'
headers = {"X-API-KEY": "DP1JG18-0BP4711-NKK1SXW-3WGRN9T"} 
help_button = 'Help'
search_button='Найти похожие фильмы'
actor_button='Найти фильмы по актеру/актрисе'
topic_button ='Найти фильмы на тему'
start_command = 'start'
say_hello = """\
        Привет! Я FilmoBot и подыщу тебе фильмы на основе твоих запросов. Для общения со мной используй команды или кнопки.Пожалуйста, обрати внимание, что лимит запросов - 200 за сутки."""
type_content = 'text'
help_reply = """\
        Используй 'Найти похожие фильмы' или команду /search, и ты получишь список фильмов, похожий на введенный тобой фильм\n
Используй 'Найти фильмы по актеру/актрисе' или команду /actor, и ты получишь список фильмов, в которых участвовал введенный тобой актер\n
Используй 'Найти фильмы на тему' или команду /topic, и ты получишь список фильмов на введенную тобой тему\n
Используй 'Help' или команду /help, чтобы получить этот текст"""
search_reply = """\
            Введи название фильма, чтобы получить список похожих:"""
actor_reply="""\
            Введи имя актера/актрисы, чтобы получить фильмы с его участием:"""
topic_reply = """\
            Введи тему, на которую хочешь посмотреть фильм(лучше вводить с маленькой буквы и в единственном числе, например: вампир)):"""
basic_site = 'https://api.kinopoisk.dev'
request_act = '/v1/person'
request_movie = '/v1.3/movie'
request_keyword = '/v1/keyword'

fields_parsed = 'selectFields'
fields_act = "name movies"
fields_sim = "name similarMovies"
fields_key = 'title movies'
name_field = 'name'
title_field = 'title'
id_field = 'id'
empty_line = ''
data = 'docs'
movies_field = 'movies'
sim_movies_field = 'similarMovies'
actor_name = 'actor'
act_name_intro = 'Имя актера:' 
film_name_intro = 'Имя фильма:'
list_sim_films_intro ='Список похожих фильмов:\n'
new_line = '\n'
film_list_intro = 'Список фильмов:\n'
empty_value = None
list_max_length = 20
sim_list_max_length = 10
sep_line = '---\n'
topic_error = "Извините, ничего по вашему запросу не нашлось. Попробуйте поменять число (например вампиры -> вампир) или проверить правописание и сделайте новый запрос."
act_error = "Извините, я не нашел такого актера. Проверьте правильность написания имени и фамилии и сделайте новый запрос."
sim_error = "Извините, кажется, нет такого фильма. Проверьте правильность написания названия и сделайте новый запрос."
command_help = '/help'
command_search = '/search'
command_actor = '/actor'
command_topic = '/topic'
multiple_ans = 'Нашел несколько результатов по твоему запросу:\n\n\n'
topic_num = 5