# ToDo API

Esta é uma API de lista de tarefas (ToDo) construída com Django e Django REST Framework.


## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/LeoMBasilio/ToDo_api.git
   cd ToDo_api
   ```
2. Crie um ambiente virtual e ative-o:

   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
3. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```
4. Execute as migrações do banco de dados:

   ```sh
   python manage.py migrate
   ```
5. Inicie o servidor de desenvolvimento:

   ```sh
   python manage.py runserver
   ```

## Endpoints

A API possui os seguintes endpoints:

- `GET /v1/task/` - Lista todas as tarefas
- `POST /v1/task/` - Cria uma nova tarefa
- `GET /v1/task/{id}/` - Detalha uma tarefa específica
- `PUT /v1/task/{id}/` - Atualiza uma tarefa específica
- `DELETE /v1/task/{id}/` - Deleta uma tarefa específica

## Modelos

### Task

- [title](http://_vscodecontentref_/18) (CharField): Título da tarefa
- [description](http://_vscodecontentref_/19) (TextField): Descrição da tarefa
- [completed](http://_vscodecontentref_/20) (BooleanField): Status de conclusão da tarefa
- [created_at](http://_vscodecontentref_/21) (DateTimeField): Data de criação da tarefa

## Serializers

### TaskSerializer

Serializa o modelo [Task](http://_vscodecontentref_/22) para JSON.

## Views

### Task_View_Set

Um viewset que fornece as operações CRUD para o modelo [Task](http://_vscodecontentref_/23).

## Admin

A interface de administração do Django foi configurada para gerenciar as tarefas.

## Configurações

As configurações do Django estão no arquivo [settings.py](http://_vscodecontentref_/24).

## URLs

As URLs da API estão configuradas no arquivo [urls.py](http://_vscodecontentref_/25).

## Testes

Os testes estão localizados no arquivo [tests.py](http://_vscodecontentref_/26).

## Licença

Este projeto está licenciado sob os termos da licença MIT.
