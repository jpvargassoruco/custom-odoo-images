from odoo import api, fields, models

class OdooSetupWizard(models.TransientModel):
    _name = 'odoo.setup.wizard'
    _description = 'Asistente de Configuración Inicial'

    company_name = fields.Char(string='Nombre de la Empresa', required=True, default=lambda self: self.env.company.name)
    company_logo = fields.Image(string='Logo de la Empresa', help='Proporciones recomendadas: 256x256 px o 512x512 px, formato cuadrado idealmente para el logo general y favicon.')
    company_favicon = fields.Image(string='Favicon', help='El logo que aparecerá en la pestaña del navegador (recomendado: 32x32 px o 256x256 px).')
    currency_id = fields.Many2one('res.currency', string='Moneda Principal', default=lambda self: self.env.company.currency_id.id)
    
    def apply_settings(self):
        self.ensure_one()
        company = self.env.company
        
        # Actualizamos la compañía
        vals = {
            'name': self.company_name,
        }
        if self.company_logo:
            vals['logo'] = self.company_logo
        if self.company_favicon:
            vals['favicon'] = self.company_favicon
        if self.currency_id:
            vals['currency_id'] = self.currency_id.id
            
        company.write(vals)

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
