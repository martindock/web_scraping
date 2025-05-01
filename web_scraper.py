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
                    #if len(cells) >= 3:  # Ensure we have at least 3 cells
                    try:
                        #  Extract data, but handle potential IndexError
                        #name_cell = cells[2] if len(cells) > 1 else None
                        #name_element = name_cell.find('a') or name_cell.find('b') if name_cell else None
                        name = cells[2].text.strip() #if name_element else "N/A"

                        start_date = cells[3].text.strip() #if len(cells) > 2 else "N/A"
                        end_date = cells[4].text.strip() #if len(cells) > 3 else "N/A"

                        print(f"Name: {name}, Start Date: {start_date}, End Date: {end_date}")
                        time.sleep(0.5)  # Be respectful

                    except IndexError as e:
                        print(f"Skipping row: IndexError while accessing cells: {e}")
                    #else:
                        #print(f"Skipping row: Not enough data columns (columns={len(cells)})")
            print("Finished processing all tables")

        except urllib.error.URLError as e:
            print(f"Error accessing {self.site}: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    target_website = "https://es.wikipedia.org/wiki/Anexo:Presidentes_de_Chile"
    scraper = GenericWebScraper(target_website)
    scraper.scrape()
