# DFx5 Technical Interview - API de Notas - Serverless

API RESTful para gestión de notas construida con AWS Lambda, API Gateway y DynamoDB usando Serverless Framework.

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener una cuenta de AWS configurada.

## 🛠️ Instalación de Dependencias

### 1. Instalar Node.js
Descarga e instala Node.js desde https://nodejs.org/ (versión LTS recomendada)

### 2. Instalar Serverless Framework
```bash
npm install -g serverless
```

### 3. Configurar AWS CLI
```bash
# Instalar AWS CLI
npm install -g aws-cli

# Configurar credenciales AWS
aws configure
```
Ingresa tus credenciales de AWS cuando se te solicite.

### 4. Instalar dependencias del proyecto
```bash
# Clonar el repositorio
git clone https://github.com/FrancoMuzzio/DFX5-Tech-Interview.git

# Ir al directorio del proyecto
cd DFX5-Tech-Interview

# Instalar dependencias de Node.js
npm install
```

## 🚀 Deployment

Para deployar la aplicación en AWS:

```bash
serverless deploy
```

El comando anterior:
- Creará automáticamente la tabla de DynamoDB
- Desplegará las funciones Lambda
- Configurará API Gateway
- Instalará automáticamente las dependencias de Python usando el plugin `serverless-python-requirements`

## 📡 Endpoints de la API

Después del deployment, obtendrás una URL base similar a:
`https://xxxxxxxxxx.execute-api.us-east-2.amazonaws.com/dev`

### 1. Crear Nota
**POST** `/notas`

Crea una nueva nota en el sistema.

**Ejemplo con curl:**
```bash
curl -X POST https://xxxxxxxxxx.execute-api.us-east-2.amazonaws.com/dev/notas \
  -H "Content-Type: application/json" \
  -d '{
    "texto": "Esta es mi primera nota"
  }'
```

**Respuesta exitosa (201):**
```json
{
  "note": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "texto": "Esta es mi primera nota"
  }
}
```

### 2. Obtener Nota
**GET** `/notas/{id}`

Obtiene una nota específica por su ID.

**Ejemplo con curl:**
```bash
curl https://xxxxxxxxxx.execute-api.us-east-2.amazonaws.com/dev/notas/550e8400-e29b-41d4-a716-446655440000
```

**Respuesta exitosa (200):**
```json
{
  "note": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "texto": "Esta es mi primera nota"
  }
}
```

**Respuesta cuando no se encuentra (404):**
```json
{
  "error": "Nota no encontrada"
}
```

## 📖 Documentación Adicional

Para conocer más sobre el proceso de desarrollo, problemas encontrados y decisiones técnicas tomadas durante la implementación, consulta:

👉 **[Proceso de Desarrollo y Lecciones Aprendidas](./DEVELOPMENT_PROCESS.md)**
