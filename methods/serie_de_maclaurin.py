from methods import serie_taylor

def serie_maclaurin(funcion, n, punto):
    return serie_taylor(funcion, 0, n, punto)  # Maclaurin es un caso especial de Taylor en x₀=0