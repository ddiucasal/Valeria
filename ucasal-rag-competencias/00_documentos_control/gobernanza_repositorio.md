# Gobernanza del repositorio

## Regla principal

El repositorio debe funcionar como fuente controlada de conocimiento para alimentar una base RAG local. No debe utilizarse como simple depósito de archivos.

## Estados sugeridos

- `vigente`: documento validado y autorizado para uso RAG.
- `vigente_a_validar`: documento cargado, pendiente de revisión formal.
- `borrador`: documento en elaboración.
- `historico`: documento reemplazado o sin vigencia actual.
- `observado`: documento con inconsistencias detectadas.

## Ramas sugeridas

- `main`: documentos vigentes y validados.
- `develop`: documentos en preparación.
- `revision-academica`: documentos listos para evaluación.
- `archive`: documentos históricos.

## Validación mínima antes de pasar a main

1. Verificar resolución y fecha.
2. Verificar carrera, plan y modalidad.
3. Verificar que las competencias sean oficiales o estén claramente marcadas como provisorias.
4. Verificar que el documento tenga metadatos YAML.
5. Verificar que no haya duplicados contradictorios.
