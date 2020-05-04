# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsDonation(models.Model):

    _name = 'donationpoints.donation'
    _description = 'Donationpoints Donation'
    _inherit = 'mail.thread'

    code = fields.Char(string=_('Code'),readonly=True)
    donationpoint_id = fields.Many2one('donationpoints.donationpoint', string=_('Channel'))
    location_id = fields.Many2one('donationpoints.location', string=_('Location'))
    user_id = fields.Many2one('res.users', string=_('Responsable'))
    date = fields.Date(string=_("Donation Date")) #Data di elaborazione della donazione
    amount = fields.Monetary(currency_field='currency_id', string=_('Amount'))
    currency_id = fields.Many2one('res.currency', 'Currency', required=True, readonly=True)

    @api.model
    def create(self, vals):
        if vals.get("code", "Don") == "Don":
            vals["code"] = self.env["ir.sequence"].next_by_code("donationpoints.donation") or "Don"
            record = super(DonationpointsDonation, self).create(vals)
            return record
