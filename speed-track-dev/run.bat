@echo off
TITLE SpeedTracker Dev Launcher

REM Define o caminho para o ambiente virtual e para o script principal
SET VENV_PATH=.\venv
SET SCRIPT_NAME=speed_tracker_app.py

REM Verifica se o executavel do Python dentro do venv existe
IF EXIST "%VENV_PATH%\Scripts\python.exe" (
    ECHO Iniciando o SpeedTracker Dev usando o ambiente virtual...
    ECHO.
    "%VENV_PATH%\Scripts\python.exe" "%SCRIPT_NAME%"
) ELSE (
    ECHO =================================================================
    ECHO  ERRO: Ambiente virtual 'venv' nao encontrado!
    ECHO =================================================================
    ECHO.
    ECHO Para corrigir, siga os passos de instalacao no README.md:
    ECHO 1. Crie o ambiente: python -m venv venv
    ECHO 2. Instale as dependencias: pip install -r requirements.txt
    ECHO.
)

ECHO.
ECHO Pressione qualquer tecla para sair...
PAUSE > NUL