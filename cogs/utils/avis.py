import aiohttp
import lxml
import unicodedata

from bs4 import BeautifulSoup as bs

class BookSifter:
    async def return_json(self, lookup):
        if "indé:" in lookup.lower() or "inde:" in lookup.lower():
            lookup_url = f"https://www.googleapis.com/books/v1/volumes?q={lookup[5:]}"

        lookup_url = f"https://www.googleapis.com/books/v1/volumes?q={lookup}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(lookup_url) as response:
                return await response.json()
            
    async def look_up(self, lookup):
        args = self.deal_with_args(lookup)
        try:
            json_results = await self.return_json(args)
        except:
            return "J'ai rien trouvé .__."

        try:
            book = json_results["items"][0]
        except KeyError:
            return "Aucun livre ne correspond à votre recherche. Êtes-vous ivre ?"

        book_info = book["volumeInfo"]
        book_dict = {
            "title": book_info['title'],
            "authors": book_info["authors"],
            "link": book_info["canonicalVolumeLink"],
        }

        return book_dict
    
    def deal_with_args(self, args):
        """
        Deal with args by removing words
        that might be here by accident
        """
        as_list = list(args)
        new_list = [word for word in as_list
            if (len(word) > 2) and 
            word not in ("par", "INDE", "INDÉ")]
        
        return "+".join(new_list)
    
    async def deal_with_authors(self, author_list):
        next_to_last = len(author_list) - 1
        result = ""
        i = 0
        
        for item in author_list:
            i += 1
            if i < next_to_last:
                result += f"{item}, "
            elif i == next_to_last:
                result += f"{item} et "
            else:
                result += item

        return result