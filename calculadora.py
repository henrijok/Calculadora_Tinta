class Calculadora:
    __area_paredes:float    #PRIVATE
    __area_teto:float       #PRIVATE

    def calcular_area_paredes(self, comodo):
        self.__area_paredes = 2 * (comodo.largura + comodo.profundidade) * comodo.altura
        return self.__area_paredes

    def calcular_area_teto(self, comodo):
        self.__area_teto = comodo.largura * comodo.profundidade
        return self.__area_teto

    def calcular_litragem_tinta(self):
        if self.__area_paredes <= 0 or self.__area_teto <=0:
            print('Não foi possivel calcular a litragem com os valores informados')
            exit()
        return (self.__area_teto + self.__area_paredes) / 10


