# Git

## Visão geral

Git é um sistema de controle de versão utilizado para acompanhar alterações em projetos e facilitar o trabalho com código.

Ele permite manter um histórico das alterações, criar versões do projeto e trabalhar com diferentes branches.

## Principais comandos

### Configuração

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

### Iniciar um repositório

```bash
git init
```

Cria um novo repositório Git na pasta atual.

### Clonar um repositório

```bash
git clone URL_DO_REPOSITORIO
```

Baixa uma cópia de um repositório existente.

### Ver alterações

```bash
git status
```

Mostra arquivos modificados, adicionados ou que ainda não estão sendo monitorados.

### Adicionar arquivos

```bash
git add .
```

Adiciona as alterações para o próximo commit.

Também é possível adicionar um arquivo específico:

```bash
git add arquivo.py
```

### Criar um commit

```bash
git commit -m "Descrição da alteração"
```

Registra as alterações no histórico do projeto.

### Enviar para o GitHub

```bash
git push
```

Envia os commits locais para o repositório remoto.

### Atualizar o projeto

```bash
git pull
```

Baixa as alterações mais recentes do repositório remoto.

## Branches

Branches permitem trabalhar em diferentes versões ou funcionalidades do projeto sem alterar diretamente a branch principal.

Criar uma branch:

```bash
git branch nova-funcionalidade
```

Trocar de branch:

```bash
git switch nova-funcionalidade
```

Criar e trocar para uma nova branch:

```bash
git switch -c nova-funcionalidade
```

## Fluxo básico

Um fluxo comum para atualizar um projeto é:

```bash
git status
git add .
git commit -m "Descrição da alteração"
git push
```

Para obter alterações do repositório antes de continuar trabalhando:

```bash
git pull
```

## Git e GitHub

Git e GitHub não são a mesma coisa.

* **Git:** ferramenta de controle de versão instalada no computador.
* **GitHub:** plataforma utilizada para hospedar repositórios Git e facilitar a colaboração.
