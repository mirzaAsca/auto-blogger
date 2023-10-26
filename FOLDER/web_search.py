from __future__ import annotations
from googleapiclient.discovery import build
import json

def web_search(query: str, num_results: int = 3) -> str: # int - number of results to include with 1 search
    """Useful for general internet search queries using Google Custom Search."""

    print("WEB_SEARCH web_search started")  # Indicates the start of the function

    # Your Google Custom Search API Key and Search engine ID
    API_KEY = "AIzaSyAJxSc8T8_G6Ysxpg_W8cxwXndWu1tXjfs"
    SEARCH_ENGINE_ID = "9486572ea12954a0d"

    # Initialize the Google Custom Search API client
    service = build("customsearch", "v1", developerKey=API_KEY)
    search_results = []

    if not query:
        print("No query provided for web_search")  # Indicates an early return due to missing query
        return json.dumps(search_results)

    # Query Google Custom Search and limit the results
    print(f"WEB_SEARCH Executing web search for query: {query}")  # Indicates that a query is being made
    results = service.cse().list(q=query, cx=SEARCH_ENGINE_ID, num=num_results).execute()
    
    if not results or 'items' not in results:
        print("No results returned from the search query")  # Indicates a case where the search didn't return items
        return json.dumps(search_results)

    # Extract and return the search results
    for item in results['items']:
        search_results.append({
            "title": item.get("title", ""),
            "link": item.get("link", ""),
            "snippet": item.get("snippet", "")
        })

    print(f"WEB_SEARCH Returning {len(search_results)} search results")  # Indicates the function is about to conclude and return results
    return json.dumps(search_results, ensure_ascii=False, indent=4)

# You can add additional functions or utility methods below if needed
