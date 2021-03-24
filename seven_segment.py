import machine

# Classe que representa um display de 7 segmentos
# pode ser configurado como anodo comum ou catodo comum
# por padrão é inicializado como catodo
class Display:

    # o construtor do diplay recebe os pinos correspondentes à cada segmento
    def __init__(self, a, b, c, d, e, f, g):
        self.common_cathode()
        self.a = machine.Pin(a, machine.Pin.OUT)
        self.b = machine.Pin(b, machine.Pin.OUT)
        self.c = machine.Pin(c, machine.Pin.OUT)
        self.d = machine.Pin(d, machine.Pin.OUT)
        self.e = machine.Pin(e, machine.Pin.OUT)
        self.f = machine.Pin(f, machine.Pin.OUT)
        self.g = machine.Pin(g, machine.Pin.OUT)

    # indica que o display é de catodo comum
    # no display de catodo cumum
    # o nivel lógico alto acende o segmento
    # o nivel lógico baixo apaga o segmento
    def common_cathode(self):
        self.on = 1
        self.off = 0

    # indica que o display é de anodo comum
    # no display de anoodo cumum
    # o nivel lógico baixo acende o segmento
    # o nivel lógico alto apaga o segmento
    def common_anode(self):
        self.on = 0
        self.off = 1
    
    # apresenta o número informado
    def show(self, digito):
        if digito == 0:
            self._state(self.on, self.on, self.on, self.on, self.on, self.on, self.off)
            return
        if digito == 1:
            self._state(self.off, self.on, self.on, self.off, self.off, self.off, self.off)
            return
        if digito == 2:
            self._state(self.on, self.on, self.off, self.on, self.on, self.off, self.on)
            return
        if digito == 3:
            self._state(self.on, self.on, self.on, self.on, self.off, self.off, self.on)
            return
        if digito == 4:
            self._state(self.off, self.on, self.on, self.off, self.off, self.on, self.on)
            return
        if digito == 5:
            self._state(self.on, self.off, self.on, self.on, self.off, self.on, self.on)
            return
        if digito == 6:
            self._state(self.on, self.off, self.on, self.on, self.on, self.on, self.on)
            return
        if digito == 7:
            self._state(self.on, self.on, self.on, self.off, self.off, self.on, self.off)
            return
        if digito == 8:
            self._state(self.on, self.on, self.on, self.on, self.on, self.on, self.on)
            return
        if digito == 9:
            self._state(self.on, self.on, self.on, self.on, self.off, self.on, self.on)
            return
        
    # altera o estado de ligado/desligado de cada um dos 7 segmentos
    def _state(self, a, b, c, d, e, f, g):
        self.a.value(a)
        self.b.value(b)
        self.c.value(c)
        self.d.value(d)
        self.e.value(e)
        self.f.value(f)
        self.g.value(g)
