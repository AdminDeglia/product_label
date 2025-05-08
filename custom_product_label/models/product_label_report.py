from odoo import models, api

class ProductTemplateLabelReport(models.AbstractModel):
    _name = 'report.product.report_producttemplatelabel_dymo'  # ¡ESTE es el nombre correcto!
    _description = 'Reporte de etiquetas DYMO desde product.template'

    @api.model
    def _get_report_values(self, docids, data=None):
        templates = self.env['product.template'].browse(docids)

        # Crear diccionario con lotes por variante
        production_data = {}
        for template in templates:
            for variant in template.product_variant_ids:
                production = self.env['mrp.production'].search([
                    ('product_id', '=', variant.id)
                ], order='date_start desc', limit=1)
                production_data[variant.id] = production.lot_producing_id.name if production.lot_producing_id else ""

        return {
            'docs': templates,
            'production_data': production_data,
        }
