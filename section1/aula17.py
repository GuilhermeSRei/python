'''
CONSTANTE = "Variaveis" que não vão mudar
Muitas condições no if (ruim)
    <- Contagem de complexidade (ruim)
'''

velocidade = 61 # Velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distancia onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1

carro_pasou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado = carro_pasou_radar_1 and vel_carro_pass_radar_1

if carro_pasou_radar_1:
    print('Carro passou radar 1')

if carro_multado:
    print('Foi multado')


