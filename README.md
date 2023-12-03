# README

This README documents the steps required to get your app up and running.

### What is this repository for?

* Quick summary...
* Version...
* [Basic writing and formatting syntax on GitHub](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

### How do I configure?

* Configuration summary...
* Settings...
* Dependencies

    To create a virtual environment

    ```
    $ python -m venv .venv
	```
	
	Then, you need to activate the virtual environment
	
	```
    $ .venv\Scripts\activate
    ```

    and then install the necessary bookstores

    ```
    $ pip install -r requirements.txt
    ```

* Database configuration...
* How to do tests...
* Deployment instructions...

#### Documentation

To generate the configuration for sphinx, create a folder with the name `doc`, and change to that folder

```
$ mkdir doc
$ cd doc
```

and then write the command below, changing the name of the author(s) and the name of the application:

```
$ sphinx-apidoc -F -f -A "nome do autor" -V 0 -R 0.1 -H "nome da aplicação" -e -P -a --ext-autodoc --ext-viewcode --ext-todo -o . ./../src/
```

Afterwards, you must configure the `doc\config.py` file with the changes you deem necessary

### Contribution Guidelines

* Writing tests...
* Code review...
* Other guidelines...

### Who should I talk to?

* Repository owner or administrator...
* Another community contact or team...
