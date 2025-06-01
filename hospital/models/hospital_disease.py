from odoo import models, fields

class HospitalDisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Disease'

    name = fields.Char(required=True)
    description = fields.Text()
    symptom_ids = fields.Many2many('hospital.symptom', string="Symptoms")
    is_grave = fields.Boolean("Is Grave?", required=True, default=False)
    needs_medicine = fields.Boolean("Needs Medication?", required=True, default=True)
    final_action = fields.Selection([
        ('go_home_medication', "Go home with medication"),
        ('hospitalize', "Hospitalize for treatment"),
    ], string="Final Action", required=True)
    hospital_days = fields.Integer("Number of Days (if hospitalized)")