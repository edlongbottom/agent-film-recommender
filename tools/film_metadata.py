import os
import requests

from smolagents import Tool

OMDB_API_KEY = os.getenv("OMDB_API")


class FilmMetadata(Tool):
    name = "film_metadata"
    description = """
    Retrieves information about a film given its title using the OMDB API.
    Returns a string including the film's title, director, release date, IMDB score, plot etc.
    """

    inputs = {
        "title": {
            "type": "string",
            "description": "Title of the film to retrieve metadata for.",
            "required": True,
        }
    }
    output_type = "string"

    def forward(
        self,
        title: str,
    ) -> str:

        params = {"apikey": OMDB_API_KEY, "t": title}
        response = requests.get(f"http://www.omdbapi.com", params=params)
        data = response.json()

        if data.get("Response") == "False":
            return {
                "error": data.get("Error", "Film not found"),
                "title": title,
            }

        return f"""
                {data['Title']} is a {data['Genre']} film directed by {data['Director']}. It was  
                released on {data['Released']} and is {data['Runtime']} long.\n
                It has an IMDB score of {data['imdbRating']} and the plot is as follows:\n
                {data['Plot']}
                """
