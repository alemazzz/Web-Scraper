import requests, argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()

parser.add_argument("-w", "--write",action="store_true", dest="write", help="write the html in a txt file")
parser.set_defaults(write=False)
    
args = parser.parse_args()


def main():
    product = get_product()
    subito_url = f'https://www.subito.it/annunci-italia/vendita/informatica/?q={product}'

    response = requests.get(subito_url)
    if args.write == True:
        with open('html.txt', "w") as file:
            file.write(response.text)
            
    if response.status_code == 200:
        print_info(response)
    else:
        print("Not found.")
        
def print_info(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', class_='SmallCard-module_link__hOkzY')

    # Estrai gli attributi 'href' da ciascun link
    for link in links:
        href = link.get('href')
        object = link.find_next('h2', class_='ItemTitle-module_item-title__VuKDo')
        price = object.find_next('p', class_='index-module_price__N7M2x').text
        
        # Estrai le informazioni desiderate per ogni oggetto
        object_name = object.text
        
        if "Venduto" in price:
            object_state = "Venduto"
            price = price.replace("Venduto", "")
        elif "Spedizione disponibile" in price:
            object_state = "Spedizione disponibile"
            price = price.replace("Spedizione disponibile", "")
        else:
            object_state = "Sconosciuto"

        # Stampa le informazioni per ogni oggetto
        print("\nNome dell'oggetto:", object_name)
        print("Prezzo:", price)
        print("Stato dell'oggetto:", object_state)
        print(f"Link diretto: {href}\n")
    
# Get the product that the user wants:
def get_product():
    product = input("Cosa stai cercando?(subito.it) ")
    return product.replace(" ", "%20")
    
    
if __name__ == "__main__":
    main()