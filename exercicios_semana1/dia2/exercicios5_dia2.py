# dia 2 semana 1 revisão o basico em python 

#Exercicios 5

produtos = {
    "Teclado Mecânico": 349.90,
    "Mouse Gamer": 129.50,
    "Monitor 24\"": 899.99,
    "Cadeira Ergonômica": 1199.00,
    "Headset Bluetooth": 259.90,
    "HD Externo 1TB": 349.00,
    "SSD 480GB": 279.99,
    "Webcam Full HD": 189.90,
    "Microfone USB": 229.00,
    "Base para Notebook": 119.00,
    "Hub USB 3.0": 89.90,
    "Cabo HDMI 2m": 39.90,
    "Mouse Pad RGB": 99.90,
    "Luminária de Mesa": 149.00,
    "Fonte 650W": 459.90
}


print('Lista de produtos')

for c,v in produtos.items():
    print(f'\n{c}: R${v:.2f}')