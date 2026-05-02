🚀 7 Boas Práticas Para APIs RESTful Profissionais!
#API Rest
Fala Comunidade tudo certo ? Hoje vou deixar listado aqui abaixo 7 padrões de rotas RESTful que são fundamentais para garantir uma API bem estruturada, consistente e de fácil leitura.



Independente da sua linguagem de programação, essas regrinhas vão te dar uns pontos extras garantidos com entrevistadores técnicos.



1. Utilização de Substantivos em Rotas: Utilize substantivos plurais para representar recursos na API. Por exemplo



 ❌ Incorreto: `/getUsers`, `/retrieveAllProducts`

 ✅ Correto: `/users`, `/products`, `/orders`



2. Utilização de Métodos HTTP: Use os métodos HTTP de forma adequada para cada operação rest;



 🔸 `GET` para recuperar recursos.

 🔸 `POST` para criar novos recursos.

 🔸 `PUT` ou `PATCH` para atualizar recursos existentes.

 🔸`DELETE` para excluir recursos.



3. Hierarquia e Aninhamento Em Rotas: Para recursos aninhados, utilize hierarquias de URLs consistentes. Por exemplo, para obter os pedidos de um usuário específico:



 ✅ `/users/{userId}/orders`



4. Nomes de Ações: Evite verbos e ações nos URLs. Em vez disso, utilize o método HTTP apropriado. Por exemplo, ao invés de `/createUser`, use:



✅ `POST /users` para criar um usuário.



5. Versionamento De Rotas: Considere versionar sua API para permitir mudanças sem quebrar clientes existentes. Por exemplo:



 🔸 `/v1/users`

 🔸 `/v2/users`



6. Parâmetros de Consulta: Use parâmetros de consulta para filtros, paginação e ordenação. Por exemplo:



 ✅ `/products?category=electronics&limit=10&page=1&sort=price`



7. Tratamento de Erros: Utilize códigos de status HTTP apropriados para indicar o sucesso ou falha de uma requisição. Por exemplo:



 🔸 `200 OK` para sucesso.

 🔸 `400 Bad Request` para requisição inválida.

 🔸 `404 Not Found` para recurso não encontrado.



Exemplo de uma estrutura de rotas RESTful para uma API de usuários:



 Recursos de Usuários:

 🔸`GET /users`: Lista todos os usuários.

 🔸`POST /users`: Cria um novo usuário.

 🔸`GET /users/{userId}`: Obtém detalhes de um usuário específico.

 🔸`PUT /users/{userId}`: Atualiza um usuário existente.

 🔸`DELETE /users/{userId}`: Exclui um usuário.



- Recursos de Pedidos (aninhado com Usuários):



 🔸 `GET /users/{userId}/orders`: Lista os pedidos de um usuário específico.

 🔸 `POST /users/{userId}/orders`: Cria um novo pedido para um usuário.



Essas práticas ajudam a criar uma API coesa, fácil de entender e que segue os padrões de design RESTful.