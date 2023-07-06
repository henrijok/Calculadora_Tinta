#IMPORTA AS CLASSES
from calculadora import Calculadora
from comodo import Comodo

#SOLICITA OS DADOS PARA O USUÁRIO NO TERMINAL
largura = input("Qual a largura do cômodo? ")
profundidade = input("Qual a profundidade do cômodo: ")

#INSTANCIA AS CLASSES
calc = Calculadora()
comodo = Comodo(largura, profundidade) #CONSTRUTOR

#IMPRIME OS RESULTADOS NO TERMINAL CHAMANDO OS MÉTODOS DA CLASSE CALCULADORA COM O ATRIBUTO CLASSE CÔMODO
print("\nA área das paredes é:", calc.calcular_area_paredes(comodo), "metros quadrados")
print("A área do teto é:", calc.calcular_area_teto(comodo), "metros quadrados")
print("A litragem de tinta necessária é:", calc.calcular_litragem_tinta(), "litros")

