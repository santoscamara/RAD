from typing import List, Optional


class DicionarioSinonimos:
    """
    Encapsula o armazenamento e protege os dados de alterações externas diretas.
    """

    def __init__(self):
        #O sublinhado (_) indica que este atributo é "privado" (encapsulado)
        #As chaves são strings e os valores são listas de string
        self._dicionario: dict[str,List[str]]= {}

    def adicionar_palavra(self, palavra:str, sinonimos: List[str]) -> None:
        """
        se a palavra já existir , os novos sinonimos são mesclados sem duplicatas.
        """
        palavra_chave = palavra.strip().lower()
        sinonimos_limpos = [s.strip().lower() for s in sinonimos]

        if palavra in self._dicionario:
            #Junta os sinonimos existentes com os novos
            todos_sinonimos = self.dicionario[palavra_chave] + sinonimos_limpos
            #usa o set() para remover duplicatas e convete de volta para lista
            self._dicionario[palavra_chave] = list(set(todos_sinonimos))
            print(f'[Atualização] Sinonimos adicionados à palavra existente: {palavra_chave}')
        else:
            self._dicionario[palavra_chave] = list(set(sinonimos_limpos))
            print(f"[Sucesso] Nova palavra registrada '{palavra_chave}'")
        
    def buscar_sinonimos(self, palavra:str) -> Optional[List[str]]:
        """
        Retorna a lista de sinonimos ou None se a palavra não for encontrada
        """
        palavra_chave = palavra.strip().lower()

            # O metodo get() é mais seguro pois não gera KeyError se a palavra não existir

        sinonimos = self._dicionario.get(palavra_chave)

        if sinonimos:
            print(f"[Busca] Sinônimos de '{palavra_chave}': {', '.join(sinonimos)}")
            return sinonimos
        else:
            print(f"[Aviso] A palavra '{palavra_chave}' não foi encontrada.")
            return None
    
    def remover_palavra(self, palavra:str)-> bool:
        """
        Retorna true se removido com sucesso, False caso a palavra não exista
        """
        palavra_chave = palavra.strip().lower()
        if palavra_chave in self._dicionario:
            del self._dicionario[palavra_chave]
            print(f"[Sucesso] Palavra '{palavra_chave}' removida do dicionário")
            return True
        else:
            print(f"[Erro] Falha ao remover: '{palavra_chave}' não existe no dicionário.")
            return False
    
    def exibir_todos(self) -> None:
        print("\n--- Dicionario Completo ---")
        if not self._dicionario:
            print("O dicionário está vazio")
        for palavra, sinonimos in self._dicionario.items():
            print(f"- {palavra.capitalize()}: {', '.join(sinonimos)}")
        print("--------------------------------\n")


if __name__ == "__main__":
    #Instanciando o objeto
    meu_dicionario = DicionarioSinonimos()

    meu_dicionario.adicionar_palavra("feliz", ["alegre", "contente", "satisfeito"])
    meu_dicionario.adicionar_palavra("rápido", ["veloz", "ágil", "apressado"])
    #testando a normalização (letras maiúsculas e espaços) e tratamento de duplicatas

    meu_dicionario.adicionar_palavra(" Feliz ", ["Radiante", "Contente", "Alegre"])
    meu_dicionario.exibir_todos()
    sinonimos_feliz = meu_dicionario.buscar_sinonimos("FELIZ")
    sinonimos_triste = meu_dicionario.buscar_sinonimos("triste") #não existe
    print("\n")
    meu_dicionario.remover_palavra("rápido")
    meu_dicionario.remover_palavra("inteligente") # Tentando remover o que não existe

    meu_dicionario.exibir_todos()

         