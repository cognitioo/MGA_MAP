"""
MGA Document Structured Prompt Templates
Full MGA document for investment projects (dynamic pages based on POAI + Development Plan)
"""

from .base_prompts import MGA_CONTEXT

MGA_SUBSIDIOS_SYSTEM = f"""
{MGA_CONTEXT}

Tu tarea es generar contenido estructurado para un documento MGA (Metodología General Ajustada) para proyectos de inversión pública.

**FUENTES DE DATOS PRINCIPALES:**
1. POAI (Plan Operativo Anual de Inversiones) - Excel con datos del proyecto
2. Plan de Desarrollo - PDF con programas, metas e indicadores
3. Datos básicos proporcionados por el usuario

**ESTRUCTURA MGA DINÁMICA:**
El documento sigue el formato oficial del DNP. Las secciones se adaptan según el tipo de proyecto.

**⚠️ REGLAS CRÍTICAS - GENERACIÓN DE CONTENIDO:**

1. **🚨 CÓDIGOS DE PROGRAMA - OBLIGATORIO:**
   - BUSCA la sección "⚠️ CÓDIGOS EXTRAÍDOS DEL POAI" en el contexto.
   - USA EXACTAMENTE el código que aparece ahí (ej: "2302 - Fomento del desarrollo...")
   - Si dice "⚠️ CÓDIGO REAL: 2302 - Nombre", ESCRIBE "2302 - Nombre" en el documento.
   - **NUNCA** uses 4001, 2402, ni NINGÚN otro código que NO esté en la sección de códigos extraídos.
   - Si no hay códigos extraídos, deja el campo VACÍO.

2. **PRIORIDAD: CONTEXTO REAL**
   - Usa los datos del POAI y Plan de Desarrollo siempre que existan.

2. **COMPLETITUD OBLIGATORIA (IMPORTANTE):**
   - ❌ **NUNCA DEJES CAMPOS VACÍOS.** El usuario NO quiere ver espacios en blanco.
   - ✅ **SI FALTA INFORMACIÓN:** ERES UN EXPERTO EN PROYECTOS. **GENERA** un valor realista, coherente y técnico basado en el nombre del proyecto y el municipio.
   - Ejemplo: Si falta el "Programa", BÚSCALO en el POAI. ⚠️ NUNCA uses códigos de ejemplo como "2402" - solo usa los códigos REALES del documento POAI.
   - Ejemplo: Si falta la "Meta", estima una meta razonable (ej: "100% de ejecución").

3. **REALISMO TÉCNICO:**
   - Tus invenciones deben sonar OFICIALES y TÉCNICAS.
   - No uses "Lorem Ipsum" ni texto genérico. Usa terminología propia de proyectos de inversión pública en Colombia.

4. **⚠️ REGLAS ESPECIALES:**
   - **BPIN:** SIEMPRE déjalo VACÍO - se asigna después de aprobación.
   - **CÓDIGOS DE PROGRAMA:** ⚠️ EXTRAE los códigos EXACTOS del documento POAI (formato "XXXX - Nombre"). NUNCA uses "2402", "2302" ni ningún código de ejemplo.
   - **POBLACIÓN:** Usa NÚMEROS REALES (ej: 30104) de la tabla de proyección, NO porcentajes.
   - **NO COPIES** datos de otros proyectos (acueducto, subsidios, etc.) a menos que el proyecto actual sea de ese tipo.

5. **FORMATO:**
   - Responde SOLO en JSON válido.
"""

