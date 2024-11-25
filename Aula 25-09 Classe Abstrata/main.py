from abstrato import *

if __name__ == '__main__':
    gere = Gerente('Rafael', '45428901802', 2245)
    opera = Operador_Caixa('Dennis', '123456', 12030, 22)
    segu = Seguranca('Marina', '99795728768', 1325, 10)

    print(gere)
    if gere.autenticar('45428901802', 2245):
        print(gere.cancelar_operação())
    else:
        print(f'Falha na Autenticação.')
    
    print('<------------------------>')

    print(opera)
    if opera.autenticar(22, 12030):
        print(opera.registrar_produto())
    else:
        print(f'Falha na Autenticação.')

    print('<------------------------>')

    print(segu)
    if segu.autenticar(10, 1325):
        print(segu.acionar_alarme())
    else:
        print(f'Falha na Autenticação.')
