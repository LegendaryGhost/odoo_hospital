from odoo import models, fields

class HospitalDisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Maladie'

    name = fields.Char(required=True)
    description = fields.Text()
    symptom_ids = fields.Many2many('hospital.symptom', string="Symptômes")