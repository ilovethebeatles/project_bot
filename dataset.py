import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
import warnings; warnings.simplefilter('ignore')
import config

class Dataset:
    def __init__(self, data, small_data, credits_file, keywords_file) :

        big_data = pd.read_csv(data)
        credits = pd.read_csv(credits_file)
        keywords = pd.read_csv(keywords_file)
        links_small = pd.read_csv(small_data)
        keywords[config.id_col] = keywords[config.id_col].astype(config.id_type)
        credits[config.id_col] = credits[config.id_col].astype(config.id_type)
        links_small = links_small[links_small[config.tmdbId_col].notnull()][config.tmdbId_col]
        links_small = links_small.astype(config.tmdbId_type)
        big_data = big_data.drop(config.bad_lines)
        big_data[config.id_col] = big_data[config.id_col].astype(config.id_type)
        big_data = big_data.merge(credits, on=config.id_col)
        big_data = big_data.merge(keywords, on=config.id_col)
        self.my_dataset = big_data[big_data[config.id_col].isin(links_small)]
        self.my_dataset[config.tagline_col] = self.my_dataset[config.tagline_col].fillna(config.empty_line)
        self.my_dataset[config.overview_col] = self.my_dataset[config.overview_col].fillna(config.empty_line)
        self.my_dataset[config.description_col] = self.my_dataset[config.overview_col] + self.my_dataset[config.tagline_col]
        for column in (config.cast_col, config.keywords_col):
            self.my_dataset[column] = self.my_dataset[column].apply(literal_eval)
            self.my_dataset[column] = self.my_dataset[column].apply(lambda x: [item[config.name] for item in x] if isinstance(x, list) else list())
    
    
    def rec_sim(self, film_name):
        tf_idf = TfidfVectorizer(analyzer=config.analyzer_param,ngram_range=config.ngram_range_param, min_df=config.min_df_param, stop_words=config.stop_words_param)
        tfidf_matrix = tf_idf.fit_transform(self.my_dataset[config.description_col])
        cos_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        self.my_dataset = self.my_dataset.reset_index(drop = True)
        idx = pd.Series(data=self.my_dataset.index, index=self.my_dataset[config.title_col])[film_name]
        sim_scores = list(enumerate(cos_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:config.lim_rec_sim]
        similar_films_index = [i[0] for i in sim_scores]
        result =  self.my_dataset[config.title_col][similar_films_index]
        result = list(result.reset_index(drop = True))
        return config.sep_symb.join(result)
    def rec_act(self, actor_name):
        self.my_dataset[config.hasactor_col] = self.my_dataset[config.cast_col].apply(lambda x: actor_name in x)
        l = list(self.my_dataset[self.my_dataset[config.hasactor_col]][config.title_col])
        return config.sep_symb.join(l)
    def rec_topic(self, topic):
        self.my_dataset[config.hastopic_col] = self.my_dataset[config.keywords_col].apply(lambda x: topic in x)
        l = self.my_dataset[self.my_dataset[config.hastopic_col]][[config.title_col, config.vote_average_col]]
        l = l.sort_values(by = [config.vote_average_col], ascending=False).head(config.head_value)
        l = list(l[config.title_col]) 
        return config.sep_symb.join(l)