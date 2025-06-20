import json
import random

from smolagents import Tool


class FilmRecommender(Tool):
    name = "film_recommender"
    description = """
    Suggests a film based on user preferences such as genre, mood or score.
    Returns a film title, a short description, and a mock IMDB score out of 10.
    """

    inputs = {
        "genre": {
            "type": "string",
            "description": "The genre of the film (e.g., Action, Comedy, Drama).",
            "required": False,
            "nullable": True,
        },
        "mood": {
            "type": "string",
            "description": "User's current mood or desired film mood (e.g., 'uplifting', 'thrilling').",
            "required": False,
            "nullable": True,
        },
        "score": {
            "type": "number",
            "description": "Film IMDB score threshold (between 0 to 10) above which the user expects the film to score.",
            "required": False,
            "nullable": True,
        },
    }

    output_type = "string"

    def forward(
        self,
        genre: str | None = None,
        mood: str | None = None,
        score: float | None = None,
    ) -> str:
        # load in films from the JSON file
        with open("data/example_films.json", "r") as file:
            films = json.load(file)

        # implement filter logic
        filtered = films
        if genre:
            filtered = [m for m in filtered if genre.lower() in m["genre"]]
        if mood and filtered:
            filtered = [m for m in filtered if mood.lower() in m["mood"]]
        if score and filtered:
            filtered = [m for m in filtered if m["score"] >= score]

        if not filtered:
            filtered = films  # fallback to all

        film = random.choice(filtered)
        return f"You might enjoy '{film['title']}': {film['desc']} IMDB score: {film['score']}/10."
