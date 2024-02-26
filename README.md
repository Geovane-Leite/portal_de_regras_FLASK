# Flask Auditoria de Documentos

Este é um projeto Flask para realizar auditoria em documentos PDF em busca de determinadas palavras-chave ou frases.
Ele permite que os usuários enviem consultas de pesquisa e retorna os parágrafos nos quais as palavras-chave foram encontradas,
juntamente com informações adicionais.

## Funcionalidades

- **Pesquisa de palavras-chave:** Os usuários podem inserir palavras-chave ou frases para pesquisar nos documentos PDF.
- **Visualização de resultados:** Os resultados da pesquisa são exibidos, incluindo o nome do arquivo, os parágrafos encontrados e as palavras-chave associadas.

## Principais Tecnologias Utilizadas

- **Flask:** Um framework de aplicativo da web em Python.
- **PyMuPDF (fitz):** Uma biblioteca Python para trabalhar com documentos PDF.

## Instruções de Uso

1. **Instalação de Dependências:**
   Certifique-se de ter o Python instalado em seu ambiente. Você pode instalar as dependências necessárias executando o seguinte comando:

2. **Execução do Aplicativo:**
Execute o arquivo `auditoria_flask.py` para iniciar o servidor Flask. Por padrão, o aplicativo será executado em `http://localhost:5000`.

3. **Acesso ao Aplicativo:**
Abra um navegador da web e navegue até `http://localhost:5000` para acessar o aplicativo.

4. **Pesquisa de Documentos:**
Na página inicial, insira as palavras-chave ou frases que deseja pesquisar nos documentos PDF e clique no botão "Pesquisar".

5. **Visualização de Resultados:**
Os resultados da pesquisa serão exibidos na página, mostrando os parágrafos encontrados em cada documento PDF, juntamente com as palavras-chave associadas.

## Observações

Certifique-se de que os documentos PDF estejam presentes no diretório especificado no código (diretorio).
O diretório temp_manuais foi criado para otimizar a busca, funcionando como uma espécie de cache.
Isso significa que não é necessário ler todo o PDF novamente a cada pesquisa.
Esse cache é usado para armazenar os textos extraídos dos PDFs, o que ajuda a otimizar a velocidade da busca.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork deste repositório, implementar melhorias e enviar um pull request.

## Licença

Este projeto é licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
