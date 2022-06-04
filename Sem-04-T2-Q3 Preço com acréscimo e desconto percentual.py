def percentual(valor, porcentagem):
    return valor * (porcentagem / 100)

pr = float(input())
vr_p = float(input())
pr_acres = pr + percentual(pr, vr_p)
pr_desc = pr - percentual(pr, vr_p)
print(f'{pr_acres:5.2f}')
print(f'{pr_desc:5.2f}')

