from odoo import models, fields, api


class SousActions(models.Model):
    _name = 'sous.actions'
    _description = 'Sous Actions'

    numero_sequentiel = fields.Char(string='Numéro Séquentiel', readonly=True)
    responsable_realisation = fields.Many2one('hr.employee', string='Responsable de Réalisation')
    delai_realisation = fields.Datetime(string='Délai de Réalisation')
    responsable_suivi = fields.Many2one('hr.employee', string='Responsable de Suivi')
    delai_suivi = fields.Datetime(string='Délai de Suivi')
    gravite = fields.Selection([
        ('faible', 'Faible'),
        ('moyenne', 'Moyenne'),
        ('elevee', 'Élevée')
    ], string='Gravité')
    priorite = fields.Selection([
        ('basse', 'Basse'),
        ('moyenne', 'Moyenne'),
        ('haute', 'Haute')
    ], string='Priorité')
    piece_jointe = fields.Binary(string='Pièce Jointe')

    action_id = fields.Many2one('action', string="Action Principale", ondelete='cascade')


    @api.model
    def create(self, vals):
        # Générer un numéro séquentiel automatiquement (optionnel)
        if vals.get('numero_sequentiel', 'New') == 'New':
            vals['numero_sequentiel'] = self.env['ir.sequence'].next_by_code('sous.actions') or 'New'
        return super(SousActions, self).create(vals)
