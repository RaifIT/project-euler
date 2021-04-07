import os
import requests
from bs4 import BeautifulSoup

def run():
    # Initialization
    ################# Markdown ##################
    markdown_dict = {}                                                          # Markdown Dictionary
    problem_id = 3                                                              # Problem number
    scrape(markdown_dict, problem_id)                                           # Scrape the webpage and add to dict


def scrape(markdown_dict, problem_id):
    problem_id_str = str(problem_id)                                            # Problem ID/Number
    ################# Soup ######################
    url = 'https://projecteuler.net/problem={}'.format(problem_id)              # URL to scrape
    page = requests.get(url).content                                            # HTML Content
    soup = BeautifulSoup(page, 'html.parser')                                   # Soup
    filter_soup(soup, markdown_dict, problem_id)                                # Filter the soup and create the MD
    # save_md_to_file(markdown_dict, problem_id)

    print(markdown_dict[3]['description'])


def save_md_to_file(markdown_dict, problem_id):
    # Save in problem folder
    path = '../{}/'.format(str(problem_id).zfill(3))
    if not os.path.isdir(path):
        os.mkdir(path)
    with open(path + 'README.MD', 'w+') as file:
        file.write(markdown_dict[problem_id]['md'])


def filter_soup(soup, markdown_dict, problem_id):
    # Filtering
    content = soup.find('div', id="content")                                    # Isolate the problem details
    title = content.find('h2').text                                             # Problem title
    subtitle = content.find('h3').text                                          # Problem subtitle (i.e. Problem 2)
    description = '\n'.join(map(lambda p: p.text, content.find_all('p')))       # Problem description
    markdown_text = '# {}\n## {}\n\n{}'.format(title, subtitle, description)    # Markdown string

    # Add entry to dictionary (which is useless for now, but might have use in future revisions
    details = {'title': title,
            'subtitle': subtitle, 'description': description, 'md': markdown_text}
    markdown_dict[problem_id] = details


run()