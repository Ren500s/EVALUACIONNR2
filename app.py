from datetime import datetime

def asignar_cama(paciente, diagnostico, urgencia, camas_uci):

    if urgencia.lower() == "alta" and camas_uci > 0:
        return f"Paciente {paciente}: asignar cama UCI."

    elif urgencia.lower() == "alta" and camas_uci == 0:
        return f"Paciente {paciente}: ingresar a lista de espera UCI."

    else:
        return f"Paciente {paciente}: asignar cama hospitalaria general."


resultado = asignar_cama(
    "Maria Gonzalez",
    "Neumonia grave",
    "Alta",
    2
)

print(resultado)