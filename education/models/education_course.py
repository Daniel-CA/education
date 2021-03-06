# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class EducationCourse(models.Model):
    _name = 'education.course'
    _inherit = 'education.data'
    _description = 'Course'

    level_id = fields.Many2one(
        comodel_name='education.level', string='Education Level',
        required=True, ondelete='cascade')
    field_id = fields.Many2one(
        comodel_name='education.field', string='Study Field')
    plan_id = fields.Many2one(
        comodel_name='education.plan', string='Education Plan')
    shift_id = fields.Many2one(
        comodel_name='education.shift', string='Shift')
    level_subject_ids = fields.One2many(
        comodel_name='education.level.course.subject',
        inverse_name='course_id', string='Subjects by Level')

    _sql_constraints = [
        ('education_code_unique', 'unique(education_code,level_id,field_id)',
         'Education code must be unique per level and field!'),
    ]

    @api.multi
    def name_get(self):
        """ name_get() -> [(id, name), ...]

        Returns a textual representation for the records in ``self``.
        By default this is the value of the ``display_name`` field.

        :return: list of pairs ``(id, text_repr)`` for each records
        :rtype: list(tuple)
        """
        result = []
        for record in self:
            if record.field_id:
                result.append((record.id, '[{}] {} ({})'.format(
                    record.education_code, record.description,
                    record.field_id.description)))
            else:
                result.append(super(EducationCourse, record).name_get()[0])
        return result
