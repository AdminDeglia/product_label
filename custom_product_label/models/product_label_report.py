from odoo import models, api

# Etiqueta desde productos (una sola etiqueta por producto)
class ProductTemplateLabelReport(models.AbstractModel):
    _name = 'report.custom_product_label.product_dymo_template'
    _description = 'Etiqueta térmica desde producto'

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

# Etiqueta desde orden de fabricación (una etiqueta por unidad)
class MrpProductionLabelReport(models.AbstractModel):
    _name = 'report.custom_product_label.mrp_dymo_template'
    _description = 'Etiqueta térmica desde orden de fabricación'

    @api.model
    def _get_report_values(self, docids, data=None):
        orders = self.env['mrp.production'].browse(docids)

        variants = []
        production_data = {}

        for order in orders:
            variant = order.product_id
            qty = int(order.product_qty)
            variants.extend([variant] * qty)

            production_data[variant.id] = order.lot_producing_id.name if order.lot_producing_id else ""

        return {
            'docs': variants,
            'production_data': production_data,
        }
