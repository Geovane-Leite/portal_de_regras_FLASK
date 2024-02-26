from flask import Flask, render_template, request
import fitz  # PyMuPDF
import os
import re

app = Flask(__name__)

def ler_pdf(nome_arquivo):
    texto = ""
    documento = fitz.open(nome_arquivo)
    for numero_pagina in range(documento.page_count):
        pagina = documento.load_page(numero_pagina)
        texto_pagina = pagina.get_text()
        padrao = r'\.\s*\n'
        texto_pagina = re.sub(padrao, lambda m: f". (Pag. {numero_pagina+1}).\n", texto_pagina)
        texto += texto_pagina
    return texto

def encontrar_paragrafos(texto, consulta):
    texto = texto.replace('- \n','').replace('-\n','')
    paragrafos = texto.split('.\n')
    consulta_palavras = consulta.lower().split()
    
    if len(consulta_palavras) == 1:
        min_palavras = 1
    elif len(consulta_palavras) == 2 or len(consulta_palavras) == 3:
        min_palavras = 2
    else:
        min_palavras = 0.5 * len(consulta_palavras)  # 50% das palavras da consulta

    resultados = []
    
    for paragrafo in paragrafos:
        palavras_encontradas = [palavra for palavra in consulta_palavras if re.search(r'\b{}\b'.format(re.escape(palavra)), paragrafo.lower())]
        cont_palavras_encontradas = len(palavras_encontradas)
        
        if cont_palavras_encontradas >= min_palavras:
            resultados.append((paragrafo, cont_palavras_encontradas, palavras_encontradas))

    return resultados if resultados else ["Nenhum parágrafo encontrado."]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        consulta = request.form['consulta']
        resultado_text = pesquisar(consulta)
        return render_template('index.html', resultado_text=resultado_text)
    return render_template('index.html', resultado_text="")

def pesquisar(consulta):
    cont = None
    diretorio = r'\\10.8.0.12\contas medicas\Ferramentas Python\manuais'
    resultado_text = ""
    consulta = consulta.replace(',', ' ')
    for arquivo in os.listdir(diretorio):
        nome_arquivo = os.path.join(diretorio, arquivo)
        nome_arquivo_txt = os.path.join(diretorio, arquivo).replace('manuais', 'temp_manuais').replace('.pdf', '.txt')
        if not os.path.isfile(nome_arquivo_txt):
            texto_pdf = ler_pdf(nome_arquivo)
            with open(nome_arquivo_txt, 'w', encoding='utf-8') as txt_file:
                txt_file.write(texto_pdf)
            resultados = encontrar_paragrafos(texto_pdf, consulta)
        else:
            with open(nome_arquivo_txt, 'r', encoding='utf-8') as txt_file:
                texto_txt = txt_file.read()
            resultados = encontrar_paragrafos(texto_txt, consulta)

        # Verifica se há resultados
        if resultados and resultados != ["Nenhum parágrafo encontrado."]:
            cont = 'encontrou'
            resultado_text += f'<h3 style="background-color: #00995e; color: white; font-family: Arial, sans-serif;">{arquivo}</h3>'
            resultados_ordenados = sorted(resultados, key=lambda x: x[1], reverse=True)
            cont_2 = 0
            for resultado in resultados_ordenados:
                cont_2 +=1
                try:
                    paragrafo, cont_palavras_encontradas, palavras_encontradas = resultado

                    if cont_palavras_encontradas >= 1 and cont_2==1:
                        resultado_text += f"<h4 style='font-family: Arial, sans-serif;'><span style='background-color: rgba(144, 238, 144, 0.5); color: #00995e;'>{'Parágrafo encontrado' if len(resultados) == 1 else 'Parágrafos encontrados'}: {len(resultados)}</span></h4>"
                    resultado_text += '<div style="background-color: lightgray; box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.1); padding: 10px;">'
                    resultado_text += f"<p style='font-family: Arial, sans-serif;'>{paragrafo}</p><p style='font-family: Arial, sans-serif;'>Total Palavras Encontradas: {cont_palavras_encontradas} : {' ; '.join(palavras_encontradas)}</p>"
                    resultado_text += '</div>'
                    resultado_text += '<hr style="border: 0.5mm gray; width: 100%; height: 100%;">'

                    
                except:
                    #resultado_text += f"Pesquisa {consulta} não encontrada.\n"
                    continue
    else:
        if not cont:
            resultado_text += f'<h3 style="background-color: red; color: #00995e; font-family: Arial, sans-serif;">Pesquisa {consulta} não encontrada!</h3>'
    return resultado_text


if __name__ == '__main__':
    app.run(debug=True)
