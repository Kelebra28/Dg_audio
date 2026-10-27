# Regla: Priorizar Herramientas de Edición sobre Comandos y Scripts de Terminal

## Principio General
En este proyecto, queda estrictamente indicado **no ejecutar scripts (Python, Bash, Node) ni comandos en la terminal** para leer, buscar, analizar o editar archivos. Todas las tareas de inspección, extracción y edición deben realizarse exclusivamente a través de las herramientas nativas del editor.

## Directrices Obligatorias

1. **Prohibido el uso de scripts inline para manipulación de código**:
   * No usar `run_command` con comandos de una línea en Python (`python3 -c "..."`), scripts en bash ni pipelines complejos para inspeccionar archivos.
   
2. **Uso estricto de herramientas nativas del editor**:
   * Para leer o inspeccionar código: usar `view_file` con rangos de líneas (`StartLine`, `EndLine`).
   * Para buscar texto o selectores: usar `grep_search`.
   * Para listar directorios: usar `list_dir`.
   * Para crear nuevos archivos: usar `write_to_file`.
   * Para modificar archivos existentes: usar `replace_file_content` o `multi_replace_file_content`.

3. **Excepción única para `run_command`**:
   * Solo se permite invocar `run_command` para procesos de ejecución indispensables que no pueden realizarse en el editor, como levantar el servidor de desarrollo local para pruebas de visualización (`python3 -m http.server`), previa autorización del usuario.
