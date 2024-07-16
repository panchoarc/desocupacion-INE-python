import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def configure_download_directory():
    current_dir = os.path.dirname(__file__)
    download_dir = os.path.join(current_dir, 'csv')
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    return download_dir

def initialize_driver(download_dir):
    chrome_options = webdriver.ChromeOptions()
    
    prefs = {"download.default_directory": download_dir}
    chrome_options.add_experimental_option("prefs", prefs)
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def open_website(driver, url):
    driver.get(url)
    
def select_language(driver):
    selectedLanguage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Español")))
    actions = ActionChains(driver)
    actions.move_to_element(selectedLanguage).click().perform()

def click_export_button(driver):
    export_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "menubar-export")))
    actions = ActionChains(driver)
    actions.move_to_element(export_button).perform()

def click_csv_export(driver):
    csv_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "menuitemExportCSV")))
    actions = ActionChains(driver)
    actions.move_to_element(csv_button).click().perform()

def switch_to_popup_frame(driver):
    all_handles = driver.window_handles
    for handle in all_handles:
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)
            break
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "DialogFrame")))
    driver.switch_to.frame(iframe)

def download_file(driver):
    download_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "_ctl12_btnExportCSV")))
    actions = ActionChains(driver)
    actions.move_to_element(download_button).click().perform()
    time.sleep(5)  # Ajusta el tiempo según sea necesario

def rename_downloaded_file(download_dir, new_filename):
    files = os.listdir(download_dir)
    for file in files:
        if file.endswith('.csv'):  # Ajusta la condición según la extensión del archivo descargado
            original_file_path = os.path.join(download_dir, file)
            new_file_path = os.path.join(download_dir, new_filename)
            if os.path.exists(new_file_path):
                os.remove(new_file_path)  # Elimina el archivo existente
            os.rename(original_file_path, new_file_path)
            print(f'Archivo renombrado de "{os.path.basename(original_file_path)}" a "{os.path.basename(new_file_path)}"')
            break



def main():
    try:
        download_dir = configure_download_directory()
        driver = initialize_driver(download_dir)
        url = "https://stat.ine.cl/Index.aspx?DataSetCode=ENE_TD"
        open_website(driver, url)
        select_language(driver)
        click_export_button(driver)
        click_csv_export(driver)
        switch_to_popup_frame(driver)
        download_file(driver)
        rename_downloaded_file(download_dir, 'Tasa_de_desocupación_INE.csv')

    except Exception as e:
        print(f'Error: {e}')

    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()
