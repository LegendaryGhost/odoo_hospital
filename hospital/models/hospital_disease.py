from odoo import models, fields

class HospitalDisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Maladie'

    name = fields.Char(required=True)
    description = fields.Text()
    symptom_ids = fields.Many2many('hospital.symptom', string="Symptômes")
    is_grave = fields.Boolean("Est grave ?", required=True, default=False)
    needs_medicine = fields.Boolean("A besoin de médicaments ?", required=True, default=True)
    final_action = fields.Selection([
        ('go_home_medication', "Rentre avec des médicaments"),
        ('hospitalize', "Hospitalisé pour le traitement"),
    ], string="Décision finale", required=True)
    hospital_days = fields.Integer("Nombre de jours (si hospitalisé)")