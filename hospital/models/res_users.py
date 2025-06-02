from odoo import fields, models

class ResUsers(models.Model):
    _inherit = 'res.users'

    patient_state = fields.Selection([
        ('treatment', 'En traitement'),
        ('remission', 'En rémission'),
        ('free', 'Libre de partir'),
    ], string="État du patient", default='treatment')
    request_ids = fields.One2many('hospital.request', 'patient_id', string='Demandes médicales')
