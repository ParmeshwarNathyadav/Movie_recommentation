import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=c0a888c07e3cec2abf1dc9d59990e4b8&language=en-US'.format(
        movie_id)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return "https://image.tmdb.org/t/p/w500" + data.get('poster_path', '')
    else:
        print(f"Error fetching data. Status code: {response.status_code}")
        return None
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.loc[i[0]].movie_id
        #feathc api
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict = pickle.load(open('movies3.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movies_name = st.selectbox(
    'Movies List ',
    movies['title'].values
)
if st.button('Recommend'):
    name, posters = recommend(selected_movies_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[1])
        st.image(posters[1])
    with col2:
        st.text(name[2])
        st.image(posters[2])
    with col3:
        st.text(name[3])
        st.image(posters[3])
    with col4:
        st.text(name[4])
        st.image(posters[4])
    with col5:
        st.text(name[5])
        st.image(posters[5])