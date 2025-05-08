from odoo import models, api

class ProductTemplateCustomDymoReport(models.AbstractModel):
    _name = 'report.custom_product_label.my_dymo_template'
    _description = 'Etiqueta térmica personalizada directa'

    @api.model
    def _get_report_values(self, docids, data=None):
        templates = self.env['product.template'].browse(docids)
        variants = templates.mapped('product_variant_ids')

        production_data = {}
        for variant in variants:
            production = self.env['mrp.production'].search([
                ('product_id', '=', variant.id)
            ], order='date_start desc', limit=1)
            production_data[variant.id] = production.lot_producing_id.name if production.lot_producing_id else ""

        return {
            'docs': variants,
            'production_data': production_data,
        }
