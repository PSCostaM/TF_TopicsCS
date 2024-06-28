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

## Técnica propuesta

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
