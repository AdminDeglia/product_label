# -*- coding: utf-8 -*-
from odoo import models, api

class ProductLabelSimpleDymoReport(models.AbstractModel):
    _name = 'report.product.report_simple_label_dymo'
    _inherit = 'report.report_abstract'

    @api.model
    def _get_report_values(self, docids, data=None):
        products = self.env['product.product'].browse(docids)

        production_data = {}
        for product in products:
            production = self.env['mrp.production'].search([
                ('product_id', '=', product.id)
            ], order='date_start desc', limit=1)
            production_data[product.id] = production.lot_producing_id.name if production.lot_producing_id else ""

        return {
            'docs': products,
            'production_data': production_data,
        }
