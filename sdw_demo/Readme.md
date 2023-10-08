# Complementação do desfio - Pipeline ETL

Atravez da API da Santander Dev Week 2023 construída em Java 17 com Spring Boot 3. 
Desenvolvi uma interface simples que representasse o consumo desses dados.

## Tecnologias
  - **Phyton**: Utilizando a versão 3.11.5.
  - **Flask**: um microframework web em Python usado para criar aplicativos web de forma rápida e simples. [link](https://flask.palletsprojects.com/en/3.0.x/)
  - **Colab**: Notebook virtual para execução do modelo Pipeline ETL utilizando as tecnoligias citadas abaixo.

## Executando o projeto DEMO

Utilize o Python 3.x
 
 - Neste repositório abra o diretório swd_demo/ em um terminal e execute o comando:
>  python -m venv myenv

instale o Flask

 > pip install Flask

Caso seja necessário instalar a biblioteca [requests](https://pypi.org/project/requests/)
> pip install requests

OBS.: Estes passos funcionam bem para Windows, procure na [Documentação](https://flask.palletsprojects.com/en/3.0.x/) formas de instalação para Linux e MacOs. 

Se tudo ocorrer bem, basta executar o comando: 
>flask run

dentro da pasta sdw_demo, no ambiente python. 
Agora acesse o pelo navegador https://localhost:5000

## Testes com Pipeline ETL
 
Ao acessar nosso ambiente demo, passando um *id* como cainho de referência a um cadastro no nosso *banco de dados*, nossa página é carregada com as informação dispostas: 
> https://localhost:5000/1


## Considerações

Este projeto tem finalidade de aprendizagem, construindo um pequeno servidor local para desenvolver um sistema utilizando a linguagem Python. 
