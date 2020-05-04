# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import logging
log = logging.getLogger(__name__)

class DonationpointsVisit(models.Model):

    _name = 'donationpoints.visit'
    _description = 'Donationpoints Visit'

    visit_date = fields.Date(string=_("Visit Date"), required=True)
    visit_type_id = fields.Many2one('donationpoints.visit.type', string=_('Type'))
    user_id = fields.Many2one('res.users', string=_('User'), required=True)
    donationbox_id = fields.Many2one('donationpoints.donationbox', string=_('Donation Box'), required=True)
    condition_id = fields.Many2one('donationpoints.donationbox.condition', string=_('Condition'), store=True)
    is_device = fields.Boolean(string=_("The donation box is a device"))
    location_id = fields.Many2one('donationpoints.location', string=_('Location'), store=True, required=True)
    amount = fields.Monetary(currency_field='currency_id', string=_('Amount'), store=True)
    currency_id = fields.Many2one('res.currency', 'Currency', readonly=True)
    note = fields.Text(string=_("Note"))


    @api.onchange('donationbox_id')
    def _donationbox_condition_state(self):
        for record in self:
            if record.donationbox_id:
                record.condition_id = record.donationbox_id.condition_id
                record.is_device = True if record.donationbox_id.type_id.model_type == 'device' else False

    @api.multi
    def write(self,vals):
        ret = super(DonationpointsVisit, self).write(vals)
        if vals.get('condition_id', False):
            vals['donationbox_id'].write({'condition_id':vals['condition_id']})
        if vals.get('amount', False) and vals['amount'] > 0:
            self.create_donation()
        return ret

    @api.model
    def create(self,vals):
        ret = super(DonationpointsVisit, self).create(vals)
        self.env['donationpoints.donationbox'].search([('id', '=', vals['donationbox_id'])]).write({'condition_id':vals['condition_id']})
        if vals.get('amount', False) and vals['amount'] > 0:
            self.create_donation

        return ret

    def create_donation(self):
        for record in self:
            donationpoint = self.env['donationpoints.donationpoint'].search([('location_id', '=', record.location_id.id), ('donationbox_id','=',record.donationbox_id.id)])
            if not donationpoint:
                raise ValidationError('Donation Point not found')

            self.env['donationpoints.donation'].create({
                'donationpoint_id': donationpoint.id,
                'location_id': record.location_id.id,
                'date': record.visit_date,
                'amount': record.amount,
                'user_id': record.user_id.id,
            })

