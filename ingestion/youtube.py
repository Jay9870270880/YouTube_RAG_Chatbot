# ===========================
# STEP 1 to 3: YOUTUBE ID, TRANSCRIPT, TRANSLATE
# ===========================

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from urllib.parse import urlparse, parse_qs
from deep_translator import GoogleTranslator


class YoutubeIngestor:
    
    
    def __init__(self):
        pass
    
    
    # ===========================
    # STEP 1: EXTRACT YOUTUBE ID    
    # ===========================
    # write working of extract_youtube_id(youtube_url) in comments
    # This function extracts the video ID from a YouTube URL.
    # It handles both short URLs (youtu.be) and full URLs (youtube.com).
    def extract_youtube_id(self,  url):
        """Extract the video ID from a YouTube URL."""
        url_after_parsing = urlparse(url)
        # what is this line doing?
        # It parses the URL and extracts its components like scheme, netloc, path, and query.

        if url_after_parsing.hostname in ['youtu.be']:
            # print(f"Extracting ID from short URL: {url_after_parsing.path[1:]}")
            return url_after_parsing.path[1:]
        
        if url_after_parsing.hostname in ['www.youtube.com', 'youtube.com']:
            # print(f"Extracting ID from full URL: {url_after_parsing.query}")
            return parse_qs(url_after_parsing.query).get('v', [None])[0]
        return None


    '''This function extracts the video ID from a YouTube URL.
    It handles both short URLs (youtu.be) and full URLs (youtube.com).
    If the URL is invalid or does not contain a video ID, it returns None.'''

    # ===========================
    # STEP 2: FETCH TRANSCRIPT
    # ===========================
    ## working of YoutubeTranscriptApi.get_transcript(video_id, languages=['en']) is as follows:
    # 1. It first tries to fetch the transcript in the specified language (e.g., 'en' for English).
    # 2. If the transcript is not available in that language, it raises a NoTranscriptFound exception.
    # 3. If the video has no transcripts available at all, it raises a TranscriptsDisabled exception.
    def fetch_transcript(self , video_id):
        """Fetch transcript in English or Hindi, fallback to auto-generated captions."""
        try:
            # print(f"Fetching transcript for video ID: {video_id}")
            # First, try to get the transcript in English
            # Try English first
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            language = 'en'
            # print(f"Transcript found in English for video ID: {video_id}")
        except NoTranscriptFound:

            try:
                # Try Hindi
                transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['hi'])
                language = 'hi'
                # print(f"Transcript found in Hindi for video ID: {video_id}")

            except NoTranscriptFound:

                try:
                    # Try auto-generated captions
                    transcript = YouTubeTranscriptApi.get_transcript(video_id)
                    language = 'auto'
                    # print(f"Transcript found in auto-generated captions for video ID: {video_id}")
                except Exception:

                    return "","not_found"

        except TranscriptsDisabled:
            # print(f"Transcripts are disabled for video ID: {video_id}")
            return "", "disabled"

        # Merge all transcript text
        full_text = " ".join(chunk["text"] for chunk in transcript)
        return full_text, language


    # ===========================
    # STEP 3: TRANSLATE TO ENGLISH
    # ===========================
    # This function translates a given text to English using Google Translator.
    # It breaks the text into smaller chunks to avoid exceeding character limits.
    def translate_to_english(self , text, max_chars=2000):
        translator = GoogleTranslator(source='auto', target='en')
        translated_text = ""

        # Break the text into smaller chunks
        for i in range(0, len(text), max_chars):
            chunk = text[i:i+max_chars]
            translated_chunk = translator.translate(chunk)
            translated_text += translated_chunk + " "

        return translated_text.strip()


    # ===========================
    # STEP 4: INGEST YOUTUBE VIDEO
    # ===========================
    # write working of extract_youtube_id(youtube_url) in comments
    # This function extracts the video ID from a YouTube URL.
    # It handles both short URLs (youtu.be) and full URLs (youtube.com).
    # If the URL is invalid or does not contain a video ID, it returns None.
    # It also validates the URL format to ensure it starts with http:// or https://.

    def ingest_youtube_video(self , youtube_url):

        """Ingest a YouTube video URL and return the transcript."""
        print(f"Processing YouTube URL: {youtube_url}")

        if not youtube_url:
            raise ValueError("YouTube URL cannot be empty")

        # Validate URL format
        if not youtube_url.startswith(('http://', 'https://')):
            raise ValueError("Invalid YouTube URL format. Must start with http:// or https://")

        # Extract video ID
        video_id = self.extract_youtube_id(youtube_url)
        if not video_id:
            raise ValueError("Invalid YouTube URL")

        transcript_text, lang = self.fetch_transcript(video_id)

        # print(f"\nExtracted Transcript Language: {lang}")

        if lang == 'hi':
            # print("\n🔄 Translating from Hindi to English...")
            transcript_text = self.translate_to_english(transcript_text)

        return transcript_text

    # # ===========================
    # # Example Test
    # # ===========================

    # if __name__ == "__main__":
    #     yt_url = input("Enter YouTube URL: ")
    #     transcript = ingest_youtube_video(yt_url)

    #     print("\n===== Extracted Transcript =====\n")
    #     print(transcript[:5000])  
