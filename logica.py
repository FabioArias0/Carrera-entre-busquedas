import random


class logicaBusqueda:
    
    def obtener_datos(self, cantidad_elementos=9999, rango_numeros=(1, 10000)):
        datos = random.sample(range(*rango_numeros), cantidad_elementos)
        
        return datos
    
    
    def busqueda_secuencial(self, datos, objetivo):
        
        for i, dato in enumerate(datos):
            if dato == objetivo:
                return i
        return -1
    
    
    def busqueda_binaria(self, datos, objetivo):
        
        izquierda, derecha = 0, len(datos) - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if datos[medio] == objetivo:
                return medio
            elif datos[medio] < objetivo:
                izquierda = medio + 1
            else:
                derecha = medio - 1

        return -1
    
    def ordenamiento_burbuja(self, datos):
        
        n = len(datos)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if datos[j] > datos[j + 1]:
                    datos[j], datos[j + 1] = datos[j + 1], datos[j]
                    
    
    def quick_sort(self, datos):
        
        if len(datos) <= 1:
            return datos
        else:
            pivot = datos.pop()
            menores = []
            mayores = []
            for elemento in datos:
                if elemento <= pivot:
                    menores.append(elemento)
                else:
                    mayores.append(elemento)
            return self.quick_sort(menores) + [pivot] + self.quick_sort(mayores)
        
    
    def metodo_insercion(self, datos):
        
        for i in range(1, len(datos)):
            key = datos[i]
            j = i - 1
            while j >= 0 and key < datos[j]:
                datos[j + 1] = datos[j]
                j -= 1
            datos[j + 1] = key



