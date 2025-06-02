from odoo import models, fields

class HospitalSymptom(models.Model):
    _name = 'hospital.symptom'
    _description = 'Symptôme'

    name = fields.Char(required=True)
    description = fields.Text()