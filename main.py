from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service #inicializa e configura o chromedriver
from selenium.webdriver.common.by import By #ajuda a localizar elementos na página pelo ID, nome, etc.
from selenium.webdriver.support.ui import WebDriverWait #esperar a página carregar completamente
from selenium.webdriver.support import expected_conditions as EC #para esperar o elemento aparecer
import time
import openpyxl #biblioteca para manipular arquivos no excel.

# Configurar o WebDriver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()

#Categorias
urls_categorias = {
    "Música": "https://www.youtube.com/feed/trending?bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D",
    "Jogos": "https://www.youtube.com/feed/trending?bp=4gIcGhpnYW1pbmdfY29ycHVzX21vc3RfcG9wdWxhcg%3D%3D",
    "Filmes": "https://www.youtube.com/feed/trending?bp=4gIKGgh0cmFpbGVycw%3D%3D"
}

#Coletar o dados das categorias.
data = []

for category, url in urls_categorias.items():
    try:
        navegador.get(url)
        time.sleep(3)

        videos = navegador.find_elements(By.XPATH, "//ytd-video-renderer")[:3] #seletor do yt para localizar os vídeos que aparecem.
        for video in videos:
            try: #utilizei o inspecionar da própria página do YT para enconrtar o XPATH e então ele poder coletar e colocar no excel.
                title = video.find_element(By.XPATH, ".//a[@id='video-title']").text
                views = video.find_element(By.XPATH, ".//span[contains(text(), 'visualizações')]").text
                channel = video.find_element(By.XPATH, ".//a[@class='yt-simple-endpoint style-scope yt-formatted-string']").text
                posted_time = video.find_element(By.XPATH, ".//div[@id='metadata-line']/span[2]").text
                video_url = video.find_element(By.XPATH, ".//a[@id='video-title']").get_attribute("href")
                thumbnail_url = video.find_element(By.XPATH, ".//img").get_attribute("src")

                data.append([category, title, views, channel, posted_time, video_url, thumbnail_url])
            except Exception as e:
                print("Erro ao extrair dados de um vídeo:", e)  #usei o except para me ajuda a saber se o código está funcionando ou não.
    except Exception as e:
        print(f"Erro ao acessar a categoria '{category}':", e)
        continue

# Salvar os dados no Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Dados Extraídos"
ws.append(["Categoria", "Título do Vídeo", "Visualizações", "Canal", "Tempo de Postagem", "URL do Vídeo", "URL da Thumbnail"])

for row in data:
    ws.append(row)

wb.save("dados_extraidos.xlsx")
print("Dados salvos em 'dados_extraidos.xlsx'")

# Fechar o navegador
navegador.quit()