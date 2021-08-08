
productos{
    Deportesxyz{
        Zapatos{
            "Masculino"= 'ZapatosXYZ', 'codigo_barras' : 8369741233658,
            "Femenino"= 'ZapatosABC', 'codigo_barras' : 7452136985471
        }
        Camisas{
            "Masculino"= 'CamisaDEF', 'codigo_barraas' :5236412896324
        }
    }
    CarteraHi_Fashion{
        Bolso{
            "Femenino"= 'Bolso', 'codigo_barras' : 5863219635478
        }
    }
}

x = input("digite el codigo de barras: ")
if x == 8369741233658:
    print("el producto escogido es: Masculino = 'ZapatosXYZ'")
    if x == 7452136985471:
        print("el producto escogido es: Femenino = 'ZapatosABC'")
        if x == 5236412896324:
            print("el producto escogido es: Masculino = 'CamisaDEF")
    elif x == 5863219635478:
        print("el producto escogido es: Femenino = 'Bolso")
else:
    print("el codigo ingresado es erroneo")
