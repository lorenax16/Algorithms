def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    contador = 0
    for tempo in permanence_period:
        if not isinstance(tempo[0], int) or not isinstance(tempo[1], int):
            return None
        if tempo[0] <= target_time <= tempo[1]:
            contador += 1
    return contador
