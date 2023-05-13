import requests
import random
from . import config

class Parser:
    def __init__(self):
        self.headers = config.headers

    async def rec_act(self, actor):
        response = requests.get(config.basic_site + config.request_act,
            params={
                config.fields_parsed: config.fields_act,
                config.name_field: actor,
            }, headers=self.headers)

        actors = response.json()
        result = config.empty_line
        if len(actors[config.data]) == 0:
            return config.act_error
        if len(actors[config.data]) > 1:
            result += config.multiple_ans
        for actor in actors[config.data]:
            actor_name = actor[config.name_field]
            result += config.act_name_intro + actor_name + config.new_line + config.new_line

            actor_movies = actor[config.movies_field]
            result += config.film_list_intro
            counter = 0
            for actor_movie in actor_movies:
                if counter < config.list_max_length and actor_movie[config.name_field] is not config.empty_value:
                    actor_movie_name = actor_movie[config.name_field]
                    result += actor_movie_name + config.new_line
                    counter += 1
                else:
                    continue
            result += config.sep_line
        return result

    async def rec_sim(self, movie_name):
        response = requests.get(config.basic_site+config.request_movie,
            params={
                config.fields_parsed: config.fields_sim,
                config.name_field: movie_name,
            }, headers=self.headers)

        movies = response.json()
        result = config.empty_line
        if len(movies[config.data]) == 0:
            return config.sim_error
        if len(movies[config.data]) > 1:
            result += config.multiple_ans
        for movie in movies[config.data]:
            movie_name = movie[config.name_field]
            result += config.film_name_intro + movie_name + config.new_line + config.new_line

            similar_movies = movie[config.sim_movies_field]
            result += config.list_sim_films_intro
            for similar_movie in similar_movies[:config.sim_list_max_length]:
                similar_movie_name = similar_movie[config.name_field]
                result += similar_movie_name + config.new_line

            result += config.sep_line
        return result

    async def rec_topic(self, keyword):
        response = requests.get(config.basic_site + config.request_keyword,
            params={
                config.fields_parsed: config.fields_key,
                config.title_field: keyword,
            }, headers=self.headers)

        movies = response.json()

        try:
            movies = movies[config.data][0][config.movies_field]
        except:
            return config.topic_error

        movie_ids = [movie[config.id_field] for movie in movies]
        random_movie_ids = random.sample(movie_ids, config.topic_num)
        result = config.empty_line

        for idx in random_movie_ids:
            response = requests.get(config.basic_site + config.request_movie,
                params={
                    config.fields_parsed: config.name_field,
                    config.id_field: idx,
                }, headers=self.headers)

            movies = response.json()
            result += movies[config.data][0][config.name_field] + config.new_line
        return result