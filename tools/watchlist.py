from smolagents import tool

# In-memory watchlist (for demo purposes; in production, use persistent storage)
user_watchlist = set()


@tool
def watchlist(action: str, film: str | None = None) -> str:
    """
    Adds a film to the user's watchlist.

    Args:
        action: 'add', 'remove', or 'view'
        film: The title of the film to add or remove (not needed for 'view')

    Returns:
        A message indicating the result or the current watchlist.
    """

    if action == "add" and film:
        user_watchlist.add(film)
        return f"Added '{film}' to your watchlist."
    elif action == "remove" and film:
        if film in user_watchlist:
            user_watchlist.remove(film)
            return f"Removed '{film}' from your watchlist."
        else:
            return f"'{film}' is not in your watchlist."
    elif action == "view":
        if user_watchlist:
            return "Your watchlist: " + ", ".join(sorted(user_watchlist))
        else:
            return "Your watchlist is empty."
    else:
        return "Invalid action. Use 'add', 'remove', or 'view'."
