import os

#================##================#
cor_reset = "\033[0m"     
cor_vermelho = "\033[38;5;198m"  
cor_p_roxo = "\033[38;5;135m"
cor_p_azul = "\033[38;5;81m"
cor_p_verde = "\033[38;5;119m"
#================##================#

def vulgo_bloody():
    print(rf"""
{cor_p_verde} ==* coded by *== {cor_p_roxo}

 ██▒   █▓ ██▓ ██▓     ██▓    ▄▄▄       ███▄    █ 
▓██░   █▒▓██▒▓██▒    ▓██▒   ▒████▄     ██ ▀█   █ 
 ▓██  █▒░▒██▒▒██░    ▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒
  ▒██ █░░░██░▒██░    ▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒
   ▒▀█░  ░██░░██████▒░██████▒▓█   ▓██▒▒██░   ▓██░
   ░ ▐░  ░▓  ░ ▒░▓  ░░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒ 
   ░ ░░   ▒ ░░ ░ ▒  ░░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░
     ░░   ▒ ░  ░ ░     ░ ░    ░   ▒      ░   ░ ░ 
      ░   ░      ░  ░    ░  ░     ░  ░         ░ 
     ░                                           
      {cor_p_verde} ==*  {cor_vermelho}VL{cor_reset} ~ {cor_vermelho}villanelle{cor_reset} | {cor_vermelho}t.me/vi77an{cor_p_verde} *=={cor_reset}
""")

def extract_login_pass(line: str) -> str:
    """
    Extrai o [login:senha] de uma linha no formato [url:login:senha].
    """
    try:
        parts = line.rsplit(':', 2)
        if len(parts) == 3:
            return f"{parts[1]}:{parts[2]}"
    except Exception as e:
        print(f"{cor_vermelho}[Erro ao processar linha]: {line.strip()} - {e}{cor_reset}")
    return ""

def transform_file(input_file: str, output_file: str):
    """
    Lê o arquivo de entrada e escreve no arquivo de saída apenas [login:senha].
    """
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                transformed_line = extract_login_pass(line.strip())
                if transformed_line:
                    outfile.write(transformed_line + '\n')
    except Exception as e:
        print(f"{cor_vermelho}[Erro] Não foi possível processar o arquivo: {e}{cor_reset}")

def obter_arquivo_de_entrada():
    txt_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.txt')]

    if not txt_files:
        print(f"{cor_vermelho}[💔] Nenhum arquivo .txt foi encontrado no diretório atual.{cor_reset}")
        exit(1)

    print(f"{cor_p_roxo}[💌] Arquivos disponíveis:{cor_reset}")
    for i, file in enumerate(txt_files, 1):
        print(f"  [{i}] {file}")
    print("  [0] Cancelar e sair")

    while True:
        try:
            choice = int(input(f"{cor_p_roxo}[?] Selecione o número do arquivo desejado: {cor_p_verde}"))
            if choice == 0:
                print(f"{cor_p_roxo}[👋] Operação cancelada pelo usuário.{cor_reset}")
                exit(0)
            elif 1 <= choice <= len(txt_files):
                return txt_files[choice - 1]
            else:
                print(f"{cor_vermelho}[💔] Escolha inválida. Tente novamente.{cor_reset}")
        except ValueError:
            print(f"{cor_vermelho}[💔] Entrada inválida. Digite um número correspondente a um arquivo.{cor_reset}")

def main():
    vulgo_bloody()
    print('+-+-+-+-+-++-+-+-+-+-++-+-+-+-+-+-+')
    print(f'.:|| {cor_p_azul}URL:LOG:PASS to LOG:PASS {cor_reset}||:.')
    print('+-+-+-+-+-++-+-+-+-+-++-+-+-+-+-+-+\n')

    input_file = obter_arquivo_de_entrada()
    output_file = 'result.txt'

    transform_file(input_file, output_file)
    print(f"{cor_p_roxo}[💚] CONFIRA >> {cor_p_verde}{output_file}{cor_reset}")

if __name__ == "__main__":
    main()
