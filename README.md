# Graph Coloring Hill Climbing - A Graph Coloring Optimization Tool

Este projeto implementa uma ferramenta de coloração de grafos utilizando algoritmos baseados em Subida de Encosta (_Hill Climbing_). A aplicação oferece duas variações do algoritmo: **Escolha Primeiro Melhor** (_First Choice_) e **Escolha Mais Íngreme** (_Steepest Choice_). O objetivo é minimizar conflitos de coloração em grafos gerados dinamicamente ou definidos pelo usuário.

## Pré-requisitos

- **Python** >= 3.7
- **Poetry** >= 1.1.0
- **Brew** (para gerenciar dependências)

## Estrutura do Projeto

O projeto segue a seguinte organização:

```
src/
   main.py
pyproject.toml
poetry.lock
README.md
```

## Como Usar

### Instalação das Dependências

Antes de executar a aplicação, é necessário instalar as dependências do projeto utilizando o **Brew** e o gerenciador de pacotes **Poetry**.

1. Certifique-se de que o **Brew** e o **Poetry** estão instalados no seu sistema:

   ```bash
   brew install poetry
   ```

2. Navegue até o diretório raiz do projeto (onde se encontra o arquivo `pyproject.toml`) e instale as dependências:

   ```bash
   poetry install
   ```

3. Ative o ambiente virtual gerenciado pelo Poetry:
   ```bash
   poetry shell
   ```

### Executando a Aplicação

Com o ambiente virtual ativo, você pode executar o arquivo principal para iniciar a aplicação. O programa permite gerar grafos, escolher algoritmos e visualizar os resultados.

```bash
python src/main.py
```

### Funcionalidades Disponíveis

Durante a execução, você terá as seguintes opções:

1. **Gerar grafo** com diferentes quantidades de vértices (10, 50, 100 ou um valor personalizado).
2. **Definir o número máximo de arestas** que cada nó pode ter.
3. **Selecionar a variante do algoritmo**:
   - _First Choice_ (Escolha Primeiro Melhor)
   - _Steepest_ (Escolha Mais Íngreme)
4. **Visualizar o grafo gerado e colorido** (opcional).

### Exemplo de Execução

#### Entrada:

- Escolha de 50 vértices
- Número máximo de arestas: 3
- Variante do algoritmo: _First Choice_
- Visualização: Sim

#### Saída esperada:

- Número de conflitos iniciais: 15
- Número de iterações realizadas: 125
- Número de conflitos finais: 0 (grafo devidamente colorido)

A visualização exibirá o grafo colorido em uma interface gráfica.

---

Desfrute da aplicação e otimize suas colorações de grafos! 🚀
