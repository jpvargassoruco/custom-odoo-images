{
    'name': 'Odoo Setup Wizard',
    'version': '1.0',
    'category': 'Administration',
    'summary': 'Asistente de configuración inicial para la empresa y módulos por defecto.',
    'description': """
        Este módulo automatiza la instalación de aplicaciones por defecto y
        proporciona un asistente interactivo para configurar los datos básicos 
        de la compañía (Logo, Nombre, Favicon) desde un solo lugar.
    """,
    'author': 'Custom Images',
    'depends': [
        'base',
        'web',
        'crm', 
        'sale_management', 
        'point_of_sale', 
        'account', 
        'purchase', 
        'stock', 
        'maintenance', 
        'repair', 
        'project', 
        'hr_timesheet', 
        'hr', 
        'hr_recruitment', 
        'hr_holidays', 
        'hr_attendance', 
        'hr_expense', 
        'fleet', 
        'mail', 
        'calendar', 
        'contacts', 
        'note'
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/setup_wizard_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
