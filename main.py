from seven_segment import Display
import machine
import utime

# display de 7 segmentos com anodo comum
# os segmentos estão conectados nos GPIOs de 0 à 6
display = Display(0, 1, 2, 3, 4, 5, 6)
display.common_anode()

# LED azul conectado na GPIO 16
led_azul = machine.Pin(16, machine.Pin.OUT)

# LED onboard do Raspberry Pi Pico
led_verde = machine.Pin(25, machine.Pin.OUT)

# variável que vai determinar se incrementa +1 ou -1
incremento = 1

# número a ser apresentado no display
numero = 0

# função para obter o próximo número
def proximoNumero():
    global numero
    global incremento
    numero += incremento
    if (numero == 9): # quando chegar em 9, conta de 9 à 0
        incremento = -1
    if (numero == 0): # quando chegar em 0, conta de 0 à 9
        incremento = 1

# loop infinito do programa
while True:
    led_verde.value(1)   # acende o LED onboard
    led_azul.value(0)    # apaga o LED azul
    display.show(numero) # apresenta o número atual
    utime.sleep(1)       # aguarda 1 segundo
    proximoNumero()      # incrementa ou decrementa o número atual
    
    led_verde.value(0)   # apaga o LED onboard
    led_azul.value(1)    # acende o LED azul
    display.show(numero) # apresenta o número atual
    utime.sleep(1)       # aguarda 1 segundo
    proximoNumero()      # incrementa ou decrementa o número atual

