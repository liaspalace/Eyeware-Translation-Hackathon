# Copyright (c) 2025, Eyeware Tech SA.
#
# All rights reserved.
#
# This sample demonstrates how to use the polling data access method.
#
# Polling is convenient in case your thread can't be blocked, and it is not critical to read the
# TrackingStateSet as soon as it is available, meaning, you can afford some latency.
#
# A typical scenario is when your thread loop is driven by other events and you want to use
# the latest TrackingStateSet in combination with said events. For example, in a game, where
# there is a logic driven by frames rendering: you don't want to block, but you want to use the
# eye tracking for some interaction in the game.
# Imports do sistema e do SDK
# Imports do sistema
import sys
import os
import time
import math
import requests

# Imports de bibliotecas externas
from PIL import Image, ImageGrab
import pytesseract

# --- Bloco de Lógica de Caminhos (ESSENCIAL) ---
# Garanta que este bloco esteja EXATAMENTE assim no seu código.

# 1. Adiciona a pasta 'samples' (um nível acima) para encontrar 'bet_sample_utils'
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

# 2. Adiciona a pasta 'package' (dois níveis acima, depois desce para 'package') para encontrar 'eyeware'
script_dir = os.path.dirname(os.path.abspath(__file__))
sdk_python_root = os.path.join(script_dir, "..", "..")
package_path = os.path.join(sdk_python_root, "package")
sys.path.append(package_path)
# --- Fim do Bloco ---

# Agora que o Python sabe onde procurar, estes imports devem funcionar:
from eyeware import beam_eye_tracker
from bet_sample_utils import (
    print_tracking_data_reception_status,
    print_latest_tracking_state_set,
    print_tracking_data_reception_status_if_changed,
)

# --- CONFIGURAÇÕES DA FIXAÇÃO ---
DWELL_TIME_SECONDS = 1.5  # Tempo em segundos que o olhar precisa ficar fixo
FIXATION_RADIUS_PIXELS = 50 # Raio em pixels de tolerância para a fixação
# -----------------------------

def extrair_texto_com_tesseract(caminho_da_imagem):
    """Usa o Tesseract OCR para extrair texto de uma imagem localmente."""
    print(f"Lendo imagem com Tesseract: {caminho_da_imagem}...")
    try:
        texto_extraido = pytesseract.image_to_string(Image.open(caminho_da_imagem), lang='eng+por')
        
        if texto_extraido and texto_extraido.strip():
            print("\n--- ✅ TEXTO ENCONTRADO (Tesseract) ---")
            print(texto_extraido.strip())
            print("--------------------------------------\n")
            return texto_extraido.strip()
        else:
            print("\n--- ❌ Nenhum texto foi detectado pelo Tesseract. ---\n")
            return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado no Tesseract: {e}")
        return None
    

def traduzir_com_tas(texto, idioma_origem='en', idioma_alvo='pt'):
    """
    Usa a API TAS diretamente, buscando a lista de servidores e testando um a um.
    """
    endpoints_url = 'https://raw.githubusercontent.com/Uncover-F/TAS/Uncover/.data/endpoints.json'
    params = {'text': texto, 'source_lang': idioma_origem, 'target_lang': idioma_alvo}
    
    print("\nBuscando lista de servidores TAS...")
    try:
        endpoints_response = requests.get(endpoints_url, timeout=10)
        if endpoints_response.status_code == 200:
            endpoints = endpoints_response.json()
        else:
            print("Não foi possível buscar a lista de servidores.")
            return None
    except Exception as e:
        print(f"Não foi possível buscar a lista de servidores: {e}")
        return None

    print("Enviando texto para tradução com a API TAS...")
    for endpoint in endpoints:
        try:
            # Adiciona a rota de tradução correta ao endpoint base
            url_completa = f"{endpoint.rstrip('/')}/translate"
            response = requests.get(url_completa, params=params, timeout=5)

            if response.status_code == 200:
                resultado = response.json()
                if resultado and 'translated_text' in resultado:
                    texto_traduzido = resultado['translated_text']
                    print("--- ✅ TRADUÇÃO (TAS) ---")
                    print(texto_traduzido)
                    print("--------------------------\n")
                    return texto_traduzido
        except requests.RequestException:
            print(f"Servidor {endpoint} falhou. Tentando o próximo...")
            continue
            
    print("--- ❌ Todos os servidores TAS falharam. ---")
    return None
    
def main():
    # --- VARIÁVEIS DE ESTADO DA FIXAÇÃO ---
    fixation_start_time = None
    last_fixation_point = None
    
    # Inicialização da API do Eye Tracker
    viewport_geometry = beam_eye_tracker.ViewportGeometry()
    viewport_geometry.point_00 = beam_eye_tracker.Point(0, 0)
    viewport_geometry.point_11 = beam_eye_tracker.Point(0, 0)
    bet_api = beam_eye_tracker.API("Python Polling Sample", viewport_geometry)
    
    last_update_timestamp_sec = beam_eye_tracker.NULL_DATA_TIMESTAMP()
    previous_status = bet_api.get_tracking_data_reception_status()
    print_tracking_data_reception_status(previous_status)

    # Loop principal
    while True:
        status = bet_api.get_tracking_data_reception_status()
        print_tracking_data_reception_status_if_changed(previous_status, status)
        previous_status = status

        if bet_api.wait_for_new_tracking_state_set(last_update_timestamp_sec, 0):
            last_received_tracking_state_set = bet_api.get_latest_tracking_state_set()
            user_state = last_received_tracking_state_set.user_state()

            if user_state.unified_screen_gaze.confidence > 0:
                current_gaze_point = (
                    int(user_state.unified_screen_gaze.point_of_regard.x),
                    int(user_state.unified_screen_gaze.point_of_regard.y)
                )
                current_time = time.time()

                if last_fixation_point is None:
                    last_fixation_point = current_gaze_point
                    fixation_start_time = current_time
                else:
                    distance = math.sqrt(
                        (current_gaze_point[0] - last_fixation_point[0])**2 + 
                        (current_gaze_point[1] - last_fixation_point[1])**2
                    )

                    if distance > FIXATION_RADIUS_PIXELS:
                        last_fixation_point = current_gaze_point
                        fixation_start_time = current_time
                    else:
                        elapsed_time = current_time - fixation_start_time
                        
                        if elapsed_time >= DWELL_TIME_SECONDS:
                            print("\n--- FIXAÇÃO DETECTADA! ACIONANDO TRADUÇÃO ---")
                            
                            try:
                                largura_captura = 500
                                altura_captura = 250
                                x1 = current_gaze_point[0] - largura_captura // 2
                                y1 = current_gaze_point[1] - altura_captura // 2
                                x2 = current_gaze_point[0] + largura_captura // 2
                                y2 = current_gaze_point[1] + altura_captura // 2

                                screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
                                nome_arquivo_screenshot = "screenshot_temp.png"
                                screenshot.save(nome_arquivo_screenshot)
                                
                                texto_encontrado = extrair_texto_com_tesseract(nome_arquivo_screenshot)
                                if texto_encontrado:
                                    traduzir_com_tas(texto_encontrado, idioma_origem='en', idioma_alvo='pt')
                                    
                            except Exception as e:
                                print(f"Erro ao processar fixação: {e}")

                            last_fixation_point = None
                            fixation_start_time = None
        
        time.sleep(0.1)

if __name__ == "__main__":
    main()
