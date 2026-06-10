def asignar_cama(paciente, diagnostico, urgencia, camas_uci):

    print("\nAnalizando paciente...")

    if urgencia.lower() == "alta":

        if camas_uci > 0:
            decision = "Asignar cama UCI"
        else:
            decision = "Lista de espera UCI"

    else:
        decision = "Asignar cama hospitalaria general"

    return f"""
Paciente: {paciente}
Diagnóstico: {diagnostico}
Urgencia: {urgencia}

Decisión del agente:
{decision}
"""


resultado = asignar_cama(
    "Maria Gonzalez",
    "Neumonia grave",
    "Alta",
    2
)

print(resultado)