# movie_recommender_system
<img width="952" alt="image" src="https://github.com/user-attachments/assets/0d377e8d-995c-4f7a-b2e9-1907922148fa">


The Movie Recommender System leverages the TMDb dataset to recommend movies based on user input. Below is a detailed explanation of the process and techniques used:

1. Data Source
TMDb API: The data for movies, such as titles, overviews, genres, and posters, is fetched from The Movie Database (TMDb) via their public API. This ensures that the movie data is always up-to-date.
API Key: An active TMDb API key is required to retrieve movie data. Make sure to sign up for the API on TMDb's website.


2. Data Preprocessing
To make effective recommendations, the data fetched from TMDb was preprocessed using various techniques:

Text Preprocessing: The movie overviews were cleaned and processed to remove unnecessary characters like punctuation and stopwords.
Lowercasing: All text data was converted to lowercase to ensure uniformity and consistency when calculating similarity.
Tokenization: The text was split into individual tokens (words) for further processing.
Stemming: Words were reduced to their root form using stemming techniques to capture the essence of each word.


3. Feature Extraction
After preprocessing the textual data, I extracted relevant features:

Movie Titles: The system allows users to select a movie by title, which serves as the basis for recommendations.
Movie Overviews: The overview of each movie was used as the primary feature for similarity calculation.


4. Vectorization
I used TF-IDF (Term Frequency-Inverse Document Frequency) to convert the text data (movie overviews) into numerical form:

TF-IDF Vectorizer: This technique converts the movie overviews into vectors of numbers. It gives more weight to unique words that are important to describe a movie, while down-weighting common words like "the" and "is."
High-Dimensional Vector Representation: Each movie is represented by a vector in a high-dimensional space where the features correspond to words in the movie's description.


5. Calculating Similarity Scores
To recommend similar movies, I calculated the cosine similarity between the movie vectors:

Cosine Similarity: This measures the angle between the vectors of two movies. A smaller angle (i.e., higher cosine similarity) means that the movies are more similar in terms of their descriptions.
Similarity Matrix: A matrix of similarity scores was generated where each element represents the cosine similarity between two movies. The top n similar movies for a selected movie are then recommended.


6. Recommender Logic
The recommendation system works as follows:

The user selects a movie from a dropdown menu.
The system retrieves the vector for the selected movie and calculates its similarity to all other movies in the dataset.
Movies with the highest similarity scores are displayed as recommendations.


7. Movie Poster Fetching
In addition to recommending movie titles, the system fetches movie posters from TMDb using the API:

Poster Fetching: The fetch_poster() function retrieves the poster URL for each recommended movie, making the recommendations more visually engaging.


8. Libraries and Tools Used
The project uses the following Python libraries and tools:

Pandas: For handling movie data in a tabular format.


NumPy: For numerical operations, including vector manipulations.


Scikit-learn: For preprocessing text data and calculating TF-IDF vectors and cosine similarity.


Requests: For making HTTP requests to the TMDb API to fetch movie data and posters.


Streamlit: For building an interactive user interface to display recommendations in real-time.


This process ensures that the recommendations are based on movie descriptions, providing users with a set of movies that are contextually similar to the one they select. By leveraging modern machine learning techniques like TF-IDF vectorization and cosine similarity, this system provides accurate and relevant movie suggestions.
