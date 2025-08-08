import pandas as pd
import numpy as np

# Sample movie ratings data
data = {
    'Movie': ['Inception', 'Before Sunrise', 'American Beauty', 'The Dark Knight', 'Dune'],
    'Genre': ['Sci-Fi', 'Romance', 'Action', 'Action', 'Sci-Fi'],
    'User1': [9, 8, 9, 10, 8],
    'User2': [10, 7, 8, 9, 9],
    'User3': [8, 8, 9, 10, 7]
}

# Creating DataFrame
df = pd.DataFrame(data)

# average rating per movie
df['Average Rating'] = np.mean(df[['User1', 'User2', 'User3']], axis=1)

# highest and lowest rated movies
highest_rated = df.loc[df['Average Rating'].idxmax()]
lowest_rated = df.loc[df['Average Rating'].idxmin()]

# Average rating per genre
genre_avg = df.groupby('Genre')['Average Rating'].mean()

# Movies above a threshold (e.g., rating > 8.5)
top_movies = df[df['Average Rating'] > 8.5]

# Print results
print("Movie Ratings Data:\n", df)
print("\n Highest Rated Movie:\n", highest_rated)
print("\n Lowest Rated Movie:\n", lowest_rated)
print("\n Average Rating by Genre:\n", genre_avg)
print("\n Movies with Rating Above 8.5:\n", top_movies) 