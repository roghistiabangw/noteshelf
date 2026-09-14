# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: NoteShelf
import re
from datetime import datetime

def parse_date(date_str):
    """Parse common date formats and return a datetime object.
    
    Supported formats:
        - YYYY-MM-DD (ISO)
        - YYYY/MM/DD
        - YYYY.MM.DD
        - DD/MM/YYYY
        - DD-MM-YYYY
        - DD Mon YYYY (e.g., 15 Jan 2024)
        - Mon DD, YYYY (e.g., Jan 15, 2024)
    
    Raises ValueError with a clear message if the date cannot be parsed.
    """
    separators = ['-', '/', '.']
    
    # Try ISO format: YYYY-MM-DD or YYYY/MM/DD or YYYY.MM.DD
    for sep in separators:
        try:
            return datetime.strptime(date_str, f'%Y{sep}%m{sep}%d')
        except ValueError:
            continue
    
    # Try DD/MM/YYYY or DD-MM-YYYY
    try:
        return datetime.strptime(date_str, '%d/%m/%Y')
    except ValueError:
        try:
            return datetime.strptime(date_str, '%d-%m-%Y')
        except ValueError:
            pass
    
    # Try DD Mon YYYY
    try:
        return datetime.strptime(date_str, '%d %b %Y')
    except ValueError:
        pass
    
    # Try Mon DD, YYYY
    try:
        return datetime.strptime(date_str, '%b %d, %Y')
    except ValueError:
        pass
    
    raise ValueError(f"Unable to parse date string: '{date_str}'. "
                     f"Supported formats: YYYY-MM-DD, DD/MM/YYYY, DD Mon YYYY, etc.")
