import yaml

from gradio_ui import GradioUI
from smolagents import CodeAgent, HfApiModel

from tools.film_recommender import FilmRecommender
from tools.film_metadata import FilmMetadata

from tools.final_answer import FinalAnswerTool
from tools.watchlist import watchlist

# load the model from Hugging Face
model = HfApiModel(
    max_tokens=2096,
    temperature=0.5,
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    custom_role_conversions=None,
)

# define tools
film_recommender = FilmRecommender()
final_answer = FinalAnswerTool()
film_info = FilmMetadata()
tools = [film_recommender, final_answer, film_info, watchlist]

# define prompt templates
with open("prompts/prompt_template.yaml", "r") as stream:
    prompt_templates = yaml.safe_load(stream)


# define code agent
agent = CodeAgent(
    model=model,
    tools=tools,
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    prompt_templates=prompt_templates,
)

# launch the app
GradioUI(agent).launch()
