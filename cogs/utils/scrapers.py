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
    @staticmethod
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
    
    @staticmethod
    async def return_contest(contest):
        title = unicodedata.normalize("NFKD", contest.find('h2').get_text(strip=True))
        subtitle = unicodedata.normalize("NFKD", contest.find('h3').text)
        tags = contest.find('div', 'mt2 mb1-ns f7 f5-ns')
        tags = tags.find_all('a')
        tags = ", ".join([unicodedata.normalize("NFKD", tag.text).capitalize() for tag in tags])
        categories = contest.find_all("p", "mv0")
        link = contest.find('a', class_="db navy")["href"]

        results = [title, subtitle, tags]

        for cat in categories:
            cat = unicodedata.normalize("NFKD", cat.get_text(strip=True))
            if (r"Frais d'inscription" in cat) and r":0 €" not in cat:
                break
            elif r"Ajout" in cat:
                continue

            else:
                results.append(cat)
            
        results.append(link)
        return results
    
    @staticmethod
    async def format_contests(by_added=False, by_deadline=False):        
        if by_added:
            url = "https://textes-a-la-pelle.fr/?filter=&sort=publication_date"
        else:
            url = "https://textes-a-la-pelle.fr/?filter=&sort=closing_date"

        contests = await scrape(url, WritingContest.return_all_contests)

        results = []

        for con in contests:
            con[0] = f"🖋 **{con[0].upper()}**"
            con[1] = f"**{con[1]}**"
            con[2] = f"*{con[2]}*\n"
            
            con = WritingContest.format_contest_items(con)
            con[-1] = f"**Lien :** {con[-1]}"
            con = "\n".join(con)
            results.append(con)

        return results
    
    @staticmethod
    def format_contest_items(contest_list):
        """
        Properly format categories formatted as name: desc
        """
        return [
            "**" + bit.replace(" :", "** : ")
            if " :" in bit
            else bit
            for bit in contest_list]
