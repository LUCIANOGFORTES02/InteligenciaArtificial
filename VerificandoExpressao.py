def dividindoExpressao(lista):

    #Lista_elementos=[]#Gravar os elementos da expressao nessa lista
    #elemento=""
    x=lista.split(" ")
    print(x)

    return x
 


def OrdemOperacoes (expressao):
    dic={}

    if '(' in expressao:
        parenteseAbertura = [i for i, item in enumerate(expressao) if item == '(']#Loop com indices para
        parenteseFechamento = [i for i, item in enumerate(expressao) if item == ')']#Descobrir a posição na expressao
        #Pega o parentese max de abertura e o próximo de fechamento 
        print (max(parenteseAbertura))
        print (parenteseFechamento)

        for i in parenteseFechamento:
            
            if parenteseFechamento[i]>max(parenteseAbertura):

                posicao=i
                break

        print (posicao)


    return dic









#23 + 12 – 55 + (2 + 4) – 8 / 2^2

lista = "23 + 12 - 55 + ( 2 + 4 ) - 8 / 2 ^ 2"

x=dividindoExpressao(str(lista))
OrdemOperacoes(x)