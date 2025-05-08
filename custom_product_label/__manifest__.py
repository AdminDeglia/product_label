{
    'name': 'Etiquetas de producto personalizadas tipo Dymo',
    'version': '1.0',
    'summary': 'Modifica la vista de etiquetas de productos',
    'author': 'Deglia',
    'depends': ['product', 'stock','mrp','product_dimensions'],
    'data': [
        'views/custom_label.xml',  
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
