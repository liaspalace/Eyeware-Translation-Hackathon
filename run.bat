@echo off
ECHO Iniciando o Tradutor Ocular...
ECHO.
ECHO Certifique-se de que o aplicativo Beam Eye Tracker esta rodando.
ECHO Este terminal precisa continuar aberto para o programa funcionar.
ECHO.

REM Navega para a pasta correta do script
cd "%~dp0\python\samples\data_access_methods"

REM Executa o script Python
python bet_polling_data_access.py

ECHO.
ECHO O programa foi finalizado. Pressione qualquer tecla para fechar.
pause