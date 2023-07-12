# Sistema que calcula o valor hora trabalhada


salario = float(input("Informe o seu salario Bruto: "))
dia = float(input("Informe o total de dias trabalhados na semana: "))
horas = float(input("Informe o numero de horas trabalhadas por dia: "))
semana =float(input("Informe o numero de semanas trabalhados no mês: "))

horasSemanais = horas * dia
horasMensais = horasSemanais * semana
valorHora = salario / horasMensais
print("-"*100)
print(f"Voce trabalha {horasSemanais} horas semanais")
print(f"Voce trabalha {horasMensais} horas mensais")
print(f"Voce recebe R$ {valorHora} por hora trabalhada")
