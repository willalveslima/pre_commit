# Projeto de Desenvolvimento Python - Pré-Commit

Este projeto implementa as práticas descritas no artigo [Aprimorando Qualidade de Código Python com Black, Flake8, Isort e Interrogate](https://medium.com/gbtech/aprimorando-qualidade-de-c%C3%B3digo-python-com-black-flake8-isort-e-interrogate-d5c089121357). O objetivo é utilizar pré-commits para garantir a qualidade do código.

Obs.: o projeto não utiliza Black e Interrogate

## Ferramentas Utilizadas

- **Flake8**: Análise de código para encontrar problemas de estilo e erros.
- **pydocstyle**: Análise de código para verificar a presença e adequação de docstrings.
- **Isort**: Ordenação automática de imports.
- **pytest**: Execução de testes automatizados.


## Configuração do Pré-Commit

Para configurar o pré-commit, siga os passos abaixo:

1. Instale o pré-commit:
    ```sh
    pip install pre-commit
    ```

2. Crie um arquivo `.pre-commit-config.yaml` na raiz do projeto com o seguinte conteúdo:
    ```yaml
      repos:
      - repo: local
        hooks:
        - id: isort
          name: Run isort
          types: [python]
          exclude: ^tests/
          entry: isort
          language: system
          exclude: /test
        - id: pydocstyle
          name: Roda pydocstyle
          types: [python]
          exclude: ^tests/
          entry: pydocstyle
          language: system
        - id: flake8
          name: Roda flake8
          types: [python]
          exclude: ^tests/
          entry: flake8
          language: system
        - id: pytest
          name: Roda pytest 
          entry: pytest
          language: system
          pass_filenames: false
          always_run: true
    ```

3. Instale os hooks do pré-commit:
    ```sh
    pre-commit install
    ```

4. Execute os hooks manualmente pela primeira vez:
    ```sh
    pre-commit run --all-files
    ```

## Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.
