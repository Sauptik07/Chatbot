import re
from html2text import HTML2Text

# Global Utilities
HTML_2_TEXT = HTML2Text()
HTML_2_TEXT.ignore_links = True

def cleanup_html(html: str) -> str:
    clean = HTML_2_TEXT.handle(html) \
        .replace('\n', ' ') \
        .replace('  ', ' ') \
        .strip()
        
    clean = re.sub(r'!\[\]\(.*\)', '', clean)
    
    return clean