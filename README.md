# Agent for film recommendations

A basic Agent that can recommend films to watch, retrieve IMDB information about them and manage a watchlist. 

Created using the `smolagents` framework and uses `Gradio` for a chat interface.

Tools:
- Film recommender - recommends a random film from a LLM-generated list of real films. Optionally users can provide a genre. 
- Film metadata - queries the OMDB API to retrieve information on a film based on its title. 
- Watchlist - allows users to view/add/remove films in a watchlist. Just stored in-memory and does not persist between conversations. 


---
title: Agent Film Recommender
emoji: 💻
colorFrom: blue
colorTo: gray
sdk: gradio
sdk_version: 5.34.2
app_file: app.py
pinned: false
short_description: Agent that recommends films developed using smolagents
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

## Setup

I used HuggingFace spaces to host the app, and it interacts with a HuggingFace-hosted LLM.  

The following tokens must be created and added to the space as secrets:
- `HF_TOKEN`: HuggingFace access token 
- `OMDB_API`: OMDB API key can be created[here](https://www.omdbapi.com/apikey.aspx)