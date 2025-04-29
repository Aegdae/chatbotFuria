from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Web Scraping para pegar dados dos jogadores atuais

def getFuriaRoster():
    options = webdriver.ChromeOptions()
    options.headless = False
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    url = 'https://www.hltv.org/team/8297/furia'
    driver.get(url)

    
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Allow all cookies')]"))
        ).click()
    except:
        print("")

    
    time.sleep(3)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    roster = []

    
    players = soup.find_all('a', class_='col-custom')

    for player in players:
        nickname = player.get('title')
        if nickname:
            roster.append(nickname)

    driver.quit()

    return roster



# WebScraping para pegar os dados das proximas partidas

def getFuriaUpcomingMatches():
    options = webdriver.ChromeOptions()
    options.headless = False
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    url = 'https://www.hltv.org/team/8297/furia'
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Allow all cookies')]"))
        ).click()
    except:
        print("Botão de cookies não apareceu")

    time.sleep(3)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    upcoming_matches = []

    matches_box = soup.find('div', id='matchesBox')

    upcoming_section = matches_box.find('h2', string='Upcoming matches for FURIA')
    if upcoming_section:
        upcoming_container = upcoming_section.find_next_sibling()
        if upcoming_container and 'empty-state' in upcoming_container.get('class', []):
            upcoming_matches.append("Não há partidas futuras agendadas para a FURIA.")
        else:
            upcoming_table = upcoming_container.find('table', class_='table-container match-table')
            if upcoming_table:
                for row in upcoming_table.find_all('tr', class_='team-row'):
                    date = row.find('td', class_='date-cell').text.strip()
                    teams = row.find('td', class_='team-center-cell')
                    team1 = teams.find('a', class_='team-name team-1').text.strip()
                    team2 = teams.find('a', class_='team-name team-2').text.strip()
                    match_link = row.find('a', class_='stats-button')['href']
                    event = row.find_previous('tr', class_='event-header-cell').text.strip()
                    upcoming_matches.append({
                        'date': date,
                        'team1': team1,
                        'team2': team2,
                        'event': event,
                        'match_link': f"https://www.hltv.org{match_link}"
                    })

    driver.quit()

    if not upcoming_matches:
        upcoming_matches.append("Não há partidas futuras agendadas para a FURIA.")  


# WebScraping para pegar os dados das ultimas partidas da Furia


def getFuriaRecentMatches():
    options = webdriver.ChromeOptions()
    options.headless = False
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    url = 'https://www.hltv.org/team/8297/furia'
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Allow all cookies')]"))
        ).click()
    except:
        print("Erro ao aceitar cookies")

    time.sleep(3)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    recent_matches = []

    matches_box = soup.find('div', id='matchesBox')

    recent_section = matches_box.find('h2', string='Recent results for FURIA')
    if recent_section:
        recent_table = recent_section.find_next_sibling('table', class_='table-container match-table')
        current_event = ""
        for row in recent_table.find_all('tr'):
            event_header = row.find('th', class_='text-ellipsis')
            if event_header:
                current_event = event_header.text.strip()
                continue
            if 'team-row' in row.get('class', []):
                date = row.find('td', class_='date-cell').text.strip()
                teams = row.find('td', class_='team-center-cell')
                team1 = teams.find('a', class_='team-name team-1').text.strip()
                team2 = teams.find('a', class_='team-name team-2').text.strip()
                score = teams.find('div', class_='score-cell').text.strip()
                match_link = row.find('a', class_='stats-button')['href']
                recent_matches.append({
                    'date': date,
                    'team1': team1,
                    'team2': team2,
                    'score': score,
                    'event': current_event,
                    'match_link': f"https://www.hltv.org{match_link}"
                })

    driver.quit()
    return recent_matches