# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


# class SchoolFees(models.Model):
#     _name = 'your.module.company.messages'
#     _description = 'Company Messages'
#
#     name = fields.Char('Message Title', required=True)
#     description = fields.Text('Message Description')
#     image = fields.Binary('Image')
#     company_id = fields.Many2one('res.company', string='Company')



class ResCompany(models.Model):
    _inherit = 'res.company'

    vision_message = fields.Text('Vision Message')
    vision_photo = fields.Binary('vision Photo')
    mission_message = fields.Text('Mission Message')
    mission_photo = fields.Binary('Mission Photo')
    core_beliefs_message = fields.Text('Core Beliefs Message')
    core_beliefs_photo = fields.Binary('Core Beliefs Photo')
    pupil_care_message = fields.Text('Pupil Care Message')
    pupil_care_photo = fields.Binary('Pupil Care Photo')

    principal_trip_message = fields.Text("Principlal's trip Message")
    principal_education_message = fields.Text("Principlal's education Message")

    fees_message = fields.Text('Vision Message')
    primary_school_description = fields.Text('Primary School Description')
    middle_school_description = fields.Text('Middle School Description')


