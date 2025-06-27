# Easy Collection

Um gerenciador de coleções intuitivo e visual para colecionadores e entusiastas.

---

## 📄 Sobre o Projeto

O **Easy Collection** é uma plataforma desenvolvida para simplificar a gestão de coleções pessoais de forma fácil, intuitiva e visual. Ele permite aos usuários organizar seus filmes, jogos, livros, histórias em quadrinhos e outros itens, integrando-se com diversas APIs externas para enriquecer as informações das coleções.

---

## ✨ Funcionalidades Principais

- **Cadastro e Login de Usuários:** Sistema de autenticação robusto.
- **Criação de Coleções Personalizadas:** Flexibilidade para o usuário definir suas próprias coleções.
- **Utilização de Coleções Pré-criadas:** Opções de coleções prontas para uso, com dados preenchidos automaticamente.
- **Gerenciamento Completo de Dados:** Controle total sobre itens e coleções.
- **Integração com APIs Externas:** Busca automática de dados detalhados para itens (filmes, jogos, livros, etc.).

---

## 🛠️ Tecnologias Utilizadas

Este projeto utiliza uma arquitetura moderna e escalável, com as seguintes tecnologias principais:

- **Front-End:** React
- **Back-End:** Node.js com Express
- **API Gateway:** AWS API Gateway
- **Cache:** Redis
- **Fila de Mensagens:** Apache Kafka
- **Workers Assíncronos:** Node.js Workers
- **ORM/ODM:** Mongoose
- **Banco de Dados:** MongoDB
- **CDN:** AWS CloudFront
- **APIs Externas:** The Movie Database (TMDb), RAWG, Open Library, Marvel API

---

## 🚀 Como Executar o Projeto

Para executar o Easy Collection localmente, siga os passos abaixo. Certifique-se de ter **Node.js**, **npm** (ou **yarn**), **Docker** e **Docker Compose** instalados em seu sistema (compatível com CachyOS Linux).

### Pré-requisitos

- Node.js (LTS recomendado)
- npm ou Yarn
- Docker e Docker Compose
- Acesso a chaves de API para serviços externos (TMDb, RAWG, Open Library, Marvel API)

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/easy-collection.git
cd easy-collection
```

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto (e/ou nos diretórios backend e frontend, conforme a estrutura do seu monorepo, se houver) com base no `.env.example`.

**Exemplo de .env (Back-End):**

```env
# Configurações do Servidor
PORT=3000
NODE_ENV=development

# Configurações do MongoDB
MONGO_URI=mongodb://localhost:27017/easycollection_db

# Configurações do Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# Configurações do Kafka (se usar Kafka localmente via Docker Compose)
KAFKA_BROKERS=localhost:9092

# Chaves de API Externas (substitua pelas suas chaves reais)
TMDB_API_KEY=sua_chave_tmdb
RAWG_API_KEY=sua_chave_rawg
OPENLIBRARY_API_KEY=sua_chave_openlibrary
MARVEL_API_KEY_PUBLIC=sua_chave_publica_marvel
MARVEL_API_KEY_PRIVATE=sua_chave_privada_marvel

# Segredos de Autenticação (JWT, etc.)
JWT_SECRET=seu_segredo_jwt_muito_seguro
```

**Exemplo de .env (Front-End):**

```env
# URL da API do Back-End
REACT_APP_API_BASE_URL=http://localhost:3000
```

### 3. Subir Serviços com Docker Compose (MongoDB, Redis, Kafka)

No diretório raiz do projeto, execute:

```bash
docker-compose up -d
```

Isso iniciará o MongoDB, Redis e Kafka em contêineres Docker.

### 4. Instalar Dependências e Iniciar o Back-End

A partir do diretório raiz:

```bash
cd backend # Ou o diretório do seu Back-End
npm install # ou yarn install
npm start   # ou yarn start
```

O servidor Back-End estará rodando em http://localhost:3000 (ou na porta configurada).

### 5. Instalar Dependências e Iniciar o Front-End

A partir do diretório raiz:

```bash
cd frontend # Ou o diretório do seu Front-End
npm install # ou yarn install
npm start   # ou yarn start
```

A aplicação Front-End será iniciada e geralmente abrirá automaticamente no seu navegador em http://localhost:3001 (ou outra porta disponível).

### 6. Executar os Workers Assíncronos

Os workers são processos separados que consomem mensagens da fila.

```bash
cd workers # Ou o diretório dos seus workers
npm install # ou yarn install
npm start   # ou yarn start
```

Os workers começarão a processar as tarefas assíncronas da fila.

---

## 🗺️ Endpoints da API (Principais)

Aqui estão alguns dos principais endpoints que o Back-End expõe (assumindo prefixo `/api`):

### Autenticação

- `POST /api/auth/register`: Registrar um novo usuário.
- `POST /api/auth/login`: Autenticar e obter um token JWT.

### Usuários

- `GET /api/users/me`: Obter informações do usuário logado (requer token).

### Coleções

- `GET /api/collections`: Listar todas as coleções do usuário.
- `POST /api/collections`: Criar uma nova coleção personalizada.
- `GET /api/collections/pre-created`: Listar coleções pré-criadas disponíveis.
- `POST /api/collections/pre-created`: Criar uma coleção a partir de um template pré-criado (isso enfileirará uma tarefa assíncrona para buscar dados de APIs externas).
- `GET /api/collections/:id`: Obter detalhes de uma coleção específica.
- `PUT /api/collections/:id`: Atualizar uma coleção.
- `DELETE /api/collections/:id`: Excluir uma coleção.

### Itens

- `GET /api/collections/:collectionId/items`: Listar itens de uma coleção.
- `POST /api/collections/:collectionId/items`: Adicionar um novo item a uma coleção (manual ou via API externa).
- `GET /api/collections/:collectionId/items/:itemId`: Obter detalhes de um item específico.
- `PUT /api/collections/:collectionId/items/:itemId`: Atualizar um item.
- `DELETE /api/collections/:collectionId/items/:itemId`: Excluir um item.

### APIs Externas (proxy/busca)

- `GET /api/external/tmdb/search?query=...`: Buscar filmes/séries no TMDb (exemplo).
- (Outros endpoints de busca para RAWG, Open Library, Marvel API)

---

## 🔐 Segurança

Com a minha experiência em Segurança da Informação, o projeto incorpora diversas práticas de segurança:

- **API Gateway:** Para autenticação centralizada, rate limiting e proteção contra ataques comuns.
- **Validação de Dados:** Rigorosa validação de entrada no Back-End para prevenir injeção e outros vetores de ataque.
- **Autenticação JWT:** Uso de JSON Web Tokens para autenticação segura e stateless.
- **Variáveis de Ambiente:** Gerenciamento de segredos via variáveis de ambiente.
- **Backup Periódico:** Estratégia de backup para garantir a durabilidade dos dados.

---

## 📈 Monitoramento

O sistema é instrumentado para monitoramento abrangente, utilizando ferramentas como:

- **Métricas de Performance:** Latência, throughput, consumo de recursos (CPU, memória) em todas as camadas.
- **Logs de Segurança e Acesso:** Rastreamento de atividades e tentativas de acesso.
- **Rastreamento de Erros e Alertas:** Notificações proativas sobre falhas no sistema.
- **Estatísticas de Uso e Rate Limiting:** Visibilidade sobre o tráfego da API e proteção contra picos.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, leia o `CONTRIBUTING.md` (se disponível) para detalhes sobre nosso código de conduta e o processo para enviar pull requests.

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
