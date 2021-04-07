import requests
from bs4 import BeautifulSoup

# Initialization
################# Markdown ##################
# markdown_text = ''                                            # Markdown string
markdown_dict = {                                               # Markdown Dictionary
    'id': [], 'title': [],
    'subtitle': [], 'description': []}
problem_id = '2'                                                # Problem ID/Number
################# Soup ######################
url = 'https://projecteuler.net/problem={}'.format(problem_id)  # URL to scrape
page = requests.get(url).content                                # HTML Content
soup = BeautifulSoup(page, 'html.parser')                       # Soup

# Filtering
content = soup.find('div', id="content")
title = content.find('h2').text
subtitle = content.find('h3').text
paragraphs = '\n'.join(map(lambda p: p.text, content.find_all('p')))

# Adding entry to dictionary
markdown_dict['id'].append(problem_id)
markdown_dict['title'].append(title)
markdown_dict['subtitle'].append(subtitle)
markdown_dict['description'].append(paragraphs)


