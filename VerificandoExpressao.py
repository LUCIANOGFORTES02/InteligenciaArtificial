def dividindoExpressao(lista):

    #Lista_elementos=[]#Gravar os elementos da expressao nessa lista
    #elemento=""
    x=lista.split(" ")
    print(x)

    return x
 


def OrdemOperacoes (expressao):
    dic={}

    if '(' in expressao:
        openParentheses = [i for i, item in enumerate(expressao) if item == '(']#
        closedParentheses = [i for i, item in enumerate(expressao) if item == ')']#
    print (openParentheses[0])
        


    return dic









#23 + 12 – 55 + (2 + 4) – 8 / 2^2

#lista = "23 + 12 - 55 + ( 2 + 4 ) - 8 / 2 ^ 2"

#x=dividindoExpressao(str(lista))
#OrdemOperacoes(x)