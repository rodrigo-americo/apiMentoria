
# API de Gestão de Estoque de PCs

## Descrição

Esta API foi desenvolvida para gerenciar o estoque de computadores em um ambiente educacional. A API permite realizar operações CRUD em registros de PCs, bem como obter uma contagem de quantos PCs possuem SSD.

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/rodrigo-americo/apiMentoria.git
   cd nome-do-repositorio
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrações:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```

## Endpoints

### 1. `GET /pc/`
Lista todos os PCs.

- **Exemplo de Resposta com Paginação**:
  ```json
  {
      "count": 50,
      "next": "http://127.0.0.1:8000/pc/?page=2",
      "previous": null,
      "results": [
          {
              "id": "PC101",
              "brand": "Dell",
              "model": "XPS",
              "classroom": 101,
              "ssd": true,
              "createdAt": "2024-08-14T17:00:00Z",
              "updatedAt": "2024-08-14T17:30:00Z"
          },
          {
              "id": "PC102",
              "brand": "HP",
              "model": "EliteBook",
              "classroom": 102,
              "ssd": false,
              "createdAt": "2024-08-14T17:35:00Z",
              "updatedAt": "2024-08-14T17:35:00Z"
          }
      ]
  }
  ```

### 2. `POST /pc/`
Cria um novo PC.

### 3. `GET /pc/<str:pk>/`
Recupera os detalhes de um PC específico.

### 4. `PUT /pc/<str:pk>/`
Atualiza os detalhes de um PC específico.

### 5. `DELETE /pc/<str:pk>/`
Exclui um PC específico.

### 6. `GET /pcs/ssd_count/`
Retorna a contagem de PCs com e sem SSD.

## Modelo `Pc`

O modelo `Pc` representa um computador no estoque e possui os seguintes campos:

- **id**: Identificador único (e.g., `PC102`).
- **brand**: Marca do computador.
- **model**: Modelo do computador.
- **classroom**: Sala de aula onde o computador está localizado.
- **ssd**: Booleano indicando se o computador possui SSD.
- **createdAt**: Data e hora de criação do registro.
- **updatedAt**: Data e hora da última atualização do registro.

## Contribuição

Contribuições são bem-vindas! Por favor, faça um fork do repositório e envie um pull request com suas mudanças.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
