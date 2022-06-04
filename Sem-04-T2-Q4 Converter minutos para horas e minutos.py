def minutos_para_horas(qtd_minutos):
    horas = qtd_minutos // 60
    minutos = qtd_minutos % 60
    return f'{horas}:{minutos}'

minutos = int(input())
horas = minutos_para_horas(minutos)
print(horas)
