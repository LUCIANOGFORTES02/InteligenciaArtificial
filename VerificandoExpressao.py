def dividindoExpressao(lista):

    #Lista_elementos=[]#Gravar os elementos da expressao nessa lista
    #elemento=""
    x=lista.split(" ")
    print(x)

    return x
 


def OrdemOperacoes (expressao):
    dic={}

    if '(' in expressao:
        parenteseAbertura = [i for i, j in enumerate(expressao) if j == '(']#Loop com indices para
        parenteseFechamento = [i for i, j in enumerate(expressao) if j == ')']#Descobrir a posição na expressao
        #Pega o parentese max de abertura e o próximo de fechamento
        
        for i in range (0,max(parenteseFechamento)):#Para pegar o parentese de fechamento
            if parenteseFechamento[i]>max(parenteseAbertura):
                posicao=i
                break
        
        if len(expressao[max(parenteseAbertura)+1:parenteseFechamento[posicao]-1]) <= 3:
            valor1 = float (expressao[max(parenteseAbertura) + 1])
            valor2 = float (expressao[parenteseFechamento[posicao]- 1])
            dic['valor1'] = valor1
            dic['valor2'] = valor2
            dic['Op'] = expressao[max(parenteseAbertura) + 2]
            dic['indiceOp'] = indiceOperador(expressao, max(parenteseAbertura), dic['Op']) - 1
            del(expressao[min(parenteseFechamento)])#Deleta os parenteses na expressão
            del(expressao[max(parenteseAbertura)])
        else:
            dic = OrdemOperacoes(expressao[max(parenteseAbertura)+1:parenteseFechamento[posicao]])
            dic['indiceOp'] += max(parenteseAbertura) + 1

    
    elif '^' in expressao:
        valor1 = float (expressao[expressao.index('^') - 1])
        valor2 = float (expressao[expressao.index('^') + 1])
        n = [i for i, j in enumerate(expressao) if j == '^']
        dic['valor1'] = valor1
        dic['valor2'] = valor2
        dic['Op'] = '^'
        dic['indiceOp'] = expressao.index(dic['Op'])
        
    elif '*' in expressao:
        valor1 = float (expressao[expressao.index('*') - 1])
        valor2 = float (expressao[expressao.index('*') + 1])
        dic['valor1'] = valor1
        dic['valor2'] = valor2
        dic['Op'] = '*'
        dic['indiceOp'] = expressao.index(dic['Op'])

    elif '/' in expressao:
        valor1 = float (expressao[expressao.index('/') - 1])
        valor2 = float (expressao[expressao.index('/') + 1])
        dic['valor1'] = valor1
        dic['valor2'] = valor2
        dic['Op'] = '/'
        dic['indiceOp'] = expressao.index(dic['Op'])

    elif '-' in expressao:
        valor1 = float (expressao[expressao.index('-') - 1])
        valor2 = float (expressao[expressao.index('-') + 1])
        dic['valor1'] = valor1
        dic['valor2'] = valor2
        dic['Op'] = '-'
        dic['indiceOp'] = expressao.index(dic['Op'])

    elif '+' in expressao:
        valor1 = float (expressao[expressao.index('+') - 1])
        valor2 = float (expressao[expressao.index('+') + 1])
        dic['valor1'] = valor1
        dic['valor2'] = valor2
        dic['Op'] = '+'
        dic['indiceOp'] = expressao.index(dic['Op'])
    







    return dic




def indiceOperador(list, parantheses_ini, operacao):
    temp = list[parantheses_ini:]
    for i in range(1, len(temp)):
        if temp[i] == operacao:
            return i + parantheses_ini




#"23 + 12 - 55 + ( 2 + 4 ) - 8 / 2 ^ 2"

lista = "( (100 - 413 ) * ( 20 - 5 * 4 ) + 25 ) / 5"
# data = separateString("(100 – 413 * (20 – 5 * 4) + 25) / 5")
x=dividindoExpressao(str(lista))
y=OrdemOperacoes(x)
print(y["Op"])