PROMPT_MGA_SUBSIDIOS_PAGINAS_1_5 = """
Genera contenido para las PRIMERAS 5 PÁGINAS del documento MGA.

**INSTRUCCIONES CLAVES - NO DEJES NADA VACÍO:**

DATOS BÁSICOS PROPORCIONADOS:
Municipio: {municipio} | Departamento: {departamento}
Entidad: {entidad} | BPIN: {bpin}
Proyecto: "{nombre_proyecto}"
Valor: ${valor_total} COP | Duración: {duracion} días
Responsable: {responsable} ({cargo})
Identificador: {identificador}
Fecha creación: {fecha_creacion}

PLANES DE DESARROLLO (Referencia):
Plan Nacional: {plan_nacional}
Plan Departamental: {plan_departamental}
Plan Municipal: {plan_municipal}

CONTEXTO ADICIONAL:
{context_dump}

**TU TAREA:**
1. Completa TODOS los campos. Si el "Plan de Desarrollo" no especifica un programa exacto, ASIGNA uno que sea coherente con "{nombre_proyecto}".
2. Para "Problema Central" y "Causas/Efectos": REDACTA el árbol de problemas basado en el nombre del proyecto.
3. **IDENTIFICADOR**: Si el dato "Identificador" entregado está vacío, GENERA uno con formato "2026-xxxxx".
4. Para "Participantes": Genera actores típicos (Alcaldía, Comunidad, Contratista).

**REGLA DE ORO:** Más vale un dato estimado técnicamente correcto que un campo vacío.

RESPONDE CON JSON VÁLIDO:

{{
    "pagina_1_datos_basicos": {{
        "titulo_documento": "{nombre_proyecto}",
        "nombre": "{nombre_proyecto}",
        "tipologia": "A - PIIP - Bienes y Servicios",
        "codigo_bpin": "",
        "sector": "Extrae del POAI o infiere del nombre del proyecto",
        "es_proyecto_tipo": "No",
        "fecha_creacion": "{fecha_creacion}",
        "identificador": "{identificador}",
        "formulador_ciudadano": "{responsable} ({cargo})",
        "formulador_oficial": "{responsable} ({cargo})"
    }},

    "pagina_2_plan_desarrollo": {{
        "plan_nacional": {{
            "nombre": "{plan_nacional}",
            "programa": "🚨 COPIA el código EXACTO de la sección '⚠️ CÓDIGOS EXTRAÍDOS DEL POAI'. NO inventes códigos.",
            "transformacion": "Desarrollo Regional / Otro según proyecto",
            "pilar": "Infraestructura / Inclusión / Otro según proyecto",
            "catalizador": "Inversión en infraestructura / Otro según proyecto",
            "componente": "Componente relevante al proyecto"
        }},
        "plan_departamental": {{
            "nombre": "{plan_departamental}",
            "estrategia": "Estrategia del plan departamental",
            "programa": "🚨 COPIA el código EXACTO de la sección '⚠️ CÓDIGOS EXTRAÍDOS DEL POAI'. NO inventes códigos."
        }},
        "plan_municipal": {{
            "nombre": "{plan_municipal}",
            "estrategia": "Estrategia del plan municipal",
            "programa": "🚨 COPIA el código EXACTO de la sección '⚠️ CÓDIGOS EXTRAÍDOS DEL POAI'. NO inventes códigos."
        }},
        "instrumentos_grupos_etnicos": "No aplica"
    }},

    "pagina_3_problematica": {{
        "problema_central": "",
        "descripcion_situacion": "",
        "magnitud_problema": ""
    }},

    "pagina_4_causas_efectos": {{
        "causas_directas": [
            {{"numero": "1", "causa": ""}}
        ],
        "causas_indirectas": [
            {{"numero": "1.1", "causa": ""}}
        ],
        "efectos_directos": [
            {{"numero": "1", "efecto": ""}}
        ],
        "efectos_indirectos": [
            {{"numero": "1.1", "efecto": ""}}
        ]
    }},

    "pagina_5_participantes": {{
        "participantes": [
            {{
                "actor": "Municipal",
                "entidad": "Alcaldía de {municipio} - {departamento}",
                "posicion": "Cooperante",
                "intereses": "{nombre_proyecto}",
                "contribucion": "Ejecutar el proyecto"
            }}
        ],
        "analisis_participantes": ""
    }}
}}
"""


