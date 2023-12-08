# Subito.it Web Scraping Bot

## Description
This Python script is a simple web scraping bot designed to retrieve and display information about computer-related products listed on Subito.it. The script uses the BeautifulSoup library for parsing HTML content and the Requests library for making HTTP requests. The user can specify the product they are searching for, and the bot will fetch relevant information from the Subito.it website.

## Usage

### Prerequisites
- Python 3.x
- Required Python packages: `requests`, `beautifulsoup4`

### Installation of Dependencies
```bash
pip install requests beautifulsoup4
```

### Command-line Arguments
- `-w` or `--write`: Optional argument to write the HTML content to a text file named `html.txt`.

### Running the Script
```bash
python script_name.py [-w] 
```

### Example
```bash
python subito_scraper.py -w
```

## Script Overview

1. The script takes a user input for the product they are searching for on Subito.it.

2. It constructs the URL for the search on Subito.it.

3. It sends an HTTP request to Subito.it and retrieves the HTML content.

4. Optionally, it writes the HTML content to a text file if the `-w` argument is provided.

5. I will add more command-line argument in the future

6. It parses the HTML content using BeautifulSoup to extract relevant information about the listed products.

7. It prints the name, price, and state of each product, along with a direct link to the product.

## Notes
- The script uses command-line arguments to provide additional functionality, such as writing the HTML content to a file.

- The `get_product()` function takes user input for the product to search for, replacing spaces with `%20` for URL compatibility.

- The script identifies the state of each product as "Venduto" (Sold), "Spedizione disponibile" (Shipping available), or "Sconosciuto" (Unknown).

- The extracted information is printed to the console.

- If the HTTP request to Subito.it is successful (status code 200), the script proceeds to extract and display information. Otherwise, it prints "Not found."
```