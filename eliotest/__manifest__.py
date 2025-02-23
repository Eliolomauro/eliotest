{
    'name': 'elio User Data Manager',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Salva dati per singolo utente',
    'description': """
        Un modulo base per salvare dati personalizzati per ogni singolo utente.
    """,
    'author': 'Elio',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/user_data_rules.xml',
        
        'views/user_data_view.xml',
    ],
    'assets': {
    'web.assets_backend': [
       
        'eliotest/static/src/css/image_preview.css',
        # 'eliotest/static/src/js/image_preview.js',
    ],
},
    'installable': True,
    'application': False,
}