PROMPT_MGA_SUBSIDIOS_PAGINAS_6_11 = """

DATOS DEL PROYECTO:
Municipio: {municipio} | Departamento: {departamento}
Proyecto: "{nombre_proyecto}"
Valor: ${valor_total} COP
Contexto POAI/Plan Desarrollo:
{context_dump}

**INSTRUCCIONES DE GENERACIÓN (IMPORTANTE):**
1. ESTE DOCUMENTO ES PARA UN PROYECTO DE: "{nombre_proyecto}"
2. NO uses datos de ejemplos anteriores (acueducto, suicidio, etc.) a menos que el proyecto sea de eso.
3. GENERA estimaciones poblacionales realistas basadas en el municipio de {municipio}.
4. REDACTA objetivos (General y Específicos) coherentes con el título del proyecto.
5. NO dejes campos vacíos. Si no tienes el dato exacto, ESTIMÁLO o REDÁCTALO basado en sentido común técnico para este tipo de proyecto.

RESPONDE CON JSON VÁLIDO:

{{
    "pagina_6_poblacion": {{
        "poblacion_afectada": {{
            "tipo": "Personas",
            "numero": 30104,
            "fuente": "DANE / Sisbén municipal",
            "localizacion": {{
                "region": "Caribe",
                "departamento": "{departamento}",
                "municipio": "{municipio}",
                "tipo_agrupacion": "Urbana",
                "agrupacion": "{municipio}"
            }}
        }},
        "poblacion_objetivo": {{
            "tipo": "Personas",
            "numero": 15000,
            "fuente": "DANE / Registros locales",
            "localizacion": {{
                "region": "Caribe",
                "departamento": "{departamento}",
                "municipio": "{municipio}",
                "tipo_agrupacion": "Urbana",
                "agrupacion": "{municipio}"
            }}
        }}
    }},

    "pagina_7_objetivos": {{
        "problema_central": "Redacta el problema central que resuelve este proyecto: {nombre_proyecto}",
        "objetivo_general": "Redacta el objetivo en infinitivo (Mejorar/Construir/Optimizar) para: {nombre_proyecto}",
        "indicadores": [
            {{
                "nombre": "Redacta un indicador principal de resultado",
                "medido": "Número/Porcentaje",
                "meta": "Define una meta numérica acorde al valor del proyecto",
                "tipo_fuente": "Documento oficial",
                "fuente_verificacion": "Secretaría de Planeación Municipal"
            }}
        ],
        "relacion_causas_objetivos": [
            {{
                "causa": "Causa directa 1: (Relacionada con el problema)",
                "objetivo": "Objetivo específico 1: (Soluciona la causa directa)"
            }},
            {{
                "causa": "Causa indirecta 1.1: (Detalle del problema)",
                "objetivo": "Acción concreta para abordar la causa indirecta"
            }}
        ],
        "alternativas": [
            {{
                "nombre": "Alternativa seleccionada: Ejecución del proyecto de inversión {nombre_proyecto}",
                "evaluacion": "Si",
                "estado": "Completo"
            }}
        ],
        "evaluaciones": {{
            "rentabilidad": "Si",
            "costo_eficiencia": "Si",
            "multicriterio": "No"
        }}
    }},

    "pagina_8_9_10_11_estudio_necesidades": {{
        "servicio_principal": {{
            "bien_servicio": "Infraestructura vial mejorada",
            "medido": "Número",
            "descripcion": "Mejoramiento de la infraestructura vial del municipio de {municipio} que permitirá mejorar la conectividad y acceso de la población a los servicios básicos.",
            "descripcion_demanda": "La población del municipio de {municipio} requiere vías en buen estado para acceder a servicios de salud, educación y comercio. Actualmente X kilómetros de vías se encuentran en mal estado.",
            "descripcion_oferta": "El municipio cuenta actualmente con una red vial limitada que no cubre las necesidades de la población. La cobertura actual es del XX%.",
            "tabla_oferta_demanda": [
                {{"ano": "2022", "oferta": "240.00", "demanda": "240.00", "deficit": "0.00"}},
                {{"ano": "2023", "oferta": "240.00", "demanda": "240.00", "deficit": "0.00"}},
                {{"ano": "2024", "oferta": "240.00", "demanda": "240.00", "deficit": "0.00"}},
                {{"ano": "2025", "oferta": "0.00", "demanda": "240.00", "deficit": "-240.00"}},
                {{"ano": "2026", "oferta": "0.00", "demanda": "240.00", "deficit": "-240.00"}},
                {{"ano": "2027", "oferta": "0.00", "demanda": "240.00", "deficit": "-240.00"}}
            ]
        }}
    }}
}}
"""

