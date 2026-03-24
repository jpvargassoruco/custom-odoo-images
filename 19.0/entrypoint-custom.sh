#!/bin/bash
set -e

# If the command starts with '-', prepend 'odoo'
if [ "${1:0:1}" = '-' ]; then
    set -- odoo "$@"
fi

# Intercept the 'odoo' command to append our custom modules and install flags
if [ "$1" = 'odoo' ]; then
    # 1. We must append our baked custom addon paths to the standard ones.
    # We include /mnt/extra-addons so the K8s cloned addons still work.
    set -- "$@" --addons-path="/mnt/extra-addons,/opt/custom-addons,/opt/custom-addons/muk-odoo-modules,/opt/custom-addons/odoomates-odooapps,/usr/lib/python3/dist-packages/odoo/addons"
    
    # 2. If this is not an 'odoo shell' command, we trigger the auto-installation
    # of our custom setup wizard on startup so it styles the tenant base.
    if [[ "$*" != *"shell"* ]]; then
        set -- "$@" -i odoo_setup_wizard
    fi
fi

# Fallback to the official Odoo entrypoint script to handle the rest of the bootstrapping
echo "Executing custom entrypoint with args: $@"
exec /entrypoint.sh "$@"
