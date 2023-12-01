# README

Este README documenta as etapas necessárias para colocar seu aplicativo em funcionamento.

### Para que serve este repositório?

* Resumo rápido...
* Versão...
* [Sintaxe básica de gravação e formatação no GitHub](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

### Como faço para configurar?

* Resumo da configuração...
* Configuração...
* Dependências

    Para criar um ambiente virtual

    ```
    $ python -m venv .venv
	```
	
	Depois, é necessário ativar o ambiente virtual
	
	```
    $ .venv\Scripts\activate
    ```

    e depois instalar as livrarias necessárias

    ```
    $ pip install -r requirements.txt
    ```

* Configuração de banco de dados...
* Como fazer testes...
* Instruções de implantação...

#### Documentação

Para gerar a configuração para o sphinx, crie uma pasta com o nome `doc`, e mude para essa pasta

```
$ mkdir doc
$ cd doc
```

e depois escreva o comando abaixo, alterando o nome do(s) autor(es), e o nome da aplicação:

```
$ sphinx-apidoc -F -f -A "nome do autor" -V 0 -R 0.1 -H "nome da aplicação" -e -P -a --ext-autodoc --ext-viewcode --ext-todo -o . ./../src/
```

Posteriormente deve configurar o ficheiro `doc\config.py` com as alterações que entenda necessárias

### Diretrizes de contribuição

* Testes de escrita...
* Revisão de código...
* Outras diretrizes...

### Com quem devo falar?

* Proprietário ou administrador do repo...
* Outro contato da comunidade ou equipe...
