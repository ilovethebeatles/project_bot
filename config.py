my_token = 'TOKEN'
data = 'movies_metadata.csv'
smaller_data = 'links_small.csv'
credits = 'credits.csv'
keywords = 'keywords.csv'
bad_lines = [19730, 29503, 35587]
help_button = 'Help'
search_button='Find me similar films'
actor_button='Find me films with a certain actor'
topic_button ='Find me films on a certain topic'
start_command = 'start'
say_hello = """\
        Hello, I'm a Filmobot, I'm here to advice you films according to your taste and occasion\
 Use buttons to send me requests and get result."""
type_content = 'text'
help_reply = """\
        Use "Find me similar films" button, type in the film, and you'll get a list of similar films\n
Use "Advise me films" button, and you'll get a list of top films according to worldwide rating."\n
Use "Choose a film for an occasion", choose the occasion in the offered list and get a list of related films.\n
Use "Help" button to see this text."""
search_reply = """\
            Type in the name of the film you like to get similar ones:"""
actor_reply="""\
            Type the name of an actor:"""
topic_reply = """\
            Type the topic(use lower case letters and singular, for example "abuse", "killer", "maniac"):"""

id_col = 'id'
id_type = 'int'
tmdbId_col = 'tmdbId'
tmdbId_type = 'int'
tagline_col = 'tagline'
overview_col = 'overview'
description_col = 'description'
cast_col = 'cast'
crew_col = 'crew'
keywords_col = 'keywords'
empty_line=''
name = 'name'
title_col = 'title'
vote_average_col = 'vote_average'
hastopic_col = 'hastopic'
hasactor_col = 'hasactor'
analyzer_param = 'word'
min_df_param = 0
ngram_range_param = (1, 4)
stop_words_param = 'english'
sep_symb = '\n'
lim_rec_sim = 11
head_value = 15