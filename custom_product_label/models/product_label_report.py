ffrom odoo import models, api

class ProductAndMrpLabelReport(models.AbstractModel):
    _name = 'report.custom_product_label.my_dymo_template'
    _description = 'Etiqueta térmica personalizada (Producto y Fabricación)'

    @api.model
    def _get_report_values(self, docids, data=None):
        active_model = self.env.context.get('active_model')
        production_data = {}

        if active_model == 'product.template':
            templates = self.env['product.template'].browse(docids)
            variants = templates.mapped('product_variant_ids')

            for variant in variants:
                production = self.env['mrp.production'].search([
                    ('product_id', '=', variant.id)
                ], order='date_start desc', limit=1)
                production_data[variant.id] = production.lot_producing_id.name if production.lot_producing_id else ""

        elif active_model == 'mrp.production':
            orders = self.env['mrp.production'].browse(docids)
            variants = []

            for order in orders:
                qty = int(order.product_qty)
                variants.extend([order.product_id] * qty)
                production_data[order.product_id.id] = order.lot_producing_id.name if order.lot_producing_id else ""

        else:
            variants = []

        return {
            'docs': variants,
            'production_data': production_data,
        }
