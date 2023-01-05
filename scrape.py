PFDB_BASE = 'http://www.profightdb.com'
PFDB_PREFIX = 'http://www.profightdb.com/cards/pg'
PFDB_SUFFIX = '-no.html'
LAST_PAGE = 4664

import requests
from bs4 import BeautifulSoup
import textwrap

class Card:
    def __init__(self, date, promotion, name, location, matches):
        self.date = date
        self.promotion = promotion
        self.name = name
        self.location = location
        self.matches = matches

    def __str__(self):
        matches = ''
        wrapper = textwrap.TextWrapper(initial_indent = '\t', subsequent_indent = '\t')
        for match in self.matches:
            matches += '{0}\n'.format(match.__str__())
        matches = matches[:-1]

        return 'Date: {0}\nPromotion: {1}\nName: {2}\nLocation: {3}\nMatches:\n{4}'.format(
            self.date,
            self.promotion,
            self.name,
            self.location,
            textwrap.indent(matches, '\t')
        )

class Match:
    def __init__(self, order, winner, victory_type, losers, duration, titles):
        self.order = order
        self.winner = winner
        self.victory_type = victory_type
        self.losers = losers
        self.duration = duration
        self.titles = titles

    def __str__(self):
        return 'Order: {0}\nWinner: {1}\nVictory Type: {2}\nLosers: {3}\nDuration: {4}\nTitles: {5}\n'.format(
            self.order,
            self.winner,
            self.victory_type,
            self.losers,
            self.duration,
            self.titles
        )

class Wrestler:
    def __init__(self, name, _id):
        self.name = name
        self._id = _id

    def __str__(self):
        return '{0} - {1}'.format(
            str(self._id),
            self.name
        )

def scrape_page(page):
    response = requests.get(PFDB_PREFIX + str(page) + PFDB_SUFFIX)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('div', attrs={'class':'table-wrapper'})
    rows = table.find_all('tr', attrs={'class': 'gray'})
    
    cards = []
    for row in rows:
        data = row.find_all('td')
        link = data[2].find('a', href=True)['href']

        card = Card(
            data[0].text.strip(),
            data[1].text.strip(),
            data[2].text.strip(),
            data[3].text.strip(),
            scrape_card(PFDB_BASE + link)
        )
        cards.append(card)

    return cards

def class_not_head(tag):
    return tag.name == 'tr' and tag.get('class') != 'head'

def scrape_card(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('div', attrs={'class': 'table-wrapper'})
    rows = table.find_all(class_not_head)[1:]

    matches = []
    for row in rows:
        data = row.find_all('td')
        match = Match(
            data[0].text.strip(),
            data[1].text.strip(),
            data[2].text.strip(),
            data[3].text.strip(),
            data[4].text.strip(),
            data[6].text.strip(),
        )
        matches.append(match)
    return matches