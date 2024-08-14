
### Documentação da API

#### Introdução

Esta API foi desenvolvida para gerenciar um estoque de computadores (PCs) em um ambiente educacional. A API permite a criação, listagem, atualização e exclusão de informações de PCs, bem como a contagem de PCs que possuem ou não SSD.

#### Modelo `Pc`

O modelo `Pc` representa um computador no estoque e possui os seguintes campos:

- **id**: Um identificador único do computador, começando com "PC", seguido por um número entre 1 e 5, e terminando com um número entre 01 e 10. Exemplo: `PC102`.
- **brand**: A marca do computador.
- **model**: O modelo do computador.
- **classroom**: O número da sala de aula onde o computador está localizado.
- **ssd**: Um campo booleano que indica se o computador possui SSD (`True`) ou não (`False`).
- **createdAt**: Data e hora em que o registro foi criado.
- **updatedAt**: Data e hora da última atualização do registro.

```python
class Pc(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    classroom = models.IntegerField()
    ssd = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pc"
        verbose_name_plural = 'Pcs'

    def __str__(self):
        return self.id
```

#### Endpoints

1. **`GET /pc/`**: Lista todos os PCs.
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

2. **`POST /pc/`**: Cria um novo PC.
   - **Corpo da Requisição**:
     ```json
     {
       "id": "PC105",
       "brand": "HP",
       "model": "EliteBook",
       "classroom": 102,
       "ssd": false
     }
     ```
   - **Resposta**:
     ```json
     {
       "id": "PC105",
       "brand": "HP",
       "model": "EliteBook",
       "classroom": 102,
       "ssd": false,
       "createdAt": "2024-08-14T17:35:00Z",
       "updatedAt": "2024-08-14T17:35:00Z"
     }
     ```

3. **`GET /pc/<str:pk>/`**: Recupera os detalhes de um PC específico.
   - **Exemplo de URL**: `/pc/PC105/`
   - **Resposta**:
     ```json
     {
       "id": "PC105",
       "brand": "HP",
       "model": "EliteBook",
       "classroom": 102,
       "ssd": false,
       "createdAt": "2024-08-14T17:35:00Z",
       "updatedAt": "2024-08-14T17:35:00Z"
     }
     ```

4. **`PUT /pc/<str:pk>/`**: Atualiza os detalhes de um PC específico.
   - **Exemplo de URL**: `/pc/PC105/`
   - **Corpo da Requisição**:
     ```json
     {
       "brand": "HP",
       "model": "EliteBook 840",
       "classroom": 103,
       "ssd": true
     }
     ```
   - **Resposta**:
     ```json
     {
       "id": "PC105",
       "brand": "HP",
       "model": "EliteBook 840",
       "classroom": 103,
       "ssd": true,
       "createdAt": "2024-08-14T17:35:00Z",
       "updatedAt": "2024-08-14T18:00:00Z"
     }
     ```

5. **`DELETE /pc/<str:pk>/`**: Exclui um PC específico.
   - **Exemplo de URL**: `/pc/PC105/`
   - **Resposta**: Status HTTP 204 No Content.

6. **`GET /pcs/ssd_count/`**: Retorna a contagem de PCs que possuem SSD e PCs que não possuem SSD.
   - **Resposta**:
     ```json
     {
       "pcs_with_ssd": 10,
       "pcs_without_ssd": 15
     }
     ```

