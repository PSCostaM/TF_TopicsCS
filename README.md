# TF_CC82_TopicosCS

 <h2 align="center">Universidad Peruana de Ciencias Aplicadas</h2>
<h2 align="center">Tópicos en Ciencias de la Computación - CC58</h2>
 
<h3 align="center"> TF</h3>
 
<h3 align="center"> Sección</h3>
<h3 align="center"> Profesor: Luis Martín Canaval Sanchez</h3>
<h3 align="center"> Alumnos</h3>
 <ul>
   <li align="center">Camargo Ramírez, Enzo Fabricio (U202010122)</li>
   <li align="center">Costa Mondragón, Paulo Sergio (U201912086)</li>
   <li align="center">Caballero Lara, Eduardo Roman (U202019644)</li>
 </ul>
 
 
 <h3 align="center">CICLO 2024-1</h3>


## Competencia específica del curso

<p align="justify">
 <b>ABET 1</b>: La capacidad de analizar un problema complejo y aplicar principios de computación y otras disciplinas relevantes para identificar soluciones.
Nivel de logro: 1
</p>

## Enunciado
<p align="justift">
El trabajo final consiste en elaborar un sistema multiagentes que permita simular la interacción de pokemones en un mundo abierto. Las características son las siguientes:
<ul>
<li>Existen pokemones de todos los tipos, por ejemplo fuego, eléctricos, etc.</li>
<li>Los pokemones existenen un mundo abierto y distribuidos según algún criterio a escoger por el grupo.</li>
<li>Se enfrentan entre ellos y el ganador se define según una tabla de probabilidades definido por las características de ventaja y desventaja de cada tipo contra cada otro tipo, por ejemplo un pokemon de agua es fuerte contra pokemones tipo fuego, de modo que tiene una mayor probabilidad de ganar la batalla.</li>
<li>Luego del enfrentamiento, un pokemon es elegido ganador y el otro queda fuera de combate saliendo de la simulación.</li>
<li>Debe iniciar con una cantidad significativa de acuerdo al rentimiento, por ejemplo 5000 pokemones, puede ser menos si el rentimiento es un limitante.</li>
 </ul>
</p>

## Motivación
<p align="justify">
 El desarrollo de un sistema multi-agents para simular la interacción de pokemones en un mundo abierto es motivador porque permite modelar de manera realista sistemas complejos donde múltiples entidades autónomas interactúan dinámicamente. Esta metodología fomenta la aplicación práctica de principios de inteligencia artificial, algoritmos y estructuras de datos, y técnicas de simulación, además de proporcionar experiencia en el uso de herramientas de control de versiones y trabajo colaborativo. Al enfrentar desafíos como la gestión de grandes volúmenes de datos y la optimización del rendimiento, los estudiantes desarrollan habilidades clave en computer science y adquieren una comprensión profunda de la dinámica de sistemas distribuidos.
</p>

## Marco Teórico

### La Librería Mesa para Simulaciones Multiagentes
<p align="justify">
Mesa es una librería de Python diseñada específicamente para crear y gestionar simulaciones multiagentes. Es una herramienta poderosa y flexible que facilita la implementación de modelos complejos donde múltiples agentes autónomos interactúan en un entorno definido. A continuación, se destacan las características y beneficios de utilizar Mesa en el desarrollo de simulaciones como la del mundo de pokemones.
</p>

### Características Principales de Mesa

#### Facilidad de Uso y Flexibilidad
<p align="justify">
<ul>
<li>API Intuitiva: Mesa ofrece una API sencilla e intuitiva que permite a los desarrolladores definir agentes, entornos y reglas de interacción de manera clara y concisa.</li>
<li>Flexibilidad: Los desarrolladores pueden personalizar el comportamiento de los agentes y el entorno según los requisitos específicos de su simulación.</li>
</ul>

#### Componentes Clave
<p>
 <ul>
<li>Agentes: Las clases Agent y Model son fundamentales en Mesa. Los agentes son entidades autónomas que interactúan según reglas predefinidas.</li>
<li>Espacio: La clase MultiGrid facilita la creación de entornos espaciales donde los agentes se mueven e interactúan.</li>
<li>Programación del Tiempo: RandomActivation y otros planificadores permiten controlar el orden en que los agentes realizan sus acciones.</li>
</ul>
 </p>
 
