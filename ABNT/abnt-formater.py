# -*- coding: utf-8 -*-

import docx
from docx.shared import Cm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
import sys
import os

# --- CONSTANTES DE FORMATAÇÃO ABNT ---
# Fonte e Tamanho
FONTE_PADRAO = 'Arial'
TAMANHO_FONTE_PADRAO = Pt(12)

# Margens (Superior/Esquerda: 3cm, Inferior/Direita: 2cm)
MARGEM_SUPERIOR = Cm(3)
MARGEM_INFERIOR = Cm(2)
MARGEM_ESQUERDA = Cm(3)
MARGEM_DIREITA = Cm(2)

# Espaçamento entre linhas (1.5)
ESPAÇAMENTO_LINHAS = 1.5

def formatar_documento_abnt(input_path, output_path):
    """
    Aplica formatação ABNT básica a um documento Word (.docx).
    - Define as margens da página.
    - Aplica fonte, tamanho e espaçamento a todos os parágrafos.
    """
    try:
        # Verifica se o arquivo de entrada existe
        if not os.path.exists(input_path):
            print(f"Erro: O arquivo de entrada '{input_path}' não foi encontrado.")
            return

        # Abre o documento de entrada
        document = docx.Document(input_path)
        print(f"Arquivo '{input_path}' aberto com sucesso.")

        # 1. CONFIGURAR MARGENS DA PÁGINA
        # A configuração de margens é feita por seção. Vamos aplicar a todas as seções.
        for section in document.sections:
            section.top_margin = MARGEM_SUPERIOR
            section.bottom_margin = MARGEM_INFERIOR
            section.left_margin = MARGEM_ESQUERDA
            section.right_margin = MARGEM_DIREITA
        
        print("Margens ABNT aplicadas.")

        # 2. CONFIGURAR ESTILO PADRÃO (Normal)
        # É uma boa prática modificar o estilo 'Normal' que a maioria dos outros herda.
        style = document.styles['Normal']
        font = style.font
        font.name = FONTE_PADRAO
        font.size = TAMANHO_FONTE_PADRAO
        
        paragraph_format = style.paragraph_format
        paragraph_format.line_spacing = ESPAÇAMENTO_LINHAS
        paragraph_format.space_before = Pt(0)
        paragraph_format.space_after = Pt(8) # Um pequeno espaço após cada parágrafo

        print(f"Estilo 'Normal' configurado para Fonte: {FONTE_PADRAO}, Tamanho: {TAMANHO_FONTE_PADRAO.pt}pt, Espaçamento: {ESPAÇAMENTO_LINHAS}.")

        # 3. PERCORRER E APLICAR ESTILO A CADA PARÁGRAFO
        # Esta é uma garantia extra, caso algum parágrafo tenha formatação direta.
        for paragraph in document.paragraphs:
            # Aplica o estilo 'Normal' para garantir a base
            paragraph.style = document.styles['Normal']
            
            # Exemplo de lógica customizada: Se quiser justificar o corpo do texto
            # (Aqui, vamos apenas justificar tudo como exemplo, exceto títulos talvez)
            # Para um formatador real, seria preciso identificar o que é título e o que é corpo.
            paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

        print("Formatação aplicada a todos os parágrafos.")

        # Salva o novo documento formatado
        document.save(output_path)
        print(f"Documento formatado salvo com sucesso em: '{output_path}'")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    # O script espera dois argumentos da linha de comando:
    # 1. O caminho para o arquivo de entrada (ex: "meu_trabalho.docx")
    # 2. O caminho para o arquivo de saída (ex: "meu_trabalho_formatado.docx")
    
    if len(sys.argv) != 3:
        print("Uso incorreto!")
        print("Exemplo: python formatador_abnt.py 'documento_original.docx' 'documento_formatado.docx'")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        formatar_documento_abnt(input_file, output_file)
