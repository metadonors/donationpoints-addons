# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsVisit(models.Model):

    _name = 'donationpoints.visit'
    _description = 'Donationpoints Visit'

    visit_date = fields.Date(string=_("Visit Date"), required=True)
    visit_type_id = fields.Many2one('donationpoints.visit.type', string=_('Type'))
    user_id = fields.Many2one('res.users', string=_('User'), required=True)
    donationbox_id = fields.Many2one('donationpoints.donationbox', string=_('Donation Box'), required=True)
    condition_id = fields.Many2one('donationpoints.donationbox.condition', string=_('Condition'), store=True)
    location_id = fields.Many2one('donationpoints.location', string=_('Location'), store=True, required=True)
    amount = fields.Monetary(currency_field='currency_id', string=_('Amount'), store=True)
    currency_id = fields.Many2one('res.currency', 'Currency', readonly=True)


    @api.onchange('donationbox_id')
    def _donationbox_condition_state(self):
        for record in self:
            if record.donationbox_id:
                record.condition_id = record.donationbox_id.condition_id

    @api.model
    def write(self,vals):
        ret = super(DonationpointsVisit, self).write(vals)
        vals['donationbox_id'].write({'condition_id':vals['condition_id']})
        return ret

    @api.model
    def create(self,vals):
        ret = super(DonationpointsVisit, self).create(vals)
        self.env['donationpoints.donationbox'].search([('id', '=', vals['donationbox_id'])]).write({'condition_id':vals['condition_id']})
        return ret