#### Visualización Integrada
<p align="justify">
<ul>
<li>CanvasGrid: Permite visualizar la simulación en tiempo real mediante una cuadrícula donde cada agente se representa gráficamente.</li>
<li>Elementos de Texto: TextElement facilita la adición de indicadores y estadísticas en la interfaz de la simulación.</li>
</ul>
</p>

## Desarrollo del Trabajo Final Utilizando Mesa

<p align="justify">
 <ol>
  <li>Configuración del Entorno y Preparación</li>
  <ul>
   <li>Instalación de Mesa: Instalar la librería Mesa junto con otras dependencias necesarias.
   
    pip install mesa
    
   </li>
   <li>Estructura del Proyecto: Organizar el proyecto en directorios y archivos adecuados, incluyendo scripts para los modelos, agentes y visualización.</li>
  </ul>
  <li>Definición de Agentes y Modelos</li>
  <ul>
   <li>Creación de la Clase de Agentes:</li>
   
   ```
class Pokemon(Agent):
    def __init__(self, unique_id, model, tipo, name):
        super().__init__(unique_id, model)
        self.tipo = tipo
        self.name = name
        self.active = True

    def step(self):
        if not self.active:
            return
        if self.model.chasing_mode:
            self.chase()
        else:
            self.move()
        self.fight()
   ```
  <li>Implementación de Métodos de Comportamiento:</li>
  <ul>
   <li>Movimiento: Definir cómo los pokemones se mueven en el mundo.</li>
   <li>Búsqueda de Oponentes: Métodos para localizar otros pokemones.</li>
   <li>Batalla: Implementar la lógica de combate y determinación del ganador.</li>
  </ul>
  </ul>
  <li>Configuración del Entorno (Modelo)</li>
  <ul>
   <li>Creación del Modelo del Mundo:</li>
   
   ```
class PokemonWorld(Model):
    def __init__(self, N):
        self.num_pokemons = N
        self.grid = MultiGrid(50, 50, False)
        self.schedule = RandomActivation(self)
        self.running = True
        self.chasing_mode = False
        self.winning_pokemon = None
        types = list(type_advantages.keys())

        for i in range(self.num_pokemons):
            tipo = random.choice(types)
            name = f"Pokemon_{i+1}"
            pokemon = Pokemon(i, self, tipo, name)
            self.schedule.add(pokemon)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(pokemon, (x, y))
   ```

   <li>Ejecución del Modelo: Implementar el método step para avanzar la simulación.</li>

   ```
def step(self):
    self.schedule.step()
    if self.check_winner():
        self.running = False
   ```
  </ul>
  <li>Visualización y Monitorización</li>
  <ul>
   <li>Definición de Portrayals para los Agentes:</li>

```
def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "r": 0.5}
    if agent.tipo == 'agua':
        portrayal["Color"] = "blue"
    elif agent.tipo == 'fuego':
        portrayal["Color"] = "red"
    elif agent.tipo == 'eléctrico':
        portrayal["Color"] = "yellow"
    elif agent.tipo == 'planta':
        portrayal["Color"] = "green"
    portrayal["Layer"] = 0
    return portrayal
```

   <li>Creación de la Interfaz de Visualización:</li>

```
grid = CanvasGrid(agent_portrayal, 50, 50, 1000, 1000)
chasing_mode_indicator = ChasingModeIndicator()
winning_pokemon_indicator = WinningPokemonIndicator()
server = ModularServer(PokemonWorld, [grid, chasing_mode_indicator, winning_pokemon_indicator], "Pokemon World", {"N": 2500})
server.port = 8521
server.launch()
```

  </ul>
  <li>Pruebas y Ajustes</li>
  <ul>
   <li>Pruebas Iniciales: Ejecutar la simulación para identificar errores y áreas de mejora.</li>
   <li>Ajustes en el Comportamiento de los Agentes: Refinar los métodos de movimiento, combate y búsqueda.</li>
   <li>Optimización de Rendimiento: Ajustar el número de agentes y la configuración del entorno para asegurar      un rendimiento óptimo.</li>
  </ul>
  <li>Documentación y Presentación</li>
  <ul>
   <li>Documentación del Código: Asegurarse de que cada sección del código esté adecuadamente comentada y documentada.</li>
<li>Elaboración del Informe en Markdown: Crear un informe detallado siguiendo las indicaciones del profesor y asegurándose de cumplir con la rúbrica de evaluación.</li>
  </ul>
 </ol>
</p>
