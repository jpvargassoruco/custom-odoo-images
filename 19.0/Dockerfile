FROM odoo:19.0

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /mnt/extra-addons

RUN git clone -b 19.0 https://github.com/muk-it/odoo-modules.git /mnt/extra-addons/muk-odoo-modules || \
    git clone https://github.com/muk-it/odoo-modules.git /mnt/extra-addons/muk-odoo-modules
    
RUN git clone -b 19.0 https://github.com/odoomates/odooapps.git /mnt/extra-addons/odoomates-odooapps || \
    git clone https://github.com/odoomates/odooapps.git /mnt/extra-addons/odoomates-odooapps

COPY custom_addons/odoo_setup_wizard /mnt/extra-addons/odoo_setup_wizard

RUN chown -R odoo:odoo /mnt/extra-addons

USER odoo

CMD ["odoo", "--addons-path", "/mnt/extra-addons,/mnt/extra-addons/muk-odoo-modules,/mnt/extra-addons/odoomates-odooapps,/usr/lib/python3/dist-packages/odoo/addons", "-i", "odoo_setup_wizard"]
