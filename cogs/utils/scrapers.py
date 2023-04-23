import aiohttp
import lxml
import unicodedata

from bs4 import BeautifulSoup as bs


async def scrape(url, func):
    """
    This function prepares a scraped page from the urg argument,
    then scrape it with the func argument. 
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            body = await response.text()
            soup = bs(body, 'lxml')
            result = await func(soup)
            
            return result


class WritingContest:
    async def return_all_contests(soup):
        """
        Return a list of current writing contests.
        """
        try:
            contests = soup.find(id='contests')
            contests = contests.find_all('article')
            results = []

            for con in contests:
                result = await WritingContest.return_contest(con)
                results.append(result)

            return results

        except:
            return None
    
    async def return_contest(contest):
        title = unicodedata.normalize("NFKD", contest.find('h2').get_text(strip=True))
        subtitle = unicodedata.normalize("NFKD", contest.find('h3').text)
        tags = contest.find('div', 'mt2 mb1-ns f7 f5-ns')
        tags = tags.find_all('a')
        tags = ", ".join([unicodedata.normalize("NFKD", tag.text).capitalize() for tag in tags])
        categories = contest.find_all("p", "mv0")

        results = [title, subtitle, tags]

        for cat in categories:
            cat = unicodedata.normalize("NFKD", cat.get_text(strip=True))
            if ("Frais d'inscription" in cat) and \
            ((":0 €" not in cat) or (": 0 €" not in cat)) :
                break
            else:
                results.append(cat)
            
        return results
    
    async def format_contests(by_added=False, by_deadline=False):        
        if by_added:
            url = "https://textes-a-la-pelle.fr/?filter=&sort=publication_date"
        else:
            url = "https://textes-a-la-pelle.fr/?filter=&sort=closing_date"

        contests = await scrape(url, WritingContest.return_contests)

        results = []

        for con in contests:
            con[0] = f"🖋 **{con[0]}**"
            con[1] = f"*{con[1]}*"
            con = "\n".join(con)
            con = con.replace(r'\n', '\n')
            con = con.replace(' :', ' : ')
            results.append(con)

        return results