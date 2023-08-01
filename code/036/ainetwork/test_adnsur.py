import requests
from bs4 import BeautifulSoup

def scrape_adnsur():
    """Scrapes the ADNSUR website for text content."""
    url = "https://www.adnsur.com.ar/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    text_content = []
    container_divs = soup.find_all("div", class_="container")
    
    for element in container_divs:
        for span in element.find_all("span"):
            text_content.append(span.text)
            
    aria_label_divs = []
    for div in soup.find_all("div"):
        for link in div.find_all("a"):
            if link.has_attr("aria-label"):
                aria_label_divs.append(link["aria-label"])
                
    return text_content, aria_label_divs

if __name__ == "__main__":
    text_content, aria_label_divs = scrape_adnsur()
    for data in text_content:
        print(data)
    for data in aria_label_divs:
        print(str(data))
 
