# Projeto To-Do List com Django

Este projeto é uma aplicação web para gerenciamento de tarefas (To-Do List), construída com Django.  
Possui autenticação de usuários (login, registro, logout) e funcionalidades para criar, listar, atualizar, deletar, completar e marcar tarefas como pendentes.

---

## Tecnologias utilizadas

- Python 3.x  
- Django 5.x  
- Banco de dados padrão SQLite (pode ser configurado para outro)  

---

## Estrutura do projeto

- **authentication**: app responsável pelo sistema de autenticação (login, registro, logout)  
- **platform_app**: app responsável pelo gerenciamento das tarefas (CRUD e status)  
- **urls.py principal**: direciona as rotas para os apps `authentication` e `platform_app`  

---

## Apps e funcionalidades

### Authentication

- **Rotas**:

  | URL                | View             | Descrição                  |
  |--------------------|------------------|----------------------------|
  | `/auth/logar/`      | Login            | Página de login            |
  | `/auth/cadastro/`   | Register         | Página de cadastro         |
  | `/auth/sair/`       | LogOut           | Logout do usuário          |

- **Views**: baseadas em `django.views.View`

  - `Login`: autentica usuário e senha, redireciona para `/tasks/listar-tarefas/` se sucesso  
  - `Register`: cria usuário novo se válido, evita duplicidade  
  - `LogOut`: realiza logout e redireciona para login

### Platform_app

- **Modelo Task**:

  | Campo       | Tipo                 | Descrição                            |
  |-------------|----------------------|------------------------------------|
  | `title`     | CharField (max 20)   | Título da tarefa                   |
  | `description` | CharField (max 100) | Descrição da tarefa                |
  | `status`    | CharField (1)        | Status da tarefa: P (pendente), C (concluída), D (deletada) |
  | `created_at`| DateTimeField        | Data e hora de criação (default: agora) |
  | `user`      | ForeignKey User      | Usuário dono da tarefa              |

- **Rotas**:

  | URL                            | View           | Descrição                         |
  |--------------------------------|----------------|---------------------------------|
  | `/tasks/listar-tarefas/`        | ListTasks      | Lista as tarefas do usuário      |
  | `/tasks/criar-tarefa/`           | TaskCreate     | Formulário para criar tarefa     |
  | `/tasks/atualizar-tarefa/<id>/` | TaskUpdate     | Atualiza tarefa existente        |
  | `/tasks/deletar-tarefa/<id>/`   | TaskDelete     | Deleta tarefa                    |
  | `/tasks/completar-tarefa/<id>/` | CompleteTask   | Marca tarefa como concluída      |
  | `/tasks/pendenciar-tarefa/<id>/`| PendingTask    | Marca tarefa como pendente       |

- **Views**: utilizam generic views do Django e mixins para proteção por login (`LoginRequiredMixin`)

- **Admin**: o model `Task` está registrado com customizações para facilitar administração (list_display, list_editable, filtros, busca)

---

## Como rodar o projeto localmente

1. Clone o repositório  
2. Crie e ative um ambiente virtual Python  
3. Instale as dependências usando o arquivo `requirements.txt`: pip install -r requirements.txt
5. Execute as migrações: python manage.py migrate
6. Crie um superusuário para acessar o admin: python manage.py createsuperuser
7. Rode o servidor de desenvolvimento: python manage.py runserver
