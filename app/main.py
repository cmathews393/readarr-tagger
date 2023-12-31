import requests
import json
from bs4 import BeautifulSoup as bs


class READARRAPI:
    def __init__(self):
        self.READARR_IP = "http://192.168.1.164:8787"
        self.READARR_TOKEN = "841e67751a1b45128fbab67cd6700afe"
        self.READARR_ENDPOINT = "/api/v1/"
        self.headers = {"X-Api-Key": self.READARR_TOKEN}
        self.base_url = f"{self.READARR_IP}{self.READARR_ENDPOINT}"

    def make_request(self, endpoint_path=""):
        full_url = self.base_url + endpoint_path
        response = requests.get(full_url, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            with open("data_file.json", "w") as file:
                json.dump(data, file, indent=4)
            return data
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None


# Usage


# print(READARR_api.make_request("bookshelf"))
def getreadarrlists():
    READARR_api = READARRAPI()
    # response = READARR_api.make_request('importlist')
    importlists = READARR_api.make_request("importlist")
    # print(importlists)
    userids = []
    listnames = []
    listids = []
    for list in importlists:
        listnames.append(list["name"])
        listids.append(list["id"])

    for id in listids:
        fields = READARR_api.make_request(f"importlist/{id}")["fields"]
        userid = next(
            (field["value"] for field in fields if field["name"] == "userId"), None
        )
        if userid:
            userids.append(userid)
            if userids[0]:
                return userids


def makegoodreadsrequest(userid):
    pagenum = 1
    books_and_authors = {}

    while True:
        print("getting page")
        response = requests.get(
            f"https://www.goodreads.com/review/list/{userid}?page={pagenum}&shelf=to-read"
        )


        print(pagenum)
        # Check if the response status code is not 200 (OK)

        print("booksoup")
        booksoup = bs(response.content, "html.parser")
        no_content = booksoup.find("div", class_="greyText nocontent stacked")
        if no_content and "No matching items!" in no_content.get_text():
            print("No matching items found, exiting loop.")
            break
        print("finding titles")
        title_elements = booksoup.find_all("td", class_="field title")
        print("finding authors")
        author_elements = booksoup.find_all("td", class_="field author")
        print("if len")
        if len(title_elements) != len(author_elements):
            raise ValueError("Mismatch in the number of titles and authors")
        print("for loop")
        for title_element, author_element in zip(title_elements, author_elements):
            print("getting title")
            title = title_element.find("a").get_text(strip=True)
            print(title)
            print("getting author")
            author = author_element.find("a").get_text(strip=True)
            print(author)
            books_and_authors[author] = title

        pagenum += 1

    print(books_and_authors)


# makegoodreadsrequest("107518177")


def parsegoodreads():
    bs.find_all("meta")
    #    <meta property="og:description"
    #   content="Alyssa Inger has 63 books on their to-read shelf: My Year of Rest and Relaxation by Ottessa Moshfegh, Lies My Teacher Told Me: Everything Your American H..." />


def main():
    userids = getreadarrlists()
    for userid in userids:
        tagname, bookslist = makegoodreadsrequest(userid)
        for book in bookslist[]:
            
    return None


main()
# if __name__ == "__main__":
#     main()

# for collection in READARRimportlists:
#     collection_name = collection['label']
#     collection_id = collection['id']

#     # Step 3: Get collection details
#     collection_details = READARR_api.make_request(f'tag/detail/{collection_id}')

#     # Step 4: Extract movie IDs
#     movie_ids = collection_details['movieIds']

#     for movie_id in movie_ids:
#         # Step 5: Get movie details
#         movies_response = READARR_api.make_request(f'movie/{movie_id}')

#         # Check if the response is a list and iterate
#         if isinstance(movies_response, list):
#             plexcollection = []

#             for movie in movies_response:
#                 # Step 6: Extract and print the title
#                 movie_title = movie['title']
#                 print(movie_title)
#         else:
#             # Single movie case
#             movie_title = movies_response['title']
#             print(movie_title)

# def checkMoviesInPlex(ple):


# for item in READARRimportlists:
#     collectionname = item['label']
#     print(collectionname)
#     collectionid = item['id']
#     print(collectionid)
#     collectionitems = READARR_api.make_request(f'tag/detail/{collectionid}')
#     print(collectionitems)
#     for id in collectionitems['movieIds']:
#         print(id)
#         itemnames = READARR_api.make_request(f'movie/{id}')
#         for item in itemnames:
#             title = item['title']
#             print(title)
# for item in itemnames:

# movies = []
# movietitle = item['title']
# print(movietitle)
# print(movies)
# movie_ids_by_tag = {}
# for item in READARRimportlists:
#     tag = item['label']
#     movie_ids_by_tag[tag] = item['movieIds']

# print(movie_ids_by_tag)

# for key, value in movie_ids_by_tag.items():
#     print(f"{key}: {value}")
