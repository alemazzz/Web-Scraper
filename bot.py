import requests, argparse, sys
from bs4 import BeautifulSoup

# Aggiungi command-line arguments:
parser = argparse.ArgumentParser()

parser.add_argument("-w", "--write",action="store_true", dest="write", help="write the html in a txt file")
parser.set_defaults(write=False)
    
args = parser.parse_args()


def main():
    product = get_product()
    subito_url = f'https://www.subito.it/annunci-italia/vendita/usato/?q={product}'
    
    # Richiede html di subito       
    try:
        response = requests.get(subito_url)
    except Exception:
        sys.exit("Error occurred, maybe you are not connected to internet?")
    
    info = get_info(response)
    
    # Scrive l'html in un file txt se occorre
    if args.write == True:
        with open('html.txt', "w") as file:
            file.write(response.text)
    
    for link in info:
        # Stampa le informazioni per ogni prodotto
        print(f"\nNome del prodotto: {info[link][0]}")
        print(f"Prezzo: {info[link][1]}")
        print(f"Stato del prodotto: {info[link][2]}")
        print(f"Link diretto: {link}\n")
            
def get_info(response):
    info = {}
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', class_='SmallCard-module_link__hOkzY')

    # Estrai gli attributi 'nome, prezzo, stato, link' di ciascun prodotto
    for link in links:
        href = link.get('href')
        object = link.find_next('h2', class_='ItemTitle-module_item-title__VuKDo')
        price = link.find_next('p', class_='index-module_price__N7M2x').text
        
        # Aggiusta i vari attributi dei prodotti
        object_name = object.text
        
        if "Venduto" in price:
            object_state = "Venduto"
            price = price.replace("Venduto", "")
        elif "Spedizione disponibile" in price:
            object_state = "Spedizione disponibile"
            price = price.replace("Spedizione disponibile", "")
        else:
            object_state = "Sconosciuto"

        # Salva le informazioni per ogni prodotto
        info[href] = [object_name, price, object_state]
    
    return info
    
# Ricerca il prodotto che vuole l'utente:
def get_product():
    return input("Cosa stai cercando? (subito.it) ").replace(" ", "+")
    
    
if __name__ == "__main__":
    main()
