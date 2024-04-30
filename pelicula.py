import json

class Pelicula:
    def __init__(self, id, name, year):
        self.id = id
        self.name = name
        self.year = year

    def __repr__(self) -> str:
        return f"Pelicula(id={self.id}, name={self.name}, year={self.year})"
    
    @classmethod
    def from_json(cls, json_data):
        return cls(json_data['id'], json_data['name'], json_data['year'])
    
# Función para cargar datos desde un archivo JSON y convertirlos en objetos Pelicula
def cargar_peliculas_desde_json(data):
    with open(data, 'r') as dt:
        datos_json = json.load(dt)
        return [Pelicula.from_json(pelicula) for pelicula in datos_json]

# Función para guardar datos (objetos Pelicula) en un archivo JSON
def guardar_peliculas_en_json(peliculas, data):
    datos_json = [pelicula.__dict__ for pelicula in peliculas]
    with open(data, 'w') as dt:
        json.dump(datos_json, dt, indent=4)

# Ejemplo de uso
if __name__ == "__main__":
    # Cargar datos desde el archivo JSON
    peliculas = cargar_peliculas_desde_json('data.json')

    # Imprimir las películas cargadas
    for pelicula in peliculas:
        print(pelicula)

    # Modificar una película (por ejemplo, cambiar el título)
    peliculas[0].name = "Vengadores Infinity War"

    # Guardar las películas modificadas de vuelta al archivo JSON
    guardar_peliculas_en_json(peliculas, 'data.json')
    
