Uma ferramenta que permite extrair combinações de login e senha de arquivos de texto (".txt") no formato `[url:login:senha]`. Ele apresenta os arquivos de texto disponíveis no diretório atual, permite que o usuário selecione um deles e salva os dados extraídos em um novo arquivo.

## Funcionalidades

1. **Seleção de Arquivo:**
   - Lista todos os arquivos `.txt` no diretório atual.
   - Permite que o usuário selecione o arquivo desejado digitando o número correspondente.
   - Opção de cancelar a operação.

2. **Extração de Dados:**
   - Processa cada linha do arquivo selecionado.
   - Extrai a combinação `login:senha` de linhas no formato `[url:login:senha]`.

3. **Geração de Resultado:**
   - Salva os dados extraídos em um arquivo chamado `result.txt` no mesmo diretório.

## Como Usar

1. Certifique-se de que os arquivos `.txt` a serem processados estejam no mesmo diretório que o script.
2. Execute o script em um terminal ou prompt de comando.
3. O script exibirá a lista de arquivos `.txt` no diretório atual.
4. Selecione o arquivo desejado digitando o número correspondente.
5. O script processará o arquivo e salvará os dados extraídos no arquivo `result.txt`.

## Estrutura do Código

- **`extract_login_pass(line)`**: Extrai a combinação `login:senha` de uma linha no formato esperado.
- **`transform_file(input_file, output_file)`**: Processa o arquivo de entrada linha por linha e salva os dados extraídos no arquivo de saída.
- **`obter_arquivo_de_entrada()`**: Lista os arquivos `.txt` no diretório atual e permite a seleção do arquivo desejado.
- **`main()`**: Orquestra a execução do script.

## Requisitos

- Python 3.x
- Sistema operacional que suporte cores ANSI no terminal para exibição das mensagens coloridas.

## Exemplo de Uso

### Entrada:
Arquivo `example.txt`:
```
https://example.com:user1:password1
https://example2.com:user2:password2
https://example3.com:user3:password3
```

### Saída:
Arquivo `result.txt`:
```
user1:password1
user2:password2
user3:password3
```

## Observações

- Apenas arquivos no formato `[url:login:senha]` serão processados corretamente. Entretando, uma melhoria para processar outros formatos será adicionada em breve.
- Caso nenhum arquivo `.txt` seja encontrado no diretório, o script será encerrado com uma mensagem de erro.
- É possível cancelar a operação digitando `0` ao ser solicitado para selecionar um arquivo.
