def criandoPeixes():
    # necessario 1 litro para cada Cm de peixe
    listaPeixes = []
    tamanho = float(input("Digite o tamanho médio dos peixes criados (em Centímetros): "))
    quantidadePeixes = float(input("Digite aproximadamente a quantidade de peixes existentes: "))
    volumeMin = tamanho * quantidadePeixes * 1  # 1 litro = 1 metro cubico de volume
    listaPeixes.append(volumeMin)

    # Alimentação saudável dos peixes = 1,4 a 1,8 kg de ração por kg de peixe.
    peso = float(input("Digite o peso médio do peixe criado (em kg): "))
    alimentoMin = peso * quantidadePeixes * 1.4
    listaPeixes.append(alimentoMin)
    return listaPeixes


def parametrosOceano():
    # No oceano uma elevação de 150 partes por milhão de CO2 na atmosfera gera um diminuição de 0,1pH aproximadamente
    # A superfície dos oceanos, em seu conjunto, tem um pH que varia entre 8,0 e 8,3. (considerando aproximadamente pH 8 para o estado atual do oceano)
    listaOceano = []
    variacaoCo2 = float(input("Digite a variação de gás carbônico na atmosfera (em ppm): "))
    phvar = 0
    if variacaoCo2 != 0:
        phvar = (variacaoCo2 / 150) * (-0.1)
        ph = 8 + phvar
    else:
        respostaph = "Não houve variação de pH."

    if ph > 8 and ph < 8.3:
        respostaph = f"A variação de {phvar:.2f}pH, promoveu pH {ph:.2f} no oceano. Portanto está dentro do padrão científico estipulado (8 até 8.3)."
    else:
        respostaph = f"A variação de {phvar:.2f}pH, promoveu pH {ph:.2f} no oceano. Portanto está fora do padrão científico estipulado (8 até 8.3)."
    listaOceano.append(respostaph)

    #A média da temperatura da água situa-se entre 0°C e 24.9°C -> maior temperatura no oceano atlantico de 24.9°C
    temperatura = 0
    print("Para calcular a média da temperatura diária do oceano digite 3 temperaturas registradas ao longo do dia. ")
    for x in range(1,4):
        temperatura += int(input(f"Digite o {x}° registro: "))

    temperaturaMedia = temperatura / 3
    calculo = 24.9 - temperaturaMedia
    if calculo > 0:
        respostaTemperatura = f"A temperatura média calculada ({temperaturaMedia:.2f}°C) está {calculo:.2f}°C menor que o recorde de maior temperatura média do oceano que foi de 24,9°C. "
    else:
        calculo = calculo * (-1)
        respostaTemperatura = f"A temperatura média calculada ({temperaturaMedia:.2f}°C) é um NOVO RECORDE, está {calculo:.2f}°C maior que o ultimo recorde de maior temperatura média do oceano (24,9°C)"
    listaOceano.append(respostaTemperatura)
    return listaOceano

periodos = {
    "Piracema": {
        "duracao": "novembro até fevereiro",
        "sobre": "é um período em que muitas espécies de peixes sobem os rios para se reproduzirem.",
    },
    "Tainha": {
        "duracao": "abril até julho",
        "sobre": "é um período em que as tainhas migram em grandes cardumes para se reproduzirem em águas costeiras.",
    },
    "Período de Reprodução": {
        "duracao": "varia conforme a espécie",
        "sobre": "é o período em que os animais se reproduzem para garantir a continuidade da espécie.",
    },
}

running = True
while running:
    print("""
1 - Formular tabela sobre criação de peixes. (volume e ração estimados)
2 - Formular tabela sobre os parâmetros do oceano atlantico. (pH e temperatura) 
3 - Períodos de pesca.  
6 - Finalizar programa.  
    """)
    match int(input("Digite uma das opções acima: ")):
        case 1:
            infos = criandoPeixes()
            print(f"""
|Volume minimo do tanque | Ração minima |
|{infos[0]}m3       |{infos[1]} kg     | 
""")
        case 2:
            respostas = parametrosOceano()
            print(f"{respostas[0]}\n{respostas[1]}")
        case 3:
            options = []
            count = 1

            print()
            print("Períodos de pesca:")
            for option, _ in periodos.items():
                options.append(option)
                print(f"{count} - {option}")
                count += 1
            print()
            userinput = int(input("Digite uma das opções acima: "))
            periodo_nome = options[userinput - 1]
            periodo = periodos[periodo_nome]

            print(f"Duração: {periodo['duracao']}")
            print(f"Sobre: {periodo['sobre']}")
        case 6:
            print("Finalizando...")
            running = False
        case _:
            print("Falha ao encontrar opção, tente novamente")