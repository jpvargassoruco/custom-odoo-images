FROM odoo:17.0

USER root

# Instalar git para clonar repositorios
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

# Asegurar la existencia del directorio base para addons
RUN mkdir -p /mnt/extra-addons

# Clonar los repositorios requeridos en sus carpetas indicadas
RUN git clone -b 17.0 https://github.com/muk-it/odoo-modules.git /mnt/extra-addons/muk-odoo-modules || \
    git clone https://github.com/muk-it/odoo-modules.git /mnt/extra-addons/muk-odoo-modules
    
RUN git clone -b 17.0 https://github.com/odoomates/odooapps.git /mnt/extra-addons/odoomates-odooapps || \
    git clone https://github.com/odoomates/odooapps.git /mnt/extra-addons/odoomates-odooapps

# Copiar el módulo de autoconfiguración
COPY 17.0/custom_addons/odoo_setup_wizard /mnt/extra-addons/odoo_setup_wizard

# Configurar permisos para el usuario odoo
RUN chown -R odoo:odoo /mnt/extra-addons

USER odoo

# Modificamos el comando de arranque para configurar el addons_path explícitamente y autoinstalar el wizard
CMD ["odoo", "--addons-path", "/mnt/extra-addons,/mnt/extra-addons/muk-odoo-modules,/mnt/extra-addons/odoomates-odooapps,/usr/lib/python3/dist-packages/odoo/addons", "-i", "odoo_setup_wizard"]
