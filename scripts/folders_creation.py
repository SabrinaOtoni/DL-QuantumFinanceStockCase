'''
Script python para criação automatizada da estrutura de pastas utilizada no projeto.
--------------------------------------
Sabrina Otoni da Silva - 2024/01
'''
# Importação da biblioteca necessária.
import os

# Dicionário que define a estrutura de pastas desejada
estrutura_pastas = {
    'data': {
        'csv': [],
        'imagens': {
            'teste': {
                'comprar': [],
                'vender': []
            },
            'treino': {
                'comprar': [],
                'vender': []
            }
        }
    },
    'notebook': [],
    'scripts': [],
    'preprocessing': [],
    'model': [],
    'documentation': []
}

# Caminho base onde as pastas serão criadas (diretório atual)
caminho_base = os.getcwd()

def criar_pastas(base, estrutura):
    """
    Cria uma estrutura de pastas baseada no dicionário fornecido.

    Parâmetros:
    base: str
        Caminho base onde as pastas serão criadas.
    estrutura: dict
        Dicionário representando a estrutura de pastas desejada.
    """
    # Itera sobre cada item (pasta e seu conteúdo) no dicionário da estrutura
    for pasta, conteudo in estrutura.items():

        # Verifica se o conteúdo é um dicionário (indicando subpastas)
        if isinstance(conteudo, dict):
            # Constrói o caminho da pasta e a cria se não existir
            caminho_pasta = os.path.join(base, pasta)
            os.makedirs(caminho_pasta, exist_ok=True)
            # Chamada recursiva para criar subpastas
            criar_pastas(caminho_pasta, conteudo)

        else:
            # Caso não seja um dicionário, cria a pasta
            caminho_pasta = os.path.join(base, pasta)
            os.makedirs(caminho_pasta, exist_ok=True)
            
            # Itera sobre cada subpasta na lista 'conteudo'
            for subpasta in conteudo:
                # Constrói o caminho da subpasta e a cria se não existir
                caminho_subpasta = os.path.join(caminho_pasta, subpasta)
                os.makedirs(caminho_subpasta, exist_ok=True)
                # Cria um arquivo .gitkeep em cada subpasta para garantir que elas sejam incluídas no Git
                with open(os.path.join(caminho_subpasta, '.gitkeep'), 'w') as f:
                    pass

# Chamando a função para criar a estrutura de pastas no caminho base
criar_pastas(caminho_base, estrutura_pastas)

