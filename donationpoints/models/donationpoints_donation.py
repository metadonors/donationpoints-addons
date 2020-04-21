# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsDonation(models.Model):

    _name = 'donationpoints.donation'
    _description = 'Donationpoints Donation'
    _inherit = 'mail.thread'

    #name = fields.Char(string=_('Name'))
    code = fields.Char(string=_('Code'),readonly=True, required=True, copy=False, default='Don')
    channel_id = fields.Many2one('donationpoints.channel', string=_('Channel'))
    location_id = fields.Many2one('donationpoints.donationbox.location', string=_('Location'))
    location_owner_id = fields.Many2one('donationpoints.location', string=_('Owner'), related=('location_id.owner_partner_id'), readonly=True)
    date = fields.DateField(string=_("Date")) #Data di elaborazione della donazione
    amount = fields.monetary(string=_('Amount'))

    @api.model
    def create(self, vals):
        if vals.get("code", "Don") == "Don":
            vals["code"] = self.env["ir.sequence"].next_by_code("donationpoints.donation") or "Don"
            record = super(DonationpointsDonation, self).create(vals)
            return record