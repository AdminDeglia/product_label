from odoo import models

class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'

    def _get_report_templates_domain(self):
        domain = super()._get_report_templates_domain()

        # Asegurarnos de incluir también nuestra plantilla personalizada
        domain = ['|'] + domain + [('report_name', '=', 'custom_product_label.my_dymo_template')]
        return domain
