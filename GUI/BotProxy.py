from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv
from multiprocessing import Pool, Manager

# Set up the proxy list
proxy_list = ["129.205.244.158:1080", "181.233.94.19:5678", "120.224.124.14:7891", "217.182.74.56:9100", "171.241.28.195:5611", "34.86.56.41:8080"]

# Write the proxy list to a file
with open('proxy_list.txt', 'w') as f:
    f.writelines("%s\n" % proxy for proxy in proxy_list)

def run_chrome(proxy, success_list):
    try:
        # Set the proxy for the current iteration
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % proxy)
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome = webdriver.Chrome(options=chrome_options)

        # Navigate to the website with the current instance of Chrome
        chrome.get("https://www.whatsmyip.org")

        # Check if the page loaded successfully
        if "404 Not Found" in chrome.page_source:
            raise Exception("Page not found error")

        # Click size
        size_button = chrome.find_elements(By.CSS_SELECTOR, '.size-grid-dropdown')
        for size_button in size_button:
            if size_button.text == 'CM 29.5':
                size_button.click()
                break
        time.sleep(2)

        # Click buy button
        size_button = chrome.find_elements(By.CSS_SELECTOR, '.buying-tools-cta-button')
        for size_button in size_button:
            if size_button.text == 'Comprar $4,399.00':
                size_button.click()
                break

        # Print a message and add the proxy to the success list
        print(f"Proxy {proxy} se ejecutó con éxito!!")
        success_list.append(proxy)

    except Exception as e:
        print(f"Error en proxy {proxy} ({time.strftime('%Y-%m-%d %H:%M:%S')}): {e}")

    finally:
        # Close the current window
        chrome.quit()

if __name__ == '__main__':
    # Create a pool of processes
    with Manager() as manager:
        # Create an empty list to store successful proxies
        success_list = manager.list()
        
        # Run the function for each proxy in parallel
        with Pool(processes=len(proxy_list)) as pool:
            pool.starmap(run_chrome, [(proxy, success_list) for proxy in proxy_list])
        
        # Print the successful proxies
        print("Proxies ejecutados con éxito:")
        for proxy in success_list:
            print(proxy)