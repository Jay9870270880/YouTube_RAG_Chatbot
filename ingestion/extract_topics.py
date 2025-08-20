# extract_topics.py
from youtube import YoutubeIngestor
from keybert import KeyBERT

class TopicExtractor:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        """
        Initialize the KeyBERT model with a sentence-transformer embedding model.
        Default: all-MiniLM-L6-v2 (lightweight & fast).
        """
        self.model = KeyBERT(model_name)

    def extract_topics(self, text, top_n=10):
        """
        Extract key topics or phrases from the transcript text.

        Args:
            text (str): The full transcript text.
            top_n (int): Number of key topics to extract.

        Returns:
            List[str]: List of extracted key topics.
        """

        # Extract keywords/phrases
        
        keywords = self.model.extract_keywords(
            text,
            keyphrase_ngram_range=(1, 3),
            stop_words='english',
            top_n=top_n
        )

        # keywords = [('data science', 0.7), ('machine learning', 0.65), ...]
        topics = [kw[0] for kw in keywords]
        return topics
    
# yt_ingestor = YoutubeIngestor()
# yt_URL = input('Enter URL: ' )
# transcripts = yt_ingestor.ingest_youtube_video(yt_URL)

# te = TopicExtractor()
# topics = te.extract_topics(transcripts)
# print(topics)


### OUTPUT ====>>>
'''
# Enter URL: https://www.youtube.com/watch?v=8WBS0dT0h2I&t=4731s
# Processing YouTube URL: https://www.youtube.com/watch?v=8WBS0dT0h2I&t=4731s
# Extracting ID from full URL: v=8WBS0dT0h2I&t=4731s
# Fetching transcript for video ID: 8WBS0dT0h2I
# Transcript found in English for video ID: 8WBS0dT0h2I

# Extracted Transcript Language: en
# ['transformer architecture training', 'transformer helps learn', 'transformer architecture various', 'improve transformer architecture', 'transformer architecture new', 'transformer architecture', 'improving transformer', 'improvements transformer architecture', 'transformer architecture drastically', 'transformer models']
'''