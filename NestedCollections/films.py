for m in movies:
    release_year = m.get("year")
    if release_year in movie_dictionary:
        movie_dictionary[release_year]+=1
    else:
        movie_dictionary[release_year]=1
print(movie_dictionary)
