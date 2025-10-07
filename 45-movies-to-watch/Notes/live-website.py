from bs4 import BeautifulSoup
import requests

scrape_site = "https://news.ycombinator.com/news"
scrape_site2 = "https://appbrewery.github.io/news.ycombinator.com/"

def write_site(site):
    response = requests.get(site)
    with open('website.html', 'w') as f:
        f.write(response.text)


# write_site(scrape_site2)

with open('website2.html') as f:
    data = f.read()
soup = BeautifulSoup(data, 'html.parser')
# article_text = soup.find(name='span', class_='title_line')
# print(article_text.next_element())

# article_tag = soup.find(name='a', class_='storylink')
# article_text = article_tag.get_text()
# article_link = article_tag.get('href')
# article_upvote = soup.find(name='span', class_='score').get_text()
# print(article_text)
# print(article_link)
# print(article_upvote)

article_texts = []
article_links = []
articles = soup.find_all(name='a', class_='storylink')
for tag in articles:
    text = tag.get_text()
    article_texts.append(text)
    link = tag.get('href')
    article_links.append(link)

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name='span', class_='score')]

print(article_texts)
print(article_links)
print(article_upvotes)

max_upvote = max(article_upvotes)
max_index = article_upvotes.index(max_upvote)
print(max_index)
print(f"Article with the most upvotes\nTitle: {article_texts[max_index]}\n"
      f"Link: {article_links[max_index]}\nUpvotes: {article_upvotes[max_index]}")

