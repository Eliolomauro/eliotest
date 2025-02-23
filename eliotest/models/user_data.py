from odoo import models, fields, api

class UserData(models.Model):
    _name = 'user.data'
    _description = 'Dati Utente Personalizzati'
    _rec_name = 'name'

    name = fields.Char(string='Nome Dato', required=True)
    value = fields.Text(string='Valore')
    user_id = fields.Many2one('res.users', string='Utente', required=True, default=lambda self: self.env.user)
    image = fields.Image(string='Immagine', max_width=800, max_height=800, required=False)


    # Override della funzione search per mostrare solo i dati dell'utente corrente
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        args.append(('user_id', '=', self.env.user.id))
        return super(UserData, self).search(args, offset, limit, order, count)
