import serial
import soundfile as sf #biblioteca utilizada para manipular o audio
import sounddevice as sd #bibiioteca utilizada para reproduzir o audio
cont = 0 #contador para evitar que o primeiro valor lido na variavel seja validado
frequencia = 0 #frequencia
audio_file = 'som/som-padrao.wav'
audio_data, sample_rate = sf.read(audio_file)
while True:
    try:
        arduino = serial.Serial('COM6', 9600)
        print('Arduino conectado')
        break
    except:
        pass
while True:
    leitura = str(arduino.readline())
    cont += 1
    if(cont > 1):
        frequencia = int(leitura[2])
        #definindo o tempo do audio de acordo com a frequencia
        if(frequencia == 1 or frequencia > 4):
            start_time_sec = 0
            print(5*'-' + str(frequencia) + 5*'-')
            print(start_time_sec)
            end_time_sec = start_time_sec + 0.170*(frequencia+1)
            print(end_time_sec)
            print(11 * '-')
        else:
            start_time_sec = 0.170*(frequencia)
            print(5 * '-' + str(frequencia) + 5 * '-')
            print(start_time_sec)
            end_time_sec = start_time_sec + 0.170*2
            print(end_time_sec)
            print(5 * '-' + str(frequencia) + 5 * '-')
        start_time_ms = int(start_time_sec * 1000) #convertendo o tempo inicial para milisegundos
        end_time_ms = int(end_time_sec * 1000) #convertendo o tempo final para milisegundos
        start_sample = int(start_time_ms * sample_rate / 1000) #convertendo o tempo inicial para amostra o comando abaixo segue o mesmo objetivo
        end_sample = int(end_time_ms * sample_rate / 1000)
        audio_segment = audio_data[start_sample:end_sample] #criando o audio
        sd.play(audio_segment, sample_rate) #reproduzindo o audio
        sd.wait() #esperando o audio terminar