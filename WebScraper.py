import requests
from bs4 import BeautifulSoup

def main():
    product = get_product()
    subito_url = f'https://www.subito.it/annunci-italia/vendita/informatica/?q={product}'

    response = requests.get(subito_url)
    if response.status_code == 200:
        print_info(response)
    else:
        print("Not found.")
        
def print_info(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    objects = soup.find_all('h2', class_='ItemTitle-module_item-title__VuKDo')

    for object in objects:
        # Estrai le informazioni desiderate per ogni oggetto
        object_name = object.text
        price = object.find_next('p', class_='index-module_price__N7M2x').text
        if "Venduto" in price:
            object_state = "Venduto"
            price = price.replace("Venduto", "")
        elif "Spedizione disponibile" in price:
            object_state = "Spedizione disponibile"
            price = price.replace("Spedizione disponibile", "")

        # Stampa le informazioni per ogni oggetto
        print("Nome dell'oggetto:", object_name)
        print("Prezzo:", price)
        print("Stato dell'oggetto:", object_state)
        print("\n")
    
# Get the product that the user wants:
def get_product():
    product = input("Cosa stai cercando?(subito.it) ")
    return product.replace(" ", "%20")
    print("Ok ricerco...")
    
    
if __name__ == "__main__":
    main()