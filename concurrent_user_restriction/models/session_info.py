from datetime import datetime
from email.policy import default

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.http import request


class SessionInfo(models.Model):
    _name = 'session.info'

    name = fields.Char()
    session_id = fields.Char()
    last_access_time = fields.Datetime()
    last_visit_time = fields.Datetime()
    family_id = fields.Many2one('family.attribute')
    brand_id = fields.Many2one('product.brand')
    attribute_id = fields.Many2one('product.attribute')
    attribute_group_id = fields.Many2one('attribute.group')
    supplier_id = fields.Many2one('supplier.info')
    active_state = fields.Boolean(default=True)


