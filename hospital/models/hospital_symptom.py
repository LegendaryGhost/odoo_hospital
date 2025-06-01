from odoo import models, fields

class HospitalSymptom(models.Model):
    _name = 'hospital.symptom'
    _description = 'Symptom'

    name = fields.Char(required=True)
    description = fields.Text()