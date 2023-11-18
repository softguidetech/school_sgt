# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class Students(models.Model):
    _inherit = 'student.student'

    comment = fields.Text('Comments')