PROMPT_MGA_SUBSIDIOS_PAGINAS_12_16 = """

DATOS DEL PROYECTO:
Proyecto: "{nombre_proyecto}"
Valor Total: ${valor_total} COP
Contexto:
{context_dump}

**INSTRUCCIONES:**
1. NO uses datos de ejemplos (acueducto) a menos que sea relevante.
2. Analiza la viabilidad técnica, legal y ambiental para: "{nombre_proyecto}".
3. Estima una cadena de valor lógica (Insumos -> Actividades -> Productos -> Resultados).
4. Genera un flujo de caja simple basado en el Valor Total ${valor_total}.

⚠️ **REGLA CRÍTICA DE COSTOS - MUY IMPORTANTE:**
La cadena de valor DEBE cumplir con esta VALIDACIÓN MATEMÁTICA:
- Suma de ACTIVIDADES de un producto = Costo del PRODUCTO
- Suma de PRODUCTOS de un objetivo = Costo del OBJETIVO
- Suma de OBJETIVOS = Valor Total: ${valor_total}

EJEMPLO DE CÁLCULO CORRECTO:
Si valor_total = 100,000,000:
- Objetivo 1: 100,000,000
  - Producto 1.1: 60,000,000
    - Actividad 1.1.1: 30,000,000
    - Actividad 1.1.2: 30,000,000
  - Producto 1.2: 40,000,000
    - Actividad 1.2.1: 20,000,000
    - Actividad 1.2.2: 20,000,000

RESPONDE CON JSON VÁLIDO:

{{
    "pagina_12_analisis_tecnico": {{
        "alternativa_seleccionada": "Ejecución del proyecto: {nombre_proyecto}",
        "analisis_tecnico": "Genera análisis técnico ESPECÍFICO para {nombre_proyecto}. NO copies de otros proyectos. Incluye: ubicación, tecnología, especificaciones técnicas reales.",
        "analisis_ambiental": "El proyecto cumple con la normativa ambiental vigente y no genera impactos negativos significativos.",
        "analisis_legal": "El proyecto se enmarca en las competencias del municipio y cumple con la normativa del sector.",
        "analisis_riesgos": "Se han identificado y mitigado los riesgos previsibles.",
        "localizacion": {{
            "region": "Caribe",
            "departamento": "{departamento}",
            "municipio": "{municipio}",
            "tipo_agrupacion": "Urbana",
            "latitud": "",
            "longitud": ""
        }}
    }},

    "pagina_13_cadena_valor": {{
        "costo_total": "{valor_total}",
        "objetivo_general": "Cumplir con el objetivo de {nombre_proyecto}",
        "objetivos": [
            {{
                "numero": "1",
                "descripcion": "Objetivo específico derivado de {nombre_proyecto}",
                "costo": "13.000.000,00",
                "productos": [
                    {{
                        "codigo": "1.3",
                        "nombre": "Servicio de acompañamiento productivo y empresarial",
                        "complemento": "",
                        "medido": "Número de unidades productivas",
                        "cantidad": "10,0000",
                        "costo": "3.000.000,00",
                        "etapa": "Inversión",
                        "localizacion": "{municipio}",
                        "personas": "50",
                        "acumulativo": "No Acumulativo",
                        "poblacion_beneficiaria": "50",
                        "actividades": [
                            {{
                                "codigo": "1.3.1",
                                "nombre": "Asistencia técnica para la identificación del estado de los procesos productivos y definición de planes de mejoras - Fase 1",
                                "costo": "1.500.000,00",
                                "etapa": "Inversión"
                            }},
                            {{
                                "codigo": "1.3.2",
                                "nombre": "Asistencia técnica para la identificación del estado de los procesos productivos y definición de planes de mejoras - Fase 2",
                                "costo": "1.500.000,00",
                                "etapa": "Inversión"
                            }}
                        ]
                    }},
                    {{
                        "codigo": "1.4",
                        "nombre": "Servicio de fomento a la asociatividad",
                        "complemento": "",
                        "medido": "Número de productores",
                        "cantidad": "10,0000",
                        "costo": "10.000.000,00",
                        "etapa": "Inversión",
                        "localizacion": "{municipio}",
                        "personas": "50",
                        "acumulativo": "No Acumulativo",
                        "poblacion_beneficiaria": "50",
                        "actividades": [
                            {{
                                "codigo": "1.4.1",
                                "nombre": "Apoyar a las asociaciones campesinas, pesqueras, mujeres rurales y víctimas del conflicto armado - Fase 1",
                                "costo": "5.000.000,00",
                                "etapa": "Inversión"
                            }},
                            {{
                                "codigo": "1.4.2",
                                "nombre": "Apoyar a las asociaciones campesinas, pesqueras, mujeres rurales y víctimas del conflicto armado - Fase 2",
                                "costo": "5.000.000,00",
                                "etapa": "Inversión"
                            }}
                        ]
                    }}
                ]
            }},
            {{
                "numero": "2",
                "descripcion": "Promocionar el acceso a la oferta del Estado al sector productivo",
                "costo": "58.000.000,00",
                "productos": [
                    {{
                        "codigo": "2.1",
                        "nombre": "Servicio de apoyo financiero para proyectos productivos",
                        "complemento": "",
                        "medido": "Número de proyectos",
                        "cantidad": "4,0000",
                        "costo": "15.000.000,00",
                        "etapa": "Inversión",
                        "localizacion": "{municipio}",
                        "personas": "40",
                        "acumulativo": "No Acumulativo",
                        "poblacion_beneficiaria": "40",
                        "actividades": [
                            {{
                                "codigo": "2.1.1",
                                "nombre": "Implementar proyectos productivos de tipo permanente y transitorio para fortalecer la economía rural",
                                "costo": "4.500.000,00",
                                "etapa": "Inversión"
                            }},
                            {{
                                "codigo": "2.1.2",
                                "nombre": "Apoyo a proyectos productivos de jóvenes, mujeres, población víctimas y LGTBIQA+ emprendedores",
                                "costo": "4.500.000,00",
                                "etapa": "Inversión"
                            }},
                            {{
                                "codigo": "2.1.3",
                                "nombre": "Apoyo a pequeños o medianos agricultores en la siembra de nuevos cultivos permanentes y/o cultivos transitorios",
                                "costo": "6.000.000,00",
                                "etapa": "Inversión"
                            }}
                        ]
                    }},
                    {{
                        "codigo": "2.2",
                        "nombre": "Servicio de apoyo para el acceso a maquinaria y equipos",
                        "complemento": "",
                        "medido": "Número de productores",
                        "cantidad": "20,0000",
                        "costo": "8.000.000,00",
                        "etapa": "Inversión",
                        "localizacion": "{municipio}",
                        "personas": "100",
                        "acumulativo": "No Acumulativo",
                        "poblacion_beneficiaria": "100",
                        "actividades": [
                            {{
                                "codigo": "2.2.1",
                                "nombre": "Adquisición de maquinaria verde y agrícola para entrega a las asociaciones rurales, campesina, pesqueras, mujeres y víctimas de conflicto armado para el fortalecimiento de sus proyectos productivos en el municipio de {municipio}",
                                "costo": "6.000.000,00",
                                "etapa": "Inversión"
                            }},
                            {{
                                "codigo": "2.2.2",
                                "nombre": "Asistencia técnica en los procesos de mecanización y producción de la maquinaria dotada",
                                "costo": "2.000.000,00",
                                "etapa": "Inversión"
                            }}
                        ]
                    }},
                    {{
                        "codigo": "2.3",
                        "nombre": "Servicio de apoyo a la comercialización",
                        "complemento": "",
                        "medido": "Número de organizaciones",
                        "cantidad": "10,0000",
                        "costo": "35.000.000,00",
                        "etapa": "Inversión",
                        "localizacion": "{municipio}",
                        "personas": "100",
                        "acumulativo": "No Acumulativo",
                        "poblacion_beneficiaria": "100",
                        "actividades": [
                            {{
                                "codigo": "2.3.1",
                                "nombre": "Apoyo logístico para la realización de los mercados campesinos",
                                "costo": "25.000.000,00",
                                "etapa": "Inversión"
                            }},
                            {{
                                "codigo": "2.3.2",
                                "nombre": "Apoyo logístico para entidades gubernamentales para las alianzas de compras públicas locales, entre los productores y compradores del municipio",
                                "costo": "10.000.000,00",
                                "etapa": "Inversión"
                            }}
                        ]
                    }}
                ]
            }}
        ]
    }},

    "pagina_14_riesgos": {{
        "riesgos": [
            {{
                "nivel": "1-Propósito (Objetivo general)",
                "tipo": "Administrativos",
                "descripcion": "El contratista no cumple de forma adecuada con las actividades generales y específicas establecidas en el contrato.",
                "probabilidad": "2. Improbable",
                "impacto": "4. Mayor",
                "efectos": "La no realización de procesos administrativos y técnicos para el fortalecimiento de la Secretaría de Desarrollo Económico y Medio Ambiente.",
                "mitigacion": "Contratar personal con experiencia en la realización de este tipo de proyectos. Realizar supervisión permanente sobre el avance en las metas según el Plan de Desarrollo Municipal."
            }},
            {{
                "nivel": "2-Componente (Productos)",
                "tipo": "Administrativos",
                "descripcion": "Incumplimiento de las obligaciones contractuales en los términos acordados.",
                "probabilidad": "3. Moderado",
                "impacto": "3. Moderado",
                "efectos": "Incumplimiento en los objetivos del proyecto.",
                "mitigacion": "Seguimiento en el desarrollo de los diferentes programas establecidos en el Plan de Desarrollo Municipal."
            }},
            {{
                "nivel": "2-Componente (Productos)",
                "tipo": "Administrativos",
                "descripcion": "Las acciones realizadas no cumplieron con los procedimientos establecidos.",
                "probabilidad": "3. Moderado",
                "impacto": "4. Mayor",
                "efectos": "La probabilidad de no implementación de la totalidad de las actividades programadas.",
                "mitigacion": "Verificar que las acciones desarrolladas estén supervisadas."
            }},
            {{
                "nivel": "3-Actividad y/o Entregable",
                "tipo": "Administrativos",
                "descripcion": "Actividad/Entregable: Contratar el personal técnico operativo de apoyo a la gestión de la Secretaría de Desarrollo Económico y Medio Ambiente municipal.\\n\\nRiesgo: Demora en los procesos de contratación.",
                "probabilidad": "3. Moderado",
                "impacto": "3. Moderado",
                "efectos": "Atraso en los procesos de ejecución",
                "mitigacion": "Programar calendario contractual según fechas programadas."
            }}
        ]
    }},

    "pagina_15_ingresos_beneficios": {{
        "ingresos": [],
        "beneficios": [
            {{
                "nombre": "Beneficio Social: Mejora en calidad de vida",
                "tipo": "Social",
                "valor": "No cuantificable monetariamente",
                "descripcion": "Impacto positivo en la comunidad beneficiaria de {municipio}"
            }}
        ]
    }},

    "pagina_16_prestamos": {{
        "prestamos": []
    }}
}}
"""

