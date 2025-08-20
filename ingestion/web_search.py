from dotenv import load_dotenv
from langchain_community.utilities import GoogleSerperAPIWrapper

load_dotenv()


class WebSearch:
    
    def __init__(self):
        self.search = GoogleSerperAPIWrapper()
    
    def search_web(self, query):
        """
        Return summarized text result from Serper (auto-generated summary).
        """
        return self.search.run(query)
    
    def search_web_with_context(self, query):
        """
        Extract and return main organic search results as plain text.
        """
        results = self.search.results(query)
        organic_results = results.get("organic", [])

        context_parts = []
        for item in organic_results:
            title = item.get("title", "")
            snippet = item.get("snippet", "")
            link = item.get("link", "")
            context_parts.append(f"{title}\n{snippet}\n{link}\n")

        return "\n".join(context_parts)

# # Example Usage:
# search = WebSearch()

# context_text = search.search_web_with_context(
#     "What is the transformer architecture in deep learning?"
# )

# print("=== Final Context ===")
# print(context_text)
