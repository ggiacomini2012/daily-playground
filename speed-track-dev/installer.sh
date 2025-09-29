#!/bin/bash

echo "🚀 Iniciando a compilação do SpeedTracker..."

# 1. Executa o PyInstaller
pyinstaller --name SpeedTracker --onefile --windowed --icon="icon.ico" speed_tracker_app.py

# Verifica se a compilação foi bem-sucedida
if [ -f "dist/SpeedTracker.exe" ]; then
    echo "✅ Compilação concluída com sucesso."

    # 2. Move o executável para a pasta principal
    echo "🚚 Movendo SpeedTracker.exe..."
    mv dist/SpeedTracker.exe .

    # 3. Limpa os arquivos e pastas temporárias
    echo "🧹 Limpando arquivos temporários (dist, build, spec)..."
    rm -rf dist/ build/ SpeedTracker.spec

    echo "🎉 Tudo pronto! Seu SpeedTracker.exe está na pasta principal."
else
    echo "❌ Erro na compilação. Verifique as mensagens acima."
fi