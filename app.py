memoria = []

def asignar_cama(paciente, diagnostico, urgencia, camas_uci):

    print("\nAnalizando paciente...")

    if urgencia.lower() == "alta":

        if camas_uci > 0:
            decision = "Asignar cama UCI"
        else:
            decision = "Lista de espera UCI"

    else:
        decision = "Asignar cama hospitalaria general"

    registro = {
        "paciente": paciente,
        "diagnostico": diagnostico,
        "decision": decision
    }

    memoria.append(registro)

    return f"""
Paciente: {paciente}
Diagnóstico: {diagnostico}
Urgencia: {urgencia}

Decisión del agente:
{decision}
"""


# CASO 1
resultado1 = asignar_cama(
    "Maria Gonzalez",
    "Neumonia grave",
    "Alta",
    2
)

# CASO 2
resultado2 = asignar_cama(
    "Pedro Soto",
    "Fractura menor",
    "Baja",
    0
)

# CASO 3
resultado3 = asignar_cama(
    "Carlos Rojas",
    "Infarto agudo",
    "Alta",
    0
)

print(resultado1)
print(resultado2)
print(resultado3)

print("\nHistorial almacenado en memoria:")

for item in memoria:
    print(item)