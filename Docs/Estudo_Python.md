https://youtube.com/playlist?list=PLRc6ZYt68prXeud4anb1DYM_k7Zl2ng0K&si=hwM3FQZaovueaXsL

Realizando o curso Python Essentials 1 pela Cisco

# Python

## Visão geral

Python é uma linguagem de programação de alto nível, de propósito geral e com sintaxe relativamente simples. É utilizada em diferentes áreas do desenvolvimento de software, incluindo automação, desenvolvimento web, análise de dados, inteligência artificial e IoT.

## Características

* Sintaxe simples e legível
* Tipagem dinâmica
* Suporte à programação orientada a objetos
* Grande quantidade de bibliotecas e frameworks
* Multiplataforma
* Utilização em automação e integração de sistemas

## Variáveis e tipos de dados

Python utiliza tipagem dinâmica, portanto o tipo da variável é definido de acordo com o valor atribuído.

```python
nome = "Jorge"
idade = 20
altura = 1.75
ativo = True
```

Tipos básicos:

| Tipo    | Descrição                  |
| ------- | -------------------------- |
| `str`   | Texto                      |
| `int`   | Número inteiro             |
| `float` | Número decimal             |
| `bool`  | Verdadeiro ou falso        |
| `list`  | Lista de valores           |
| `dict`  | Estrutura de chave e valor |

## Estruturas condicionais

As estruturas `if`, `elif` e `else` permitem executar diferentes trechos do código de acordo com determinadas condições.

```python
temperatura = 25.5

if temperatura > 30:
    print("Temperatura alta")
elif temperatura >= 20:
    print("Temperatura normal")
else:
    print("Temperatura baixa")
```

## Estruturas de repetição

O `for` é utilizado principalmente para percorrer sequências ou repetir uma operação.

```python
for numero in range(5):
    print(numero)
```

O `while` mantém a execução enquanto uma condição for verdadeira.

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

## Funções

Funções permitem separar uma determinada tarefa em um bloco reutilizável, facilitando a organização e manutenção do código.

```python
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

media = calcular_media(8, 7)
print(media)
```

## Bibliotecas

Bibliotecas podem ser utilizadas para adicionar funcionalidades ao projeto sem a necessidade de implementar tudo do zero.

Exemplo utilizando a biblioteca `math`:

```python
import math

resultado = math.sqrt(25)
print(resultado)
```

