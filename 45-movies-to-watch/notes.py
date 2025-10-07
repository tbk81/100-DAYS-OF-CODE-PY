from bs4 import BeautifulSoup
# lxml can be used as a different parser for markup langs
# import lxml


with open("website.html") as f:
    data = f.read()

# print(data)
soup = BeautifulSoup(data, "html.parser")
# print(soup.title.name)  # name of the title tage
# print(soup.title.string)  # string inside the title tag
# print(soup.prettify())  # indents the html for easy viewing
# print(soup.a)  # first anchor tag
# print(soup.li)  # first list tag
# print(soup.p)  # first paragraph tag

# all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.get_text())
#     print(tag.get('href'))  # gets the value of the attribute

# heading = soup.find(name='h1', id='name')  # soup.find finds the first attribute that appears
# print(heading)
#
# h3_heading = soup.find(name='h3', class_='heading')
# print(h3_heading)
# print(h3_heading.getText())  # can use get_text()
# print(h3_heading.get('class'))  # value of attribute
# print(h3_heading.name)  # name of the tag

company_url = soup.select_one(selector='p a')  # select will select all; this uses a css selector with 'p' and 'a' tags
print(company_url)

name = soup.select_one(selector='#name')
print(name)

headings = soup.select(".heading")
print(headings)

