import requests
from bs4 import BeautifulSoup
import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

POPULAR_KEYWORDS = [
    "Gaming PC", "Steam Deck", "RTX", "Razer", "Logitech", "Headset", "Keyboard", "Mouse",
    "Monitor", "GPU", "PS5", "Xbox", "Gift Card", "Amazon", "Meta Quest",
    "Laptop", "Smartphone", "Microphone", "Electric Scooter", "Eyewear"
]

def fetch_all_active_giveaways(keyword_filters=None, min_results=1):
    base_url = 'https://giveawaybase.com/category/active-giveaways/page/{}/'
    headers = {'User-Agent': 'Mozilla/5.0'}

    giveaways = []
    page = 1

    while True:
        url = base_url.format(page)
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article')

        if not articles:
            break

        page_results = []
        for article in articles:
            title_tag = article.find('h2')
            link_tag = article.find('a', href=True)
            if title_tag and link_tag:
                title = title_tag.get_text(strip=True)
                link = link_tag['href']
                if not keyword_filters or any(kw.lower() in title.lower() for kw in keyword_filters):
                    page_results.append({'title': title, 'link': link})

        if len(page_results) >= min_results:
            giveaways.extend(page_results)

        page += 1

    return giveaways

def choose_keyword_mode():
    print(Fore.YELLOW + "\n Choose input mode for giveaway keyword filtering:")
    print(Fore.CYAN + "1. Enter your own keyword(s) (comma-separated)")
    print(Fore.CYAN + "2. Select from the 20 most common keywords")
    print(Fore.CYAN + "3. Show all giveaways (no filtering)")

    try:
        choice = int(input(Fore.GREEN + "\nEnter your choice (1-3): ").strip())
        if choice == 1:
            keywords = input("Enter your own keyword(s), separated by commas: ").strip()
            return [k.strip() for k in keywords.split(',') if k.strip()]
        elif choice == 2:
            return choose_from_popular_keywords()
        elif choice == 3:
            return None
        else:
            print("Invalid choice. No keyword filtering will be used.")
            return None
    except ValueError:
        print("Invalid input. No keyword filtering will be used.")
        return None

def choose_from_popular_keywords():
    print(Fore.YELLOW + "\nSelect one of the 20 most common keywords:")
    for i, kw in enumerate(POPULAR_KEYWORDS, start=1):
        print(Fore.CYAN + f"{i}. {kw}")
    try:
        choice = int(input(Fore.GREEN + f"\nEnter your choice (1-{len(POPULAR_KEYWORDS)}): ").strip())
        if 1 <= choice <= len(POPULAR_KEYWORDS):
            return [POPULAR_KEYWORDS[choice - 1]]
        else:
            print("Invalid choice. No keyword filtering will be used.")
            return None
    except ValueError:
        print("Invalid input. No keyword filtering will be used.")
        return None

def print_title():
    ascii_title = pyfiglet.figlet_format("Giveaway Scanner")
    print(Fore.MAGENTA + ascii_title)
    print(Fore.BLUE + Style.BRIGHT + "Made by github.com/Cr0mb/\n")

if __name__ == "__main__":
    print_title()
    keyword_filters = choose_keyword_mode()

    try:
        min_results = int(input(Fore.YELLOW + "Minimum results per page to include (default 1): ").strip() or 1)
    except ValueError:
        min_results = 1

    if keyword_filters:
        print(Fore.MAGENTA + f"\n⏳ Fetching giveaways filtered by: {', '.join(keyword_filters)}...\n")
    else:
        print(Fore.MAGENTA + "\n⏳ Fetching all giveaways..\n")

    giveaways = fetch_all_active_giveaways(keyword_filters=keyword_filters, min_results=min_results)

    if giveaways:
        print(Fore.GREEN + f"Found {len(giveaways)} matching giveaways:\n")
        for idx, giveaway in enumerate(giveaways, start=1):
            print(Fore.CYAN + f"{idx}. {giveaway['title']}\n   Link: {giveaway['link']}\n")
    else:
        print(Fore.RED + "No matching giveaways found.")

