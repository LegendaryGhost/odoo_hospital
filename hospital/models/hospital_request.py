from odoo import models, fields

class HospitalRequest(models.Model):
    _name = 'hospital.request'
    _description = 'Medical request from the patient'

    patient_id = fields.Many2one('res.users', string='Patient', required=True)
    symptom_ids = fields.Many2many('hospital.symptom', string='Symptômes')
    note        = fields.Text(string='Commentaires')
