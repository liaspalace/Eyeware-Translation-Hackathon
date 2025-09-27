---

# 📑 Sumário (Table of Contents)

### 🇧🇷 Em Português
1. [Tradutor Ocular em Tempo Real](#-tradutor-ocular-em-tempo-real)  
2. [Sobre o Projeto](#sobre-o-projeto)  
   - [Uma Escolha Consciente](#uma-escolha-consciente-código-aberto-vs-apis-comerciais)  
3. [Funcionalidades](#funcionalidades)  
4. [Tecnologias Utilizadas](#tecnologias-utilizadas)  
5. [Configuração do Ambiente](#configuração-do-ambiente)  
6. [Como Executar](#como-executar)  
7. [Use o Aplicativo](#use-o-aplicativo)  
8. [Nota Importante Sobre a Tradução](#nota-importante-sobre-a-tradução)  
9. [Autores](#autores)  

---

### 🇺🇸 In English
1. [Real-Time Eye-Tracking Translator](#-real-time-eye-tracking-translator)  
2. [About the Project](#about-the-project)  
   - [A Conscious Choice](#a-conscious-choice-open-source-vs-commercial-apis)  
3. [Features](#features)  
4. [Technologies Used](#technologies-used)  
5. [Environment Setup](#environment-setup)  
6. [How to Run](#how-to-run)  
7. [Use the Application](#use-the-application)  
8. [Important Note on Translation](#important-note-on-translation)  
9. [Authors](#authors)  

---

# Projeto Vencedor da Hackathon
# Tradutor Ocular em Tempo Real
Traduza qualquer texto na sua tela, apenas com o olhar. Este projeto, desenvolvido para uma hackathon, transforma seu rastreador ocular em uma ferramenta de tradução instantânea, utilizando tecnologias de código aberto que respeitam sua privacidade.

---

## Sobre o Projeto
Este add-on permite que o usuário traduza parágrafos em qualquer lugar da tela simplesmente ao fixar o olhar sobre eles por um instante. O texto é extraído da tela e traduzido em tempo real, com o resultado exibido no terminal.

### Uma Escolha Consciente: Código Aberto vs. APIs Comerciais
Uma decisão fundamental neste projeto foi a utilização de uma stack de tecnologias **100% gratuita e de código aberto**.  
Para o reconhecimento de texto e para a tradução, optamos por ferramentas como **Tesseract** e **LibreTranslate**.

Essa escolha foi feita para evitar a dependência de serviços comerciais (como o Google Cloud, que exigem conta de faturamento).  
Nosso objetivo: criar uma ferramenta **totalmente acessível**, sem custos para o usuário final e com mais **privacidade**.  
A consequência é que a tradução depende de instâncias públicas da comunidade, que podem apresentar instabilidade.

---

## Funcionalidades
- **Tradução por Fixação:** Mantenha o olhar fixo em um texto para acionar a tradução.  
- **Privacidade em Primeiro Lugar:** OCR 100% offline, diretamente na máquina do usuário.  
- **Controle sem as Mãos:** Sem necessidade de teclado ou mouse.  
- **Stack de Código Aberto:** Usa Tesseract + LibreTranslate (sem custos e sem chaves de API pagas).  
- **Customizável:** Ajuste do tempo de fixação e sensibilidade do cursor ocular no código.  

---

## Tecnologias Utilizadas
- **Linguagem:** Python 3.12  
- **Rastreamento Ocular:** Beam Eye Tracker SDK  
- **OCR:** Tesseract OCR  
- **Tradução:** API Pública do LibreTranslate  
- **Bibliotecas:** Pillow, Pytesseract, Requests  

---

## Configuração do Ambiente

### 1. Instale o Beam Eye Tracker
Baixe e instale o software no site oficial da Eyeware.

### 2. Instale o Tesseract OCR
- Baixe o instalador para Windows: https://github.com/UB-Mannheim/tesseract/wiki
  
  Procure por tesseract-ocr-w64-setup-5.5.0.20241111.exe (64 bit)
  
- Durante a instalação:  
  - Adicione pacotes de idiomas (ex: English e Portuguese).  
  - Certifique-se de marcar a opção para adicionar o Tesseract ao **PATH** do sistema.  

### 3. Instale as Dependências Python
Com o Python 3.12 instalado, abra o terminal na pasta raiz deste projeto e execute o seguinte comando para instalar todas as bibliotecas necessárias de uma vez:

```bash
pip install -r requirements.txt
```
## Como Executar

### 1. Inicie o Eye Tracker
Primeiro, certifique-se de que o software **Beam Eye Tracker** está aberto e rastreando seu rosto ativamente.

### 2. Execute o Programa
Dê um clique duplo no arquivo **run.bat** para iniciar o projeto.  
Um terminal será aberto automaticamente.

## Use o Aplicativo

### 1. Olhe para qualquer texto na sua tela.

### 2. Fixe o olhar por 1.5 segundos.

### 3.A tradução aparecerá no terminal que está executando o script principal.

## Nota Importante Sobre a Tradução

Este projeto utiliza instâncias públicas e gratuitas da API LibreTranslate.
Como são serviços mantidos pela comunidade, podem ficar sobrecarregados ou temporariamente offline.

Se a tradução falhar, isso geralmente significa instabilidade dos servidores.

O código tentará automaticamente outras opções da lista.

Se todas falharem, aguarde um pouco e tente novamente.

## Autores
Giulia Meninel Mattedi

Lucas Ferri dos Santos

Pedro Huck Henrique

Sthefany Viveiros Cordeiro

Túlio Gonçalves Vieira

# Hackathon Winner Project 
# Real-Time Eye-Tracking Translator
Translate any text on your screen, just with your gaze.  
This project, developed for a hackathon, turns your eye tracker into an instant translation tool, using open-source technologies that respect your privacy.

---

## About the Project
This add-on allows the user to translate paragraphs anywhere on the screen simply by staring at them for a moment. The text is extracted from the screen and translated in real-time, with the result displayed in the terminal.

### A Conscious Choice: Open Source vs. Commercial APIs
A key decision in this project was the use of a **100% free and open-source technology stack**.  
For text recognition and translation, we chose tools like **Tesseract** and **LibreTranslate**.

This choice was made to avoid dependency on commercial services (such as Google Cloud, which require a billing account).  
Our goal: to create a **fully accessible** tool, with **no costs** for the end user and enhanced **privacy**.  
The consequence is that translation relies on community-maintained public instances, which may occasionally be unstable.

---

## Features
- **Gaze Translation:** Simply fix your eyes on a text to trigger translation.  
- **Privacy First:** OCR runs 100% offline on the user’s machine.  
- **Hands-Free Control:** No need for keyboard or mouse interaction.  
- **Open-Source Stack:** Uses Tesseract + LibreTranslate (no costs or paid API keys).  
- **Customizable:** Fixation time and gaze sensitivity can be easily adjusted in the code.  

---

## Technologies Used
- **Language:** Python 3.12  
- **Eye Tracking:** Beam Eye Tracker SDK  
- **OCR:** Tesseract OCR  
- **Translation:** LibreTranslate Public API  
- **Libraries:** Pillow, Pytesseract, Requests  

---

## Environment Setup

### 1. Install Beam Eye Tracker
Download and install the software from Eyeware’s official website.

### 2. Install Tesseract OCR
- Download the installer for Windows: https://github.com/UB-Mannheim/tesseract/wiki

  Search for ´tesseract-ocr-w64-setup-5.5.0.20241111.exe (64 bit)
  
- During installation:  
  - Add language packages (e.g., English and Portuguese).  
  - Make sure to select the option to add Tesseract to the system **PATH**.  

### 3. Install Python Dependencies
With Python 3.12 installed, open the terminal in the project’s root folder and run:

```bash
pip install -r requirements.txt
```
## How to Run

### 1. Start the Eye Tracker
First, ensure the **Beam Eye Tracker** software is open and actively tracking your face.

### 2. Run the Program
Double-click the **run.bat** file to start the project.  
A terminal window will appear automatically.

### 3. Use the Application
- Look at any text on your screen.  
- Fix your gaze for **1.5 seconds**.  
- The translation will appear in the terminal window that opened.  

## Important Note on Translation
This project uses **public and free instances** of the **LibreTranslate API**.  
Since they are community-maintained services, they may become overloaded or temporarily offline.  

- If translation fails, it usually means the servers are unstable.  
- The code will automatically try other instances from the list.  
- If all fail, please wait a while and try again.  

---

## Authors
- Giulia Meninel Mattedi  
- Lucas Ferri dos Santos  
- Pedro Huck Henrique  
- Sthefany Viveiros Cordeiro  
- Túlio Gonçalves Vieira
