# Ponderada Reconhecimento de Dígitos Manuscritos com CNN e Flask

Este repositório contém o código e os recursos necessários para treinar e implementar uma rede neural convolucional (CNN) capaz de reconhecer dígitos manuscritos usando o conjunto de dados MNIST.

## Descrição do Projeto

1. **Treinamento do Modelo**:
    - Utilizando a base de dados MNIST, o modelo convolucional é treinado para reconhecer dígitos manuscritos.
    - O script de treinamento gera o arquivo `pesos.h5`, que contém os pesos treinados do modelo.

2. **Aplicação Flask**:
    - Uma aplicação web construída com Flask permite a interação com o modelo treinado.
    - A interface web fornece um formulário para upload de imagens contendo dígitos manuscritos.
    - Após o upload, a aplicação retorna o dígito predito pelo modelo.

## Estrutura do Repositório

```
project/
│
├── templates/
│   └── index.html        # Página HTML para upload de imagens
├── pesos.h5              # Pesos do modelo treinado
├── app.py                # Código da aplicação Flask
└── train_model.py        # Script de treinamento do modelo
```
## Requisitos de instalação

Certifique-se de ter flask tensorflow pillow instalado. Caso não tenha, é recomendado criar um amabiente virtual executando os seguintes comandos na raíz do projeto:
```
python3 -m venv venv
```
```
venv\Scripts\activate
```
E instalar a biblioteca necessária:

```
pip install flask tensorflow pillow
```

## Instruções de Uso

1. **Treinamento do Modelo**:
    - Execute o script `train_model.py` para treinar o modelo e gerar o arquivo `pesos.h5`.

    ```
    python train_model.py
    ```

2. **Iniciar a Aplicação Flask**:
    - Execute o script `app.py`na raíz do projeto para iniciar o servidor Flask.

    ```
    python app.py
    ```

    - Acesse `http://localhost:5000` no seu navegador para utilizar a interface web.

3. **Uso da Interface Web**:
    - Faça o upload de uma imagem contendo um dígito manuscrito.
    - O resultado da predição será exibido na tela.

## Rotas do Backend

O backend feito utilizando flask e definido no arquivo app.py, consiste em duas rotas:

**Rota "/":** essa é uma rota do tipo GET	que tem como objetivo retornar apágina HTML, definida no código pelo arquivo "index.html". Essa rota é responsável por exibir a página inicial com o formulário de upload de imagem.

**Rota "/predict":** essa é uma rota do tipo POST responsável por receber um Arquivo de imagem e retornar um JSON com o dígito reconhecido na predição.
