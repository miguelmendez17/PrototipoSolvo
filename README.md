
## Indicaciones generales de lo realizado

-Se utilizó el json proporcionado para poder visualizar los objetos.
-El filtrado de django no se utilizó, ya que aplica para clases y en este prototipo no se utilizó. Aunque 
en un momento se optó por hacer uso de BD y utilizar un ORM, pero para el protipo no lo consideré necesario.
-Se abre el servidor con : python manage.py runserver
-Se corre por defecto en:  http://localhost:8000/


## Requerimientos
-Un cantón esta compuesto por un nombre, un código y una provincia.  Un distrito esta compuesto por un nombre un código y una referencia al cantón de donde se puede obtener el nombre del cantón y la provincia. Se espera encontrar esos campos en el prototipo.

El vistado permite hacer búsquedas por nombre  , tiene una opción para realizar acciones predefinidas como por ejemplo eliminar elementos y una sección de filtros, además solo muestra 20 elementos por pagina ( no tiene que hacer 20 elementos para demostrar la idea) solo el paginado.

Los cantones se filtran por provincia y los distritos se filtran por cantón y provincia, es importante notar existen 81 cantones en Costa Rica.
