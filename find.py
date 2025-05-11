from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Link iniziale
MAPS_LINK = "https://www.google.com/maps"

# Configura e avvia il driver Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 20)

# Vai a Google Maps
driver.get(MAPS_LINK)

# Accetta i cookie se il bottone è presente
try:
    accetta_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[.//span[contains(text(), 'Accetta tutto')]]")))
    accetta_btn.click()
    print("Bottone 'Accetta tutto' cliccato.")
except Exception as e:
    print(f"Nessun bottone 'Accetta tutto' trovato (o già accettato). Errore: {e}")

# Inserisci la ricerca nella barra
search_box = wait.until(EC.presence_of_element_located((By.ID, "searchboxinput")))
search_box.clear()
search_box.send_keys("Concessionaria Auto, Verona")

# Clicca sul bottone di ricerca
search_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@aria-label='Cerca']")))
search_button.click()

# Attendi che la sezione principale della pagina si carichi
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='main']")))
time.sleep(3)  # Attendere ulteriormente per caricare completamente i risultati

# Prova a prendere le schede dei risultati
lista_concessionarie = driver.find_elements(By.CLASS_NAME, "Nv2PK")

# Controlla se sono stati trovati risultati
print(f"\nTrovate {len(lista_concessionarie)} concessionarie:\n")

# Se trovi dei risultati, estrai i nomi
if lista_concessionarie:
    for i, concessionaria in enumerate(lista_concessionarie, 1):
        try:
            nome = concessionaria.find_element(
                By.XPATH, ".//div[contains(@class,'qBF1Pd') or contains(@class,'fontHeadlineSmall')]"
            ).text
        except:
            nome = concessionaria.text.split('\n')[0]  # fallback se non c'è un nome visibile
        print(f"{i}. {nome}")
        link = concessionaria.find_element(By.CLASS_NAME, "hfpxzc").get_attribute("href") 
        driver.get(link)  # Apri il link della concessionaria
        time.sleep(2)  # Attendere che il sito si apra
        driver.back()  # Torna alla scheda della concessionaria
        time.sleep(2)
        # Torna alla pagina dei risultati
else:
    print("Nessuna concessionaria trovata.")
# Chiudi il driver
print("\nChiusura del driver...")
driver.quit()
