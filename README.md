# Automobile_web
The framework Automobile reestructured to use just for web,
this will make it faster and easier to read and maintain

# Automobile_web — Automatización de pruebas Bykon Consulting

Suite de pruebas automatizadas end-to-end para el sitio [bykon.com.mx](https://www.bykon.com.mx/), construida con **Behave** (BDD) y **Playwright**, con reportes integrados en **Allure**.

## 📋 Descripción

Este proyecto valida flujos clave de navegación y UI del sitio de Digital-ByKon Consulting, incluyendo:

- Carga correcta de la página principal.
- Acceso al Aviso de Privacidad.
- Navegación a la sección de Servicios Digitales.
- Apertura del modal para agendar una llamada ("Book a call").
- Validación visual del sitio al traducirlo al español (vía Google Translate y vía selector nativo de idioma).

## 🗂️ Estructura del proyecto

```
Automobile_web/
├── features/
│   ├── pages/                 # Page Objects
│   │   ├── base_page.py
│   │   ├── book_call_page.py
│   │   ├── digital_page.py
│   │   └── home_page.py
│   ├── steps/                 # Definición de steps de Behave
│   │   └── web_steps.py
│   ├── utils/
│   │   └── report_helpers.py  # Utilidades para adjuntar capturas a Allure
│   ├── bykon.feature           # Escenarios en Gherkin
│   └── environment.py          # Hooks (before_all, after_step, after_all)
├── behave.ini.py
└── requirements.txt
```

## 🔧 Requisitos previos

- Python 3.9+
- pip

## 📦 Instalación

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd Automobile_web
   ```

2. Crea y activa un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate      # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Instala los navegadores de Playwright:
   ```bash
   playwright install
   ```

## ▶️ Ejecución de las pruebas

Ejecutar toda la suite:
```bash
behave
```

Ejecutar un feature específico:
```bash
behave features/bykon.feature
```

> **Nota:** Actualmente el navegador se ejecuta en modo visible (`headless=False`) según lo configurado en `environment.py`. Si deseas ejecutarlo en modo headless, ajusta esa variable o reactiva el uso de la variable de entorno `PLAYWRIGHT_HEADLESS`.

## 📊 Reportes con Allure

Este proyecto genera evidencias (capturas de pantalla) automáticamente cuando un step falla, y también en el escenario de validación visual en español, adjuntándolas al reporte de Allure.

Para generar y visualizar el reporte (requiere tener Allure Commandline instalado):
```bash
behave -f allure_behave.formatter:AllureFormatter -o ./reports/allure-results
allure serve ./reports/allure-results
```

## 🧩 Tecnologías utilizadas

| Herramienta       | Uso                                      |
|-------------------|-------------------------------------------|
| [Behave](https://behave.readthedocs.io/) | Framework BDD (Gherkin)     |
| [Playwright](https://playwright.dev/python/) | Automatización de navegador |
| [Allure](https://docs.qameta.io/allure/) | Reportería de pruebas         |
| [Pillow](https://pillow.readthedocs.io/) / [pixelmatch](https://pypi.org/project/pixelmatch/) | Comparación/validación visual |

## 📝 Escenarios cubiertos (`bykon.feature`)

- ✅ Carga exitosa de la página principal
- ✅ Acceso al Aviso de Privacidad mediante scroll
- ✅ Navegación a la sección de Servicios Digitales
- ✅ Apertura del modal para agendar una llamada
- ✅ Validación de diseño al traducir la página con Google Translate
- ✅ Validación de diseño al traducir la página con el selector nativo (bandera de México)

## 👤 Autora

**Mariana Torres** basado en el framework Automobile