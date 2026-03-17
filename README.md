# ValleHealth

Aplicación web para visualizar datos epidemiológicos del Valle del Cauca, desarrollada como proyecto del curso Redes e Infraestructura 2025-03 en la Universidad Autónoma de Occidente.

## ¿Qué hace?

Muestra un dashboard con información de enfermedades reportadas en los municipios del Valle del Cauca, usando datos reales del SIVIGILA del Instituto Nacional de Salud de Colombia.

## Links

- App: https://magnifico-chebakia-4b62d4.netlify.app
- API: https://vallehealth-backend.onrender.com/docs

## Tecnologías usadas

- Backend: Python con FastAPI
- Base de datos: PostgreSQL
- Frontend: HTML, CSS y JavaScript con Chart.js
- Despliegue: Render (backend) y Netlify (frontend)
- Dataset: SIVIGILA 2023 – INS Colombia (23.983 casos de Dengue en el Valle del Cauca)

## Cómo correrlo localmente

Clonar el repositorio:
```bash
git clone https://github.com/SebastianMejiam03/vallehealth.git
```

Instalar dependencias del backend:
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Abrir el frontend:
```bash
open frontend/index.html
```

## Estructura
```
vallehealth/
├── backend/       # API REST con FastAPI
├── frontend/      # Páginas HTML del dashboard
└── README.md
```
