# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    ed_position_id = fields.Many2one(
        comodel_name='education.position', string='Position')
    ed_work_reason_id = fields.Many2one(
        comodel_name='education.work_reason', string='Work Reason')
    ed_contract_type_id = fields.Many2one(
        comodel_name='education.contract_type', string='Contract Type')
    ed_workday_type_id = fields.Many2one(
        comodel_name='education.workday_type', string='Workday Type')
    ed_contract_hours = fields.Float(string='Contract Hours')