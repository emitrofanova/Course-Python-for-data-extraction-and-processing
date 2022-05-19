def DEPOSIT(parameters):
    if parameters[0] not in clients:
        clients[parameters[0]] = 0
    clients[parameters[0]] += int(parameters[1])
    return clients[parameters[0]]
    #зачислить сумму sum на счет клиента name. 
    #Если у клиента нет счета, то счет создается.
def WITHDRAW(parameters):
    if parameters[0] not in clients:
        clients[parameters[0]] = 0
    clients[parameters[0]] -= int(parameters[1])
    return clients[parameters[0]]
    #снять сумму sum со счета клиента name. 
    #Если у клиента нет счета, то счет создается
def BALANCE(parameters):
    if parameters[0] in clients:
        return clients[parameters[0]]
    else:
        return 'ERROR' 
    #узнать остаток средств на счету клиента name
    #Если же у клиента с запрашиваемым именем не 
    #открыт счет в банке, выведите ERROR
def TRANSFER(parameters):
    if parameters[0] not in clients:
        clients[parameters[0]] = 0
    if parameters[1] not in clients:
        clients[parameters[1]] = 0
    clients[parameters[0]] -= int(parameters[2])
    clients[parameters[1]] += int(parameters[2])
    return clients[parameters[0]], clients[parameters[1]]
    #перевести сумму sum со счета клиента name1 на счет клиента name2. 
    #Если у какого-либо клиента нет счета, то ему создается счет. 
def INCOME(parameters):
    for client in clients:
        if clients[client] > 0:
            clients[client] = clients[client] * (100 + int(parameters[0])) // 100
    return clients

    #начислить всем клиентам, у которых открыты счета, p от суммы
    # счета. Проценты начисляются только клиентам с положительным 
    # остатком на счету, если у клиента остаток отрицательный, 
    # то его счет не меняется. После начисления процентов сумма на
    #  счету остается целой, то есть начисляется только целое число 
    #  денежных единиц. Дробная часть начисленных процентов отбрасывается.

numoper = int(input())
clients = {}
for i in range(numoper):
    string = list(input().split())
    function = string[:1]
    parameters = string[1:]
    if function[0] == 'DEPOSIT':
        DEPOSIT(parameters)
    if function[0] == 'WITHDRAW':
        WITHDRAW(parameters)
    if function[0] == 'BALANCE':
        print(BALANCE(parameters))
    if function[0] == 'TRANSFER':
        TRANSFER(parameters)
    if function[0] == 'INCOME':
        INCOME(parameters)
