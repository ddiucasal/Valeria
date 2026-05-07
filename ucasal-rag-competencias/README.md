# UCASAL RAG Competencias

Repositorio de conocimiento preparado para alimentar una base RAG local orientada a la transformación de programas formulados por objetivos hacia programas formulados por competencias.

## Propósito

Este repositorio funciona como **fuente controlada de conocimiento**. No reemplaza la validación académica humana. Su función es ordenar, versionar y facilitar la indexación de documentos institucionales relacionados con:

- Modelo Educativo UCASAL.
- Competencias transversales.
- Competencias específicas por carrera.
- Matrices de tributación.
- Criterios de transformación curricular.
- Prompts y reglas para agentes de IA.

## Estructura

```text
00_documentos_control/             Normas de uso, gobernanza y trazabilidad.
01_modelo_ucasal/                  Referencias institucionales base.
02_matrices_tributacion/           Documentos por facultad, carrera y resolución.
03_guias_transformacion_curricular/ Guías pedagógicas para transformar objetivos en competencias.
04_prompts_sistema/                Prompts para el agente IA y validadores.
05_ejemplos/                       Ejemplos de entrada y salida.
06_scripts_ingesta/                Script base para indexación local.
data/raw/                          Archivo original consolidado.
data/index/                        Catálogo y JSONL para ingesta.
```

## Flujo recomendado

```text
GitHub privado
   ↓
Documentos con metadatos
   ↓
Script de ingesta
   ↓
Base vectorial local
   ↓
Software con API de ChatGPT
   ↓
Transformación curricular asistida
   ↓
Validación docente / DDDI
```

## Estado de esta versión

- Fecha de generación: 2026-05-07
- Fuente original: `data/raw/matriz_competencias_ucasal_RAG_ULTIMA_VERSION_2026_MAYO.txt`
- Documentos segmentados automáticamente: 61
- Estado general: `vigente_a_validar`

## Recomendación

Usar la rama `main` solo para documentos validados. Usar ramas como `develop` o `revision-academica` para documentos en proceso.
