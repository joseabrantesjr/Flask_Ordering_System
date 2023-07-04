# Sistema de Lanchonete

Um sistema web desenvolvido com Flask em Python que permite aos usuários visualizar o cardápio da lanchonete, selecionar produtos pelo código e adicionar ao pedido.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- Python 3.x
- Flask (instalável via `pip install flask`)

## Instalação

1. Clone o repositório para o seu ambiente local:

   git clone https://github.com/joseabrantesjr/PedidosLanchonete.git

2. Acesse o diretório do projeto:

   cd nome-do-repositorio

3. Crie um ambiente virtual (opcional, mas recomendado) e ative-o:

   python3 -m venv venv
   source venv/bin/activate

4. Instale as dependências do projeto:

   pip install -r requirements.txt

5. Configure as variáveis de ambiente:
Crie um arquivo .env no diretório raiz do projeto
Defina as seguintes variáveis no arquivo .env:

FLASK_APP=app.py
FLASK_ENV=development

6. Execute a aplicação:

   flask run

7. Acesse a aplicação em seu navegador web no seguinte endereço:
   http://localhost:5000

Uso

Ao acessar a aplicação, você verá o cardápio da lanchonete com os produtos disponíveis e seus respectivos códigos.
Digite o código do produto desejado na caixa de seleção e clique em "Adicionar ao Pedido" para adicionar o produto ao pedido atual.
O pedido será exibido abaixo do cardápio, mostrando os produtos selecionados e o total a pagar.
Contribuição

Contribuições são bem-vindas! Se você quiser contribuir para este projeto, siga as diretrizes de contribuição e envie uma solicitação de pull. Para relatar problemas ou fazer sugestões, abra uma issue.


Contato

Se você tiver alguma dúvida ou precisar de suporte, entre em contato com [seu nome] por e-mail em [seu-email@example.com].