PROMPT_MGA_SUBSIDIOS_PAGINAS_17_21 = """
Genera contenido para las PÁGINAS 17-21 del documento MGA.

DATOS DEL PROYECTO:
Proyecto: "{nombre_proyecto}"
Valor Total: ${valor_total} COP
Contexto:
{context_dump}

INSTRUCCIONES:
1. Genera riesgos adicionales coherentes con el proyecto.
2. Para beneficios, si es social, destaca la mejora en calidad de vida.
3. El flujo económico debe ser consiste con el valor total.

RESPONDE CON JSON VÁLIDO:

{{
    "pagina_17_riesgos_continuacion": {{
        "riesgos_adicionales": [
            {{
                "nivel": "3-Actividad y/o Entregable",
                "tipo": "Financieros",
                "descripcion_actividad": "Ejecución presupuestal de {nombre_proyecto}",
                "descripcion_riesgo": "Insuficiencia de recursos o flujo de caja.",
                "probabilidad": "1. Raro",
                "impacto": "5. Catastrófico",
                "efectos": "Suspensión de actividades",
                "mitigacion": "Asegurar disponibilidad presupuestal previa."
            }}
        ]
    }},

    "pagina_18_19_ingresos_beneficios": {{
        "beneficios": [
            {{
                "titulo": "Aumento de ingresos de los productores por competencias adquiridas",
                "tipo": "Beneficios",
                "medido": "Número",
                "bien_producido": "FC inversión agropecuaria",
                "razon_precio_cuenta": "0.91",
                "descripcion_cantidad": "Corresponde a los productores apoyados",
                "descripcion_valor_unitario": "Corresponde al valor promedio de aumento de la producción por apoyos recibidos.",
                "tabla_periodos": [
                    {{"periodo": "1", "cantidad": "124.00", "valor_unitario": "$2.800.000,00", "valor_total": "$347.200.000,00"}}
                ]
            }},
            {{
                "titulo": "Costos evitados por educación no formal y capacitaciones",
                "tipo": "Beneficios",
                "medido": "Número",
                "bien_producido": "Otros",
                "razon_precio_cuenta": "0.80",
                "descripcion_cantidad": "Corresponde a los productores apoyados",
                "descripcion_valor_unitario": "Corresponde al valor promedio de educación no formal y capacitaciones del sector productivo agropecuario.",
                "tabla_periodos": [
                    {{"periodo": "1", "cantidad": "124.00", "valor_unitario": "$250.000,00", "valor_total": "$31.000.000,00"}}
                ]
            }}
        ],
        "tabla_totales": [
            {{"periodo": "1", "total_beneficios": "$378.200.000,00", "total": "$378.200.000,00"}}
        ]
    }},

    "pagina_20_flujo_economico": {{
        "alternativa": "Alternativa 1",
        "flujo": [
            {{"p": "0", "beneficios": "$0,0", "creditos": "$0,0", "costos_preinversion": "$0,0", "costos_inversion": "$296.529.217,7", "costos_operacion": "$0,0", "amortizacion": "$0,0", "intereses": "$0,0", "valor_salvamento": "$0,0", "flujo_neto": "-$296.529.217,7"}},
            {{"p": "1", "beneficios": "$340.752.000,0", "creditos": "$0,0", "costos_preinversion": "$0,0", "costos_inversion": "$0,0", "costos_operacion": "$0,0", "amortizacion": "$0,0", "intereses": "$0,0", "valor_salvamento": "$0,0", "flujo_neto": "$340.752.000,0"}}
        ]
    }},

    "pagina_21_indicadores_decision": {{
        "alternativa_descripcion": "Fortalecimiento integral del sector productivo de {municipio} a través de apoyo financiero, asistencia técnica y promoción comercial",
        "evaluacion_economica": {{
            "vpn": "$16.087.296,08",
            "tir": "14,91 %",
            "rcb": "$1,05",
            "costo_beneficiario": "$125.754,55",
            "valor_presente_costos": "$296.529.217,68",
            "cae": "$9.145.127,50"
        }},
        "costo_capacidad": {{
            "productos": [
                {{"nombre": "Servicio de asistencia técnica agropecuaria dirigida a pequeños productores (Producto principal del proyecto)", "costo": "$2.359.092,18"}},
                {{"nombre": "Servicio de apoyo financiero para proyectos productivos", "costo": "$3.000.000,00"}},
                {{"nombre": "Servicio de apoyo para el acceso a maquinaria y equipos", "costo": "$331.000,00"}},
                {{"nombre": "Servicio de apoyo para el fomento organizativo de la Agricultura Campesina, Familiar y Comunitaria", "costo": "$300.000,00"}},
                {{"nombre": "Servicio de acompañamiento productivo y empresarial", "costo": "$300.000,00"}},
                {{"nombre": "Servicio de apoyo a la comercialización", "costo": "$2.800.000,00"}},
                {{"nombre": "Servicio de fomento a la asociatividad", "costo": "$800.000,00"}}
            ]
        }},
        "decision": {{
            "alternativa": "Ejecución de {nombre_proyecto} por su alta rentabilidad social"
        }},
        "alcance": "Alcance definido para {nombre_proyecto} en {municipio}."
    }}
}}
"""

PROMPT_MGA_SUBSIDIOS_PAGINAS_22_24 = """
Genera contenido para las PÁGINAS FINALES del documento MGA (Indicadores).

DATOS DEL PROYECTO:
Municipio: {municipio} | Departamento: {departamento}
Proyecto: "{nombre_proyecto}"
Valor Total: ${valor_total} COP
Contexto:
{context_dump}

**INSTRUCCIONES CLAVE - INDICADORES Y REGIONALIZACIÓN DINÁMICA:**
1.  **GENERACIÓN DINÁMICA**: Debes generar UN (1) conjunto de datos POR CADA PRODUCTO definido en la cadena de valor.
    *   **Indicadores**: Genera un objeto en "indicadores_producto" por cada producto.
    *   **Regionalización**: Genera un objeto en "regionalizacion_productos" por cada producto.
    *   **Focalización**: Genera una lista en "focalizacion" con las políticas transversales aplicables.
    *   **IMPORTANTE**: Si el proyecto tiene 7 productos, debe haber 7 indicadores y 7 tablas de regionalización.
2.  **CONSISTENCIA**: Usa los MISMOS nombres de productos que en la Cadena de Valor.
3.  **FOCALIZACIÓN**: Asigna presupuesto a políticas como "Construcción de Paz" o similares si aplica.

RESPONDE CON JSON VÁLIDO:

{{
    "indicadores_producto": [
        {{
            "objetivo": {{
                "numero": "1",
                "descripcion": "Objetivo específico asociado"
            }},
            "producto": {{
                "codigo": "1.X",
                "nombre": "Nombre del producto",
                "complemento": "Descripción complementaria"
            }},
            "indicador": {{
                "codigo": "1.X.1",
                "nombre": "Nombre del indicador",
                "medido": "Unidad de medida",
                "meta_total": "Meta numérica total",
                "formula": "Fórmula",
                "es_acumulativo": "Sí/No",
                "es_principal": "Sí",
                "tipo_fuente": "Informe",
                "fuente_verificacion": "Secretaría"
            }},
            "programacion_indicadores": [
                {{"periodo": "1", "meta": "Valor"}}
            ]
        }}
    ],
    "regionalizacion_productos": [
        {{
            "producto": "Nombre del producto (Debe coincidir con la lista de productos)",
            "ubicacion": {{
                "region": "Caribe",
                "departamento": "{departamento}",
                "municipio": "{municipio}",
                "tipo_agrupacion": "Municipio",
                "agrupacion": "{municipio}"
            }},
            "tabla_costos": [
                 {{
                    "periodo": "0", 
                    "costo_total": "Valor", 
                    "costo_regionalizado": "Valor", 
                    "meta_total": "Valor", 
                    "meta_regionalizada": "Valor", 
                    "beneficiarios": "Número"
                }}
            ]
        }}
    ],
    "focalizacion": [
        {{
            "politica": "Nombre Política (ej: Construcción de Paz)",
            "categoria": "Nombre Categoría",
            "subcategoria": "Nombre Subcategoría (o vacío)",
            "valor": "Valor Monetario"
        }}
    ]
}}
"""
