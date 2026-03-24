import sys
import requests
from bs4 import BeautifulSoup

def verify_utcs(eid):
    url = f"https://directory.utexas.edu/?query={eid}&scope=all"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return False
            
        soup = BeautifulSoup(response.text, 'html.parser')

        page_text = soup.get_text().lower()
        
        if "computer sci" in page_text:
            return True
        return False
    except Exception:
        return False

if __name__ == "__main__":
    user_eid = sys.argv[1]
    if verify_utcs(user_eid):
        print("verified")
        sys.exit(0)
    else:
        print("failed")
        sys.exit(1)