#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 OpenERP SA (<http://openerp.com>). All Rights Reserved
# 
#    from num2words import num2words
#    import base64
#    import re
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import api, models

class customer_invoice_report(models.AbstractModel):
    _name = 'report.customer_invoice_report.customer_invoice'
    _description = "Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        record = self.env['account.move'].browse(docids)

        company = self.env['res.company'].search([('id','=',1)])





        return {
            'doc_ids': docids,
            'doc_model':'account.move',
            'data': data,
            'docs': record,
            'company': company,
        }


