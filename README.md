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
- **Rastreamento Ocular:** BEam Eye Tracker SDK  
- **OCR:** Tesseract OCR  
- **Tradução:** API Pública do LibreTranslate  
- **Bibliotecas:** Pillow, Pytesseract, Requests  

---

## Configuração do Ambiente

### 1. Instale o Beam Eye Tracker
Baixe e instale o software no site oficial da Eyeware.

### 2. Instale o Tesseract OCR
- Baixe o instalador para Windows: https://github.com/UB-Mannheim/tesseract/wiki(#)  
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
Abra o aplicativo **Beam Eye Tracker** e certifique-se de que ele está rastreando seu rosto. Ative "Extensões de Jogo".

### 2. Execute o Script Principal
Abra um terminal, navegue até a pasta do script  
`(.../python/samples/data_access_methods/)` e execute:

```bash
python bet_polling_data_access.py 
```

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
