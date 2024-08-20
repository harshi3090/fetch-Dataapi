import json
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import XSD

file_path = "data/getPopularMovies.json"

# Load the JSON data from the file
with open(file_path, 'r',encodings="utf8") as f:
    data = json.load(f)

# Define a namespace
EX = Namespace("https://rdfox.com/getting-started/")

# Create a new RDF graph
g = Graph()

# Function to create RDF triples for a movie
def create_movie_rdf(movie):
    movie_uri = EX[f"movie_{movie['id']}"]
    g.add((movie_uri, RDF.type, EX.Movie))
    g.add((movie_uri, EX.title, Literal(movie['title'])))
    g.add((movie_uri, EX.original_title, Literal(movie['original_title'])))
    g.add((movie_uri, EX.overview, Literal(movie['overview'])))
    g.add((movie_uri, EX.adult, Literal(movie['adult'], datatype=XSD.boolean)))
    g.add((movie_uri, EX.original_language, Literal(movie['original_language'])))
    g.add((movie_uri, EX.popularity, Literal(movie['popularity'], datatype=XSD.float)))
    g.add((movie_uri, EX.release_date, Literal(movie['release_date'], datatype=XSD.date)))

    for genre_id in movie['genre_ids']:
        g.add((movie_uri, EX.genre_id, Literal(genre_id)))

# Process each movie in the JSON data
for movie in data['results']:
    create_movie_rdf(movie)

# Serialize the graph to Turtle format
ttl_data = g.serialize(format='turtle')

# Write the Turtle data to a file
with open('data/movies.ttl', 'w') as f:
    f.write(ttl_data)

