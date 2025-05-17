<img src="https://github.com/user-attachments/assets/f0c9bba0-53ca-46fd-80f2-541d464b00ab" width="300" />


---

# Giveaway Scanner



**Giveaway Scanner** is a simple Python script that scrapes [GiveawayBase](https://giveawaybase.com) for active giveaways and filters them based on your input keywords. It helps you quickly find giveaways related to popular tech and gaming items like GPUs, gaming PCs, consoles, peripherals, and more.

---

## Features

* Scrapes all active giveaways from GiveawayBase.
* Filter giveaways by your own keywords or select from 20 popular tech/gaming-related keywords.
* Option to view all giveaways without filtering.
* Minimum results per page filter to fine-tune output.
* Clean console output with colors and ASCII art for a friendly user experience.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Cr0mb/Giveaway-Scanner.git
   cd Giveaway-Scanner
   ```

2. Install dependencies (recommended in a virtual environment):

   ```bash
   pip install requests beautifulsoup4 pyfiglet colorama
   ```

   **Dependencies:**

   * `requests`
   * `beautifulsoup4`
   * `pyfiglet`
   * `colorama`

3. Run the script:

   ```bash
   python give.py
   ```

---

## Usage

Run the script and follow the prompts to:

* Choose keyword filtering mode.
* Enter or select keywords.
* Set minimum results per page.
* View matching giveaways directly in your terminal.

---

## Keyword Filters

You can either:

* Enter custom keywords separated by commas, e.g. `GPU, PS5, headset`.
* Select from a predefined list of popular keywords related to tech and gaming:

```
Gaming PC, Steam Deck, RTX, Razer, Logitech, Headset, Keyboard, Mouse,
Monitor, GPU, PS5, Xbox, Gift Card, Amazon, Meta Quest,
Laptop, Smartphone, Microphone, Electric Scooter, Eyewear
```

* Or opt to see **all giveaways** without filtering.

---

## How It Works

* The script scrapes paginated active giveaway listings from GiveawayBase.
* It parses giveaway titles and URLs using BeautifulSoup.
* Filters giveaways by keywords if provided.
* Displays results in a colorful, readable format with numbering and direct links.

---

## Contributing

Feel free open pull requests or issues for support.



