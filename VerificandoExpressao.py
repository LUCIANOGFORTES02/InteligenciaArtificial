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
        print (parenteseAbertura)
        print (parenteseFechamento)

        for i in range (0,max(parenteseFechamento)):#Para pegar o parentese de fechamento
            if parenteseFechamento[i]>max(parenteseAbertura):
                posicao=i
                break
        
        if len(expressao[max(parenteseAbertura)+1:parenteseFechamento[posicao]-1]) <= 3:
            x1 = float (expressao[max(parenteseAbertura) + 1])
            x2 = float (expressao[parenteseFechamento[posicao]- 1])
            dic['x1'] = x1
            dic['x2'] = x2
            dic['Op'] = expressao[max(parenteseAbertura) + 2]
            dic['n'] = operationIndex(expressao, max(parenteseAbertura), dic['Op']) - 1
            del(expressao[min(parenteseFechamento)])#Deleta os parenteses na expressão
            del(expressao[max(parenteseAbertura)])
        else:
            dic = OrdemOperacoes(expressao[max(parenteseAbertura)+1:parenteseFechamento[posicao]])
            dic['n'] += max(parenteseAbertura) + 1

    """
    elif '^' in expressao:
        x1 = float (expressao[expressao.index('^') - 1])
        x2 = float (expressao[expressao.index('^') + 1])
        n = [i for i, item in enumerate(expressao) if item == '^']
        dic['x1'] = x1
        dic['x2'] = x2
        dic['Op'] = '^'
        dic['n'] = expressao.index(dic['Op'])
    elif '*' in expressao:
        x1 = float (expressao[expressao.index('*') - 1])
        x2 = float (expressao[expressao.index('*') + 1])
        dic['x1'] = x1
        dic['x2'] = x2
        dic['Op'] = '*'
        dic['n'] = expressao.index(dic['Op'])
    elif '/' in expressao:
        x1 = float (expressao[expressao.index('/') - 1])
        x2 = float (expressao[expressao.index('/') + 1])
        dic['x1'] = x1
        dic['x2'] = x2
        dic['Op'] = '/'
        dic['n'] = expressao.index(dic['Op'])
    elif '-' in expressao:
        x1 = float (expressao[expressao.index('-') - 1])
        x2 = float (expressao[expressao.index('-') + 1])
        dic['x1'] = x1
        dic['x2'] = x2
        dic['Op'] = '-'
        dic['n'] = expressao.index(dic['Op'])
    elif '+' in expressao:
        x1 = float (expressao[expressao.index('+') - 1])
        x2 = float (expressao[expressao.index('+') + 1])
        dic['x1'] = x1
        dic['x2'] = x2
        dic['Op'] = '+'
        dic['n'] = expressao.index(dic['Op'])
    """







    return dic




def operationIndex(list, parantheses_ini, operacao):
    temp = list[parantheses_ini:]
    for i in range(1, len(temp)):
        if temp[i] == operacao:
            return i + parantheses_ini




#"23 + 12 - 55 + ( 2 + 4 ) - 8 / 2 ^ 2"

lista = "( 100 - 413 * ( 20 - 5 * 4 ) + 25 ) / 5"
# data = separateString("(100 – 413 * (20 – 5 * 4) + 25) / 5")
x=dividindoExpressao(str(lista))
y=OrdemOperacoes(x)
print(y["Op"])