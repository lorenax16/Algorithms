def study_schedule(permanence_period, target_time):
    contador = 0

    if target_time == 0 or target_time is None:
        return None

    for tempo in permanence_period:
        if tempo[0] <= target_time <= tempo[1]:
            contador + 1
    return contador
