from odoo import models,fields

class ResPartner(models.Model):
    _inherit='res.partner'

    student_code=fields.Char()
    