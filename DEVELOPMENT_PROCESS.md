# Proceso de Desarrollo y Lecciones Aprendidas

Este documento describe el proceso de desarrollo seguido para implementar la API de notas, incluyendo los desafíos encontrados y las decisiones técnicas tomadas.

## 📝 Proceso de Implementación

### 1. Investigación Inicial
Busqué cómo iniciar y configurar un proyecto usando **Serverless Framework**, evaluando las mejores prácticas y opciones disponibles.

### 2. Configuración de AWS
- **Instalé AWS CLI** y me autentifiqué en la plataforma
- Tuve que **crear un Retrieve access key** en la consola de AWS para establecer las credenciales necesarias

### 3. Setup de Serverless Framework
- **Instalé Serverless Framework** globalmente
- Me creé una cuenta en la plataforma Serverless
- **Vinculé la cuenta con AWS** mediante AWS IAM Role para automatizar los permisos

### 4. Selección de Template
Inicié el proyecto usando el template **"AWS / Python / HTTP API"** por las siguientes razones:
- **Simplicidad**: Para el requerimiento del ejercicio, era más simple que usar "FastAPI with DynamoDB"
- **Menor configuración**: Nos ahorramos configuraciones innecesarias
- **Enfoque minimalista**: No era necesario crear una App adicional para vincular al proyecto

### 5. Configuración de Dependencias
Utilicé la siguiente secuencia de comandos para optimizar la gestión de dependencias:

```bash
npm init -y
npm install --save-dev serverless-python-requirements
```

**Ventaja**: Esto evita tener que instalar manualmente las dependencias de Python, ya que el plugin se encarga automáticamente.

### 6. Desarrollo de Endpoints
Creé los endpoints con su lógica en `handler.py`, implementando únicamente:
- **Códigos de respuesta mínimos y necesarios**
- **Funcionalidad core** sin sobrecarga de features innecesarias
- **Manejo básico de errores**

### 7. Configuración de Infraestructura
Durante la configuración del `serverless.yml` enfrenté algunos desafíos:

#### Problema con DynamoDB
- **Eliminé la tabla existente "notas"** que estaba vacía
- **Razón**: Serverless se encarga de la creación de forma más simple y automatizada
- **Beneficio**: Evita conflictos de configuración manual

#### Problema con IAM Roles
- **Configuré el IAM role** que había sido problemático durante el live coding
- **Resultado**: Configuración más limpia y mantenible

### 8. Testing y Deployment
- Hice **deploy inicial** usando `serverless deploy`
- **Probé los endpoints** para verificar funcionalidad
- **Iteré sobre errores** hasta obtener la versión final estable

### 9. Proceso de Corrección
Corregí errores de forma iterativa hasta tener la **versión final funcional**, aplicando:
- **Testing manual de endpoints**
- **Ajustes de configuración**

## 🎯 Lecciones Aprendidas

### ✅ Decisiones Acertadas
- **Usar Serverless Framework**: Simplificó significativamente la configuración de infraestructura
- **Template minimalista**: Evitó complejidad innecesaria para el scope del proyecto
- **Automatización de dependencias**: El plugin de Python requirements ahorró tiempo y errores

### ⚠️ Desafíos Superados
- **Gestión manual vs automatizada**: Aprendí que Serverless maneja mejor la infraestructura que la configuración manual
- **IAM complexity**: La configuración manual de permisos es más propensa a errores
- **DynamoDB conflicts**: Las tablas preexistentes pueden causar problemas en deployment, no es eficiente pedir como paso de deploy que se cree la tabla manualmente.
