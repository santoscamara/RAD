## ms8.py


import time

def get_coxinhas(*pedidos):
    print("--- [Return] Preparando TODA a fornada de coxinhas de uma vez....")
    time.sleep(1) # Simula um processo demorado
    return [f'{pedido} coxinhas' for pedido in pedidos]

def get_joelho(*pedidos):
    for pedido in pedidos:
        print(f'--- [Yield] Saindo um pedido de {pedido} joelho(s) agora!')
        time.sleep(5) #Simula o processo de fritar um por um
        yield f'{pedido} joelho(s)'

if __name__ == "__main__":
    print("SOLICITANDO COXINHAS (Return):")
    salgados_return = get_coxinhas(4,6,8)
    print("Recebi a list completa:", salgados_return)

    print("\n" + "-"*30 + "\n")

    print("SOLICITANDO JOELHOS (Yield):")
    pedidos_joelhos = get_joelho(4,6,8)
    for salgado in pedidos_joelhos:
        print(f"Cliente recebeu: {salgado}")
