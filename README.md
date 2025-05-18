<img src="https://github.com/user-attachments/assets/c309dfe5-17e7-4a65-a266-b8d85939f877" width="300" />

# Giveaway Scanner

Giveaway Scanner is a Python command-line tool designed to scrape and display active giveaways from [GiveawayBase.com](https://giveawaybase.com/). It supports keyword filtering, pagination, and provides a clean, colorful terminal interface for easy browsing of giveaways.

---

## Features

* Scrapes active giveaways from multiple pages on GiveawayBase.
* Supports filtering giveaways by custom keywords or a curated list of popular keywords.
* Pagination support for browsing results in manageable chunks.
* Minimum results per page threshold to filter out less relevant pages.
* User-friendly terminal interface with clear controls.
* Color-coded output for improved readability.

---
## Update
```

1. give.py - not updated, works as intended
2. give-send.py - works 24/7 and emails you for any new give aways found - saving those found to .json file
```

For give-send.py, make sure you include a .env file ``nano .env`` or create .env file if on windows

.env should look like this:
```
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_email_password
RECEIVER_EMAIL=recipient_email@gmail.com
```
---


## Installation

1. Clone this repository or download the script file.

2. Ensure you have Python 3.6 or newer installed.

3. Install the required dependencies using pip:

```bash
pip install requests beautifulsoup4 tqdm pyfiglet colorama
```

---

## Usage

Run the script in your terminal:

```bash
python give.py
```

The program will prompt you to choose a filtering mode:

1. Enter your own keyword(s) — input comma-separated terms to filter giveaways.
2. Select from a predefined list of 20 popular keywords.
3. Show all giveaways without any filtering.

Next, specify the minimum number of results required per page to include giveaways from that page.

The scanner then retrieves and displays giveaways matching your criteria, presenting them in pages of 10 entries each. Use the following controls:

* **Enter**: Next page
* **b**: Previous page
* **q**: Quit the program

---

## How It Works

* The script requests pages from GiveawayBase's active giveaways section.
* It parses giveaway titles, links, and dates using BeautifulSoup.
* Filters giveaways based on the selected keywords.
* Continues fetching pages until no more results are available or an error occurs.
* Displays giveaways page by page with simple navigation controls.

---

## Dependencies

* [requests](https://pypi.org/project/requests/) – for HTTP requests
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) – for parsing HTML
* [tqdm](https://pypi.org/project/tqdm/) – for progress bars
* [pyfiglet](https://pypi.org/project/pyfiglet/) – for ASCII art title
* [colorama](https://pypi.org/project/colorama/) – for colored terminal output

---

## Notes

* The script respects server load by adding small delays between requests.
* If network issues or invalid pages are encountered, the scan stops gracefully.
* Keyword filtering is case-insensitive.
* Pagination controls help navigate large result sets efficiently.

---
# Contributing
Contributions are welcome! If you'd like to suggest improvements, report bugs, or add new features, please do so. Forks are not welcome.


