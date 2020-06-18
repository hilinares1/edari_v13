# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import timedelta,datetime,date
from odoo.exceptions import Warning, ValidationError

from datetime import datetime
from dateutil.relativedelta import relativedelta


class AccMoveExt(models.Model):
	_inherit='account.move'

	sale_order_id = fields.Many2one('sale.order',string="Sale Order")
	employee = fields.Many2one('hr.employee', string="Employee")
	automated_invoice = fields.Boolean(string = "Automated Invoice")
	invoice_month = fields.Date(string= "Invoice Month")
	from_date = fields.Date(string= "From Date")
	to_date = fields.Date(string= "To Date")

	pro_rate_adjust = fields.Float(string= "Pro Rate Adjustment")
	leave_taken = fields.Float(string= "Leave Taken")
	sick_days_taken = fields.Float(string= "Sick Days Taken")



class ProductExtension(models.Model):
	_inherit='product.product'

	accruing_account_id = fields.Many2one('account.account',string = "Accrued Account")


# class PartnerExtensionSo(models.Model):
# 	_inherit='res.partner'

# 	function_contact = fields.Selection([
# 		('primary','Primary'),
# 		('billing','Billing'),
# 		], string='Function', default="primary")
