def fazer_big_mac (nome):
    print (f'sanduiche big mac {nome}')


def fazer_batata (tamanho):
    print (f"batata {tamanho}")  

def preparar_refrigerante (tipo, tamanho):
    print (f'{tipo} {tamanho}')    


fazer_big_mac ("Vanessa")
fazer_batata ("Grande")
preparar_refrigerante ("Coca-cola", "Media")

def combo_bigmac (nome, tamanho_batata, tipo_refrigerante, tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata (tamanho_batata)
    preparar_refrigerante (tipo_refrigerante, tamanho_refri)
    
combo_bigmac ("Mauro", "Media", "Coca-cola", "Grande")    