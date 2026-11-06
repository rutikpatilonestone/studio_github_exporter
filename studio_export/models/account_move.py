# Generated from Odoo Studio fields.
from odoo import fields, models


class AccountMove(models.Model):

    _inherit = 'account.move'

    x_studio_new_studio_field = fields.Char(
        string='New Studio Field'
    )
