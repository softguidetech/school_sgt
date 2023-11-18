from odoo import fields, http, SUPERUSER_ID, _
from odoo.http import request
import werkzeug
from odoo.osv.expression import AND, OR
from odoo.tools import groupby as groupbyelem
from odoo.addons.portal.controllers import portal
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from collections import OrderedDict
from operator import itemgetter
from odoo.exceptions import AccessError, MissingError
import base64
from odoo.tools import plaintext2html
from datetime import datetime, timedelta,date

class SchoolPortal(portal.CustomerPortal):

    @http.route(['/teachers', '/teachers/page/<int:page>'], type='http', auth="user", website=True)
    def portal_teachers(self, **kwargs):
        teachers = request.env['school.teacher'].sudo().search([])
        values = {
            'teachers': teachers
        }
        return request.render("school_figma.portal_teachers", values)

    @http.route(['/principal_msg', '/principal_msg/page/<int:page>'], type='http', auth="user", website=True)
    def portal_principal_msg(self, **kwargs):
        company = request.env.company
        values = {
            'company': company
        }
        return request.render("school_figma.portal_principal_msg", values)

    @http.route(['/our_values', '/our_values/page/<int:page>'], type='http', auth="user", website=True)
    def portal_our_values(self, **kwargs):
        company = request.env.company
        values = {
            'company': company
        }
        return request.render("school_figma.portal_our_values", values)\

    @http.route(['/school_fees', '/school_fees/page/<int:page>'], type='http', auth="user", website=True)
    def portal_school_fees(self, **kwargs):
        company = request.env.company
        values = {
            'company': company
        }
        return request.render("school_figma.portal_school_fees", values)

    @http.route(['/school_admission', '/school_admission/page/<int:page>'], type='http', auth="user", website=True)
    def portal_school_admission(self, **kwargs):
        return request.render("school_figma.portal_school_admission")

    @http.route(['/', '//page/<int:page>'], type='http', auth="user", website=True)
    def custom_homepage(self, **kwargs):
        team_works = request.env['team.work'].sudo().search([], limit=3)
        students = request.env['student.student'].sudo().search([], limit=3)
        subjects = request.env['subject.subject'].sudo().search([], limit=3)
        values = {
            'team_works': team_works,
            'students': students,
            'subjects': subjects
        }
        return request.render("school_figma.custom_homepage", values)




