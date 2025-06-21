import json
import random

from smolagents import Tool


class FilmRecommender(Tool):
    name = "film_recommender"
    description = """
    Suggests a film based on user preference for genre.
    Returns a film title and a short description.
    """

    inputs = {
        "genre": {
            "type": "string",
            "description": "The genre of the film (e.g., Action, Comedy, Drama).",
            "required": False,
            "nullable": True,
        }
    }

    output_type = "string"

    def forward(
        self,
        genre: str | None = None,
    ) -> str:
        # load in films from the JSON file
        with open("data/example_films.json", "r") as file:
            films = json.load(file)

        # implement filter logic
        filtered = films
        if genre:
            filtered = [m for m in filtered if genre.lower() in m["genre"]]

        if not filtered:
            filtered = films  # fallback to all

        film = random.choice(filtered)
        return f"You might enjoy '{film['title']}': {film['desc']}."
