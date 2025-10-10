import requests
from bs4 import BeautifulSoup

endpoint = "https://www.billboard.com/charts/hot-100/2000-08-26"
archive_site = "https://web.archive.org/web/20180219192606/https://www.billboard.com/charts/hot-100/2000-08-26"


def write_site(site):
    response = requests.get(site)
    with open('website.html', 'w') as file:
        file.write(response.text)


# write_site(endpoint)

with open('website.html') as f:
    data = f.read()
soup = BeautifulSoup(data, 'html.parser')
# print(soup)
song_class = ("c-title a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 "
              "lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max "
              "a-truncate-ellipsis-2line lrv-u-margin-b-025 lrv-u-margin-b-00@mobile-max")
artist_class = ("c-label a-no-trucate a-font-secondary u-font-size-15 "
                "u-font-size-13@mobile-max u-line-height-18px@mobile-max u-letter-spacing-0010 u-line-height-21px "
                "a-children-link-color-black a-children-link-color-brand-secondary:hover "
                "lrv-a-children-link-decoration-underline:hover lrv-u-display-block a-truncate-ellipsis-2line "
                "u-max-width-397 u-max-width-230@tablet-only u-max-width-300@mobile-max")
song = soup.find_all(name="h3", class_=song_class)
artist = soup.find_all(name='span', class_=artist_class)
hot_100_li = [f"{i+1}) {artist[i].get_text().strip()} - {song[i].get_text().strip()}" for i in range(len(artist))]
# for s in hot_100_li:
#     print(s)
# print(hot_100_li)







# ----------------------------------------------- TESTING ----------------------------------------------- #
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.get_text().strip() for song in song_names_spans]
# print(song_names)


# for i in range(len(artist)):
#     print(artist[i].get_text().strip())
#     print(song[i].get_text().strip())
# for a in artist:
#     print(a.get_text().strip())
# for s in song:
#     print(s.get_text().strip())
