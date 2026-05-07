# Convenciones de metadatos

Cada documento Markdown debe comenzar con frontmatter YAML.

```yaml
---
id: "ucasal_comp_001_abogacia"
titulo: "Abogacía"
institucion: "Universidad Católica de Salta - UCASAL"
facultad_o_unidad: "Facultad de Ciencias Jurídicas"
carrera: "Abogacía"
tipo_documento: "competencias_especificas_y_alcances_para_RAG"
resolucion: "Resolución N° 290/2025"
fecha_documento: "2025-08-12"
modalidad: "Presencial y Distancia"
estado: "vigente"
prioridad_rag: alta
requiere_validacion_humana: true
---
```

## Campos obligatorios

- `id`
- `titulo`
- `facultad_o_unidad`
- `carrera`
- `tipo_documento`
- `estado`
- `requiere_validacion_humana`

## Uso en RAG

El indexador debe conservar estos metadatos junto a cada chunk para que el agente pueda recuperar fuentes por carrera, unidad académica, resolución, modalidad y estado de vigencia.
