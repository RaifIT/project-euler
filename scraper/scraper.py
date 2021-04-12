import os
import requests
import json
from bs4 import BeautifulSoup


def run():
    markdown_dict = {}  # Markdown Dictionary
    from_problem, to_problem = 1, 6  # Range of problems to scrape
    for p in range(from_problem, to_problem + 1):
        scrape(markdown_dict, p)  # Scrape the webpage and add to dict
        save_md_to_file(markdown_dict, p)  # Save problem MD in problem folder
    save_dict_to_json(markdown_dict)  # Save dictionary to a JSON


def scrape(markdown_dict, problem_id):
    url = 'https://projecteuler.net/problem={}'.format(problem_id)  # URL to scrape
    page = requests.get(url).content  # HTML Content
    soup = BeautifulSoup(page, 'html.parser')  # Soup
    filter_soup(soup, markdown_dict, problem_id)  # Filter the soup and create the MD


def filter_soup(soup, markdown_dict, problem_id):
    content = soup.find('div', id="content")  # Isolate the problem details
    title = content.find('h2').text  # Problem title
    subtitle = content.find('h3').text  # Problem subtitle (i.e. Problem 2)
    description = '\n'.join(map(lambda p: p.text, content.find_all('p')))  # Problem description
    markdown_text = '# {}\n## {}\n\n{}'.format(title, subtitle, description)  # Markdown string
    details = {'title': title,  # Create new entry
               'subtitle': subtitle, 'description': description, 'md': markdown_text}
    markdown_dict[problem_id] = details  # Add entry to dictionary


def save_md_to_file(markdown_dict, problem_id):
    path = '../{}/'.format(str(problem_id).zfill(3))  # Directory Path
    if not os.path.isdir(path):  # Check if directory exists
        os.mkdir(path)  # Create it if not
    with open(path + 'README.MD', 'w+') as file:  # Create/Open README.MD
        file.write(markdown_dict[problem_id]['md'])  # Write problem description to file


def save_dict_to_json(markdown_dict):
    with open('dictionary.json', 'w+') as file:  # Create/Open dictionary.json
        json.dump(markdown_dict, file, indent=5)  # Write dictionary to JSON


run()
