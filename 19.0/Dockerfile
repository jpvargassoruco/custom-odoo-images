FROM odoo:19.0

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/custom-addons

RUN git clone -b 19.0 https://github.com/muk-it/odoo-modules.git /opt/custom-addons/muk-odoo-modules || \
    git clone https://github.com/muk-it/odoo-modules.git /opt/custom-addons/muk-odoo-modules
    
RUN git clone -b 19.0 https://github.com/odoomates/odooapps.git /opt/custom-addons/odoomates-odooapps || \
    git clone https://github.com/odoomates/odooapps.git /opt/custom-addons/odoomates-odooapps

COPY 19.0/custom_addons/odoo_setup_wizard /opt/custom-addons/odoo_setup_wizard

RUN chown -R odoo:odoo /opt/custom-addons

# Copy and set our entrypoint wrapper
COPY 19.0/entrypoint-custom.sh /entrypoint-custom.sh
RUN chmod +x /entrypoint-custom.sh

USER odoo

ENTRYPOINT ["/entrypoint-custom.sh"]
CMD ["odoo"]
