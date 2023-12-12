# Cadastro com Flet & CRUD
&nbsp;
Sistema de Cadastro de pessoas desenvolvido em Python 

utilizando para a interface gráfica o framework Flet.
---
### Versão 1.0

&nbsp;

> Pré-requisitos

Python 3.9+
 
&nbsp;
  
> Bibliotecas
 
[Flet](https://flet.dev/docs/guides/python/getting-started/)
  
[SQLite3](https://www.sqlite.org/docs.html)

&nbsp;
&nbsp;

> Pré-code
> > virtual environment
### Feito via terminal, instalação de um ambiente virtual
    python -m venv env
    .\env\Scripts\activate

&nbsp;
&nbsp;
    
> Pré-code
> > Instalando as bibliotécas

    pip install flet db-sqlite3     


&nbsp;
&nbsp;


> Funcionalidades:

* Cadastrar novos usuários com nome, idade, contato, sexo, email e endereço
* Listar todos os usuários cadastrados em uma tabela
* Editar dados de um usuario
* Excluir um usuario
* Salvar os dados em um banco SQLite

&nbsp;
&nbsp;

> Uso

Execute python `app.py` e acesse http://localhost:80 para utilizar a interface web.

As funções estão disponíveis através de botões e menus.

&nbsp;
&nbsp;

### Implementação

A interface é construída com [Flet](https://flet.dev/docs/guides/python/getting-started/) utilizando componentes como `TextField`, `Table` e `SnackBar`.

Os dados são salvos em um banco [SQLite3](https://www.sqlite.org/docs.html), com uma tabela `users` para armazenar os cadastros.

&nbsp;
&nbsp;

> Créditos


Código inicial baseado no canal [Cursos de Programação](https://www.youtube.com/watch?v=cOzpRMBfvcY&list=WL&index=24).


Documentação e melhorias adicionadas por [Wesley Pereira](https://github.com/wesleyp846)



&nbsp;
> Licença
MIT


Espero que a documentação ajude a entender a aplicação! Por favor sinta-se a vontade para melhorá-la.


# Algumas telas gráficas


![Captura de tela 2023-12-11 214420](https://github.com/wesleyp846/Cadastro_com_flet/assets/101286798/2827c07f-eeff-45d2-adb7-0036138e0502)
![Captura de tela 2023-12-11 214507](https://github.com/wesleyp846/Cadastro_com_flet/assets/101286798/23f8d694-cb54-4c78-bd26-732e24d52356)

