# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class TeamWork(models.Model):
    _name = 'team.work'

    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string='Photo')
    position = fields.Char(string='Position')
    subject = fields.Char(string='Subject')
    description = fields.Text(string='Description')


