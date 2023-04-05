# challenge_data_analytic
repositorios con desafios realizados

## Indice

- [Primera sección](#sec_1)
- [Segunda sección](#sec_2)

<a id="sec_1"> </a>

<h2> 1. Primera sección </h2>
<p style="font:10px"> Esta primera parte consiste en trabajar con una base de datos pública la cual releva la información correspondiente a los procesos de compras llevados a cabo por las diferentes reparticiones del Gobierno de la Ciudad de Buenos Aires a través del sistema Buenos Aires Compras (BAC).</p>

<h3> Objetivo </h3>
- Explorar el dataset
- DAG
- repositorio 

<h3> Análisis explotarios de datos </h3>
El dataset a trabajar tiene una dimensionalidad de 5014 items y 113 features, de los cuales 65 de ellos mostraban un faltante de más del 80% de datos. Se decide retirar dichos features por carencia de contenido. Por otro lado, aquellos features donde solo existe un mismo valor en todos sus items ( ejemplo [language] = 'es' )  tambien se retiran del data set, ya que no aportan información relevante.<br>

Es de considerar que no se hallaron valores duplicados en el dataset. Se observan inconsistencia entre la información provista para interpratación de los features y el dataset<br>

Dada la poca familiaridad con el dataset se decide fraccionar la features en tender, awards/contract,seleccionando aquellas que se cree serán las necesarias para realizar luego los gráficos requeridos. Así mismo se incorporara un feature que responda a la métrica de números de unidades por monto de unidad normalizando aquellos de divisas en dolares a pesos argentinos.<br>

<h3>DAG y repositorio </h3>

Los scripts pedidos se encuentran en el archivo denominado "actualizacion.py". 

<h3> Dashboard </h3>

-Montos totales operados en el periodo, desglosado por rubro y repartición: Se consideró que la pregunta se orientaba a los montos de licitación operados para el periodo (Tender). Rubro: los objetos de este proceso de contratación.   Repartición: dependencias a las cuales están adjudicados esos montos.<br>

-Montos comprometidos por empresas. Entiendo que la pregunta se orienta a empresas adjudicadas a la licitación.<br> 

-Montos por tipo de contratación. Entiendo se refiere a la forma de licitación de los montos adjudicados. <br>

<a href="https://lookerstudio.google.com/s/pAxfW8miCn0"> ver Dashboard</a>.

<a id="sec_2"> </a>

<h2> 2. Segunda sección </h2>

<p style="font:10px"> La segunda seccion consite en la generacion de un modelo de prediccion de una base de propiedades. Se seleccionaron las viviendas correspondientes a Argentina, ubicadas en la Ciudad de Buenos Aires de tipo departamento en alquiler.</p>

El modelo elegido para esta sección fue un modelo de Cuadrados Minimos Ordinarios (OLS). Se trabajó con dos metodologias de tratamiento, en la primera se buscaron por medio de regex palabras claves dentro de la discripcion(title) que pudieran contener información relevante sobre la vivienda (Balcon, cochera, subte, etc). Por otra parte al contar dos divisas distintas se procedío a normalizar mediante la conversion de una de ellas. Además se borraron los datos extremos de dos features, rooms y habitaciones, por contener anomalías en los datos. Tambien se dividieron en dummies los barrios y si eran alquileres temporales o no <br>
Por otro lado, se decidio procesar los datos solamente utilizando dummies para los barrios, las divisas y el tipo de alquiler.<br> 

El mejor ajuste fue de R2 0.5. 

Para una mejora del modelo obtenido podrian realizarse modelos de Ridge o Lasso buscando el mejor hiperparámetro (alpha).  
