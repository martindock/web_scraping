import urllib.request
from bs4 import BeautifulSoup
import re
import time

class GenericWebScraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        try:
            r = urllib.request.urlopen(self.site)
            html = r.read().decode('utf-8')
            soup = BeautifulSoup(html, "html.parser")

            tables = soup.find_all('table', {'class': 'wikitable'})  # Find ALL tables

            for table in tables:  # Iterate through each table
                rows = table.find_all('tr')  # Get all rows in the table
                for row in rows[1:]:  # Skip the header row
                    cells = row.find_all('td')
                    if len(cells) >= 3:  # Ensure we have at least 3 cells
                        try:
                        #Extract data, but handle potential IndexError
                            name = cells[2].text.strip() #if name_element else "N/A"
                            start_date = cells[3].text.strip().split()[-1] #if len(cells) > 2 else "N/A"
                            end_date = cells[4].text.strip().split()[-1] #if len(cells) > 3 else "N/A"
                            #duration = int(end_date) - int(start_date)

                            print(f"{name} ({start_date} - {end_date})")
                            time.sleep(1)  # Be respectful

                        except IndexError as e:
                            print(f"Skipping row: IndexError while accessing cells: {e}")
                    else:
                        print("Finished processing all tables")

        except urllib.error.URLError as e:
            print(f"Error accessing {self.site}: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    target_website = "https://es.wikipedia.org/wiki/Anexo:Presidentes_de_Chile"
    scraper = GenericWebScraper(target_website)
    scraper.scrape()
