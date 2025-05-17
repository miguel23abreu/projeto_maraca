import serial
import pygame
import random
import socket
from pydub import AudioSegment
from pydub.playback import play
import threading

UDP_IP = "0.0.0.0"  # Escuta em todas as interfaces
UDP_PORT = 5006    # Porta UDP

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# Variável global para armazenar a última leitura do socket
ultima_leitura = "0"

def receber_dados():
    global ultima_leitura
    while True:
        data, _ = sock.recvfrom(1024)  # Aguarda pacotes UDP
        ultima_leitura = data.decode()  # Atualiza a variável global

# Inicia a thread para escutar os pacotes sem travar o programa
threading.Thread(target=receber_dados, daemon=True).start()

while True:
    try:
        arduino = serial.Serial('COM3', 115200)
        print('Arduino conectado')
        break
    except:
        pass

pygame.init()
display_x = 500
display_y = 200
display = pygame.display.set_mode((display_x, display_y))
clock = pygame.time.Clock()
maraca = pygame.image.load('teste_pygame/maraca_02_per.png')
maraca_ani = pygame.image.load('teste_pygame/maraca_03_red.png')

Running = True
x = display_x / 2
y = display_y / 2

cont = 0  # contador para evitar que o primeiro valor lido seja validado
frequencia = 0  # frequência
freq_last = 0

# Função para tocar áudio em uma thread separada
def tocar_som(som):
    play(AudioSegment.from_mp3(som))

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    display.fill("purple")

    freq_last = frequencia
    leitura = ultima_leitura  # Usa a variável global que foi atualizada pela thread
    cont += 1

    numRandom = random.randint(0, 80)

    if cont > 1 and leitura:
        try:
            frequencia = int(leitura[2])  # Lendo o valor da frequência
        except (IndexError, ValueError):
            frequencia = 0  # Garante que não quebre o código se a leitura for inválida

        print('Frequência:', frequencia)
        print('Número aleatório:', numRandom)

        display.blit(maraca, (x, y))

        # Definindo o áudio de acordo com a frequência
        if frequencia % 4 == 0:
            som = 'som/audio_4_gonza_rec.mp3'
        elif frequencia % 3 == 0:
            som = 'som/audio_3_gonza_rec.mp3'
        elif frequencia % 2 == 0:
            som = 'som/audio_2_gonza_rec.mp3'
        else:
            som = 'som/audio_1_gonza_rec.mp3'

        # Simulando canais diferentes sem bloquear o loop principal
        if numRandom > 72:
            print('Tocando nos dois canais')
            threading.Thread(target=tocar_som, args=(som,)).start()
            threading.Thread(target=tocar_som, args=(som,)).start()

        elif numRandom < 40:
            print('Tocando no canal 1')
            threading.Thread(target=tocar_som, args=(som,)).start()

        else:
            print('Tocando no canal 2')
            threading.Thread(target=tocar_som, args=(som,)).start()

    if frequencia == freq_last:
        print('Frequências iguais')
        display.fill("purple")
        maraca_center = pygame.transform.rotozoom(maraca_ani, 0, 1)
        display.blit(maraca_center, (x, y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
