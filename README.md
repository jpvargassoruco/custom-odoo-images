# Resumen de Implementación de Imágenes Odoo

## Cambios Realizados
- **Estructura de Directorios:** Se crearon los directorios `17.0`, `18.0` y `19.0` con sus respectivos `Dockerfile`.
- **Clonado de Repositorios Adicionales:** Cada Dockerfile se configuró para clonar `muk-it/odoo-modules` y `odoomates/odooapps` en carpetas específicas (`muk-odoo-modules` y `odoomates-odooapps`) dentro de `/mnt/extra-addons`. En caso de que un tag por versión no exista temporalmente en sus ramas, se hace un "fallback" a la clonación por defecto para la resiliencia del pipeline.
- **Módulo de Autoconfiguración (`odoo_setup_wizard`):** Se desarrolló desde cero un Addon personalizado para optimizar la puesta en marcha:
  - Inyecta preinstalación de todas las aplicaciones solicitadas: `crm, sale_management, point_of_sale, account, purchase, stock, maintenance, repair, project, hr_timesheet, hr, hr_recruitment, hr_holidays, hr_attendance, hr_expense, fleet, mail, calendar, contacts, note`.
  - Contiene un asistente (`TransientModel`) en los Ajustes que permite dictar en una sola pantalla el nombre de la empresa, y subir el Logotipo y Favicon (incluyendo recomendaciones de formato, ej: en caso del avatar un cuadrado de 256x256 px). Al guardar, esto se aplica globalmente en `res.company`.
- **Instalación Inicial Automatizada:** Usamos una directiva `CMD` en los ficheros Docker que arranca Odoo con `--addons-path` explícito (los repos de github clonados más las carpetas base de odoo) y obliga un `odoo -i odoo_setup_wizard`. Automáticamente la base de datos descargará e instalará todas las dependencias.
- **Integración Continua (CI/CD):** Se creó `.github/workflows/docker-publish.yml` listo para accionar GitHub Actions y empujar la versión generada a **GitHub Container Registry (GHCR)** con las etiquetas (`tags`) correctas (`17.0`, `18.0`, `19.0`).

## Sobre el Idioma de la Base de Datos
Odoo arranca por defecto en **Inglés (EE.UU.)**.
Sin embargo, **antes** de que el contenedor comience a instalar las aplicaciones automáticas, Odoo te presenta el "Gestor de Bases de Datos" en el navegador (`http://localhost:8069`). 
En esa misma pantalla de creación es donde el usuario (tú) debe seleccionar el país y el idioma de preferencia (ej. Español/España o Español/Latinoamérica). Una vez seleccionas el idioma y haces clic en "Crear", Odoo genera la base de datos en español y procede con la instalación desatendida del `odoo_setup_wizard`.

## Resultados de Validación
- Validada la gramática de Odoo XML para la vista del asistente de configuración (`setup_wizard_views.xml`).
- Verificada la escritura del archivo de privilegios de seguridad (`ir.model.access.csv`).
- Verificada de forma estática la corrección de los comandos de Docker. El sistema se encuentra completamente posicionado para publicar utilizando GitHub Actions.

## Docker compose de ejemplo
```yaml
version: '3.8'

services:
  web:
    # Selecciona el "tag" de la versión que quieres usar: 17.0, 18.0 o 19.0
    image: ghcr.io/jpvargassoruco/custom-odoo-images:18.0
    depends_on:
      - db
    ports:
      - "8069:8069"
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=my_secure_password
    volumes:
      - odoo-web-data:/var/lib/odoo

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_PASSWORD=my_secure_password
      - POSTGRES_USER=odoo
    volumes:
      - odoo-db-data:/var/lib/postgresql/data

volumes:
  odoo-web-data:
  odoo-db-data:
```
