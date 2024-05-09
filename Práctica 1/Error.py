class Error:
    def divideError(self, dividendo, divisor):
        dividendo = float(dividendo)
        divisor = float(divisor)
        resultado = dividendo/divisor
        return resultado
    
    def divideCatch(self, dividendo, divisor):
        try:
            dividendo = float(dividendo)
            divisor = float(divisor)
            resultado = dividendo/divisor
            return resultado
        except ZeroDivisionError as e:
            print("Error:", e)
            return False