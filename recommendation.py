import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
data = {
    'movie': [
        # Action movies
        'Avengers', 'Iron Man', 'Thor', 'Captain America', 'Doctor Strange', 'Spider-Man: No Way Home', 'Pushpa: The Rise',
        # Scifi movies
        'Interstellar', 'Inception', 'The Dark Knight', 'Tenet', 'Kalki 2898 AD', '1 - Nenokkadine', 'Project Z',
        # epic movies
        'Baahubali: The Beginning', 'Baahubali 2: The Conclusion', 'RRR', 'Salaar', 'Sye Raa Narasimha Reddy', 'KGF',
        # romance movies
        'The Notebook', 'Titanic', 'Sita Ramam', 'Bommarillu', 'Arjun Reddy', 'Geethanjali', 'Radhe Shyam', 'Uppena',
        # family movies
        'Ala Vaikunthapurramuloo', 'Jathi Ratnalu', 'F2: Fun and Frustration', 'Toy Story', 'Despicable Me', 'Mathu Vadalara'
    ],
    'genre': [
        'Action Sci-Fi Superhero', 'Action SciFi Superhero', 'Action Fantasy Superhero', 'Action Adventure Superhero', 'Action Fantasy Sci-Fi Superhero', 'Action Adventure Sci-Fi Superhero', 'Action Crime Thriller',
        'SciFi Space Drama', 'Sci-Fi Thriller MindBending', 'Action Crime Thriller', 'Action SciFi Thriller', 'Sci-Fi Epic Mythology Action', 'Action Psychological Thriller', 'Sci-Fi Thriller',
        'Action Epic Drama Fantasy', 'Action Epic Drama Fantasy', 'Action Epic Drama Historical', 'Action Crime Drama', 'Action Historical Drama', 'Action Crime Thriller',
        'Romance Drama', 'Romance Drama Disaster', 'Romance Drama War', 'Romance Family Comedy', 'Action Romance Drama', 'Romance Drama', 'Romance SciFi Drama', 'Romance Drama',
        'Action Comedy Family', 'Comedy Crime', 'Comedy Family', 'Animation Adventure Comedy', 'Animation Comedy Family', 'Comedy Crime Thriller'
    ]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(df['genre'])
similarity_matrix = cosine_similarity(genre_matrix)

def recommend(movie_name, num_recommendations=3):
    movie_list = df['movie'].tolist()
    movie_list_lower = [m.lower() for m in movie_list]
    if movie_name.lower() not in movie_list_lower:
        return f"Movie '{movie_name}' is not found in database.how about another one?"
    idx = movie_list_lower.index(movie_name.lower())
    similarity_scores = list(enumerate(similarity_matrix[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    recommendations = []
    for i in similarity_scores[1:num_recommendations+1]:
        if i[1] > 0: 
            recommendations.append(df.iloc[i[0]]['movie'])
    
    return recommendations

def main():
    print("\n===============================")
    print("AI MOVIE RECOMMENDATION SYSTEM")
    print("===============================")
    
    while True:
        print("\nAvailable Movies (Partial List):")
        print("Action: Baahubali, RRR, Avengers, Salaar")
        print("Sci-Fi: Inception, Kalki 2898 AD, Interstellar")
        print("Romance: Sita Ramam, The Notebook, Bommarillu")
        
        user_input = input("\nWhat have you watched recently? (or type 'exit'): ").strip()
        
        if user_input.lower() == 'exit':
            print("Enjoy your movie night! Goodbye!")
            break
        
        results = recommend(user_input)
        
        if isinstance(results, list):
            if not results:
                print("I don't have enough similar movies yet, but stay tuned!")
            else:
                print(f"\nSince you liked '{user_input}', you might also like:")
                for movie in results:
                    print(f" {movie}")
        else:
            print(f"\n{results}")

if __name__ == "__main__":
    main()