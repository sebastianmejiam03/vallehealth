# 🏥 ValleHealth

Dashboard epidemiológico para el monitoreo de enfermedades en el **Valle del Cauca**, basado en datos reales del SIVIGILA (Instituto Nacional de Salud de Colombia).

## 🌐 Demo en vivo
- **Frontend:** https://magnifico-chebakia-4b62d4.netlify.app
- **API Backend:** https://vallehealth-backend.onrender.com/docs

## 📋 Descripción
ValleHealth es una aplicación web que presenta dashboards interactivos con información epidemiológica del Valle del Cauca. Permite a ciudadanos y profesionales de salud consultar y analizar datos de enfermedades por municipio.

## 👥 Usuarios
- **Ciudadano:** Consulta enfermedades y alertas en su municipio
- **Profesional de salud / Admin:** Análisis avanzado, gestión de datos y exportación CSV

## 🛠️ Tecnologías
| Componente | Tecnología |
|---|---|
| Backend | Python + FastAPI |
| Base de datos | PostgreSQL |
| Frontend | HTML + CSS + JavaScript + Chart.js |
| Despliegue backend | Render.com |
| Despliegue frontend | Netlify |
| Dataset | SIVIGILA – INS Colombia |

## 🚀 Cómo ejecutar localmente

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
open frontend/index.html
```

## 📊 Dataset
Los datos provienen del **SIVIGILA** (Sistema de Vigilancia en Salud Pública) del Instituto Nacional de Salud de Colombia. Contiene **23,983 casos reales** de Dengue en el Valle del Cauca para el año 2023.

## 📁 Estructura del proyecto
```
vallehealth/
├── backend/
│   ├── main.py          # API REST con FastAPI
│   ├── models.py        # Modelos de base de datos
│   ├── database.py      # Conexión PostgreSQL
│   └── requirements.txt
├── frontend/
│   ├── index.html       # Dashboard principal
│   ├── dashboard.html   # Vista con filtros
│   ├── login.html       # Inicio de sesión
│   └── admin.html       # Panel administrador
└── README.md
```

## 👨‍💻 Desarrollado por
Proyecto de curso – Redes e Infraestructura 2025-03
