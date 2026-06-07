def gerar_relatorio():
    temperatura = 28
    umidade = 65

    relatorio = f"""
RELATÓRIO CLIMÁTICO AUTOMÁTICO

Temperatura: {temperatura}°C
Umidade: {umidade}%

Análise:

Os dados indicam condições climáticas estáveis.
Sistemas baseados em Inteligência Artificial podem utilizar
informações obtidas por satélites para auxiliar no monitoramento ambiental.
"""

    return relatorio


print(gerar_relatorio())
