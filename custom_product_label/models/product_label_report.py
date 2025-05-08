from odoo import models, api

class ProductLabelReportData(models.AbstractModel):
    _name = 'report.product.report_productlabel_dymo'
    _description = 'Reporte de etiquetas DYMO con datos extendidos'

    @api.model
    def _get_report_values(self, docids, data=None):
        products = self.env['product.product'].browse(docids)

        # Buscar lote más reciente desde órdenes de fabricación
        production_data = {}
        for product in products:
            production = self.env['mrp.production'].search([
                ('product_id', '=', product.id)
            ], order='date_start desc', limit=1)
            production_data[product.id] = production.lot_producing_id.name if production.lot_producing_id else ""

        # La estructura esperada por el template original
        quantity = {p: [(p.barcode, 1)] for p in products}

        return {
            'quantity': quantity,
            'production_data': production_data,
        }
