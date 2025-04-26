# FURIA Chatbot

Este projeto é um chatbot interativo desenvolvido para fornecer informações sobre a equipe de CS2 da FURIA, incluindo elenco, próximas partidas e últimas partidas. Utiliza tecnologias como Angular no front-end e Python no back-end para comunicação com a API.

## Tecnologias Utilizadas

- **Front-end:** Angular
- **Back-end:** Python (Flask)
- **Banco de Dados:** MongoDB
- **API de IA:** Cohere
- **Outras:** HttpClient, API REST

## Funcionalidades

O chatbot responde a perguntas sobre:

- Elenco atual da FURIA
- Próximas partidas e eventos
- Últimas partidas e resultados

## Como Rodar

### Requisitos

- Angular CLI
- Python 3.x
- MongoDB
- API Cohere (chave de acesso necessária)

### Instruções

1. Clone este repositório:

   ```bash
   git clone https://github.com/Aegdae/chatbotFuria.git
   ```

2. Acesse a pasta do frond-end:

    ```bash
   cd frontend
   ```

3. Instale as dependências do front-end:

    ```bash
   npm install
   ```
4. Acesse a pasta do back-end:

    ```bash
   cd ../backend
   ```

5. Instale as dependências do back-end:

    ```bash
   pip install -r requirements.txt
   ```

6. Inicie o back-end (Python Flask):
    ```bash
   python app.py
   ```

7. Inicie o front-end (Angular):
    ```bash
   ng serve
   ```
8. Acesse o chatbot em http://localhost:4200 no seu navegador.

## Como Funciona

- O front-end (Angular) se comunica com o back-end (Python) por meio de uma API REST.

- O back-end faz requisições à API Cohere para gerar respostas automáticas baseadas nas perguntas dos usuários.

- O MongoDB armazena informações sobre partidas e jogadores.

## Contribuições

Sinta-se à vontade para abrir issues ou pull requests para melhorias. 
Caso queira contribuir, faça um fork deste repositório, faça suas alterações 
e envie um pull request com uma descrição clara do que foi alterado.

MIT License

Copyright (c) 2025 Aegdae

Permitted use, modification, distribution, and sublicensing are subject to the terms of this license. For the full license, please refer to: https://opensource.org/licenses/MIT