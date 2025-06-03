from odoo import models, fields

class HospitalRequest(models.Model):
    _name = 'hospital.request'
    _description = 'Medical Request'

    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('assigned', 'Assigned'),
            ('treated', 'Treated'),
        ],
        default='new',
        string='Status',
    )
    patient_id = fields.Many2one('res.partner', string='Patient', required=True)
    symptom_ids = fields.Many2many('hospital.symptom', string='Symptoms')
    note        = fields.Text(string='Comments')
    nurse_id = fields.Many2one('res.users', string='Nurse', default=lambda self: self.env.user)
    doctor_id = fields.Many2one('res.users', string='Assigned Doctor')
