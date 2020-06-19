# Copyright 2019 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from .donationpoints_settings import PAYMENT_MODE_ID_CONF, JOURNAL_ID_CONF

class DonationpointsDonation(models.Model):

    _inherit = 'donationpoints.donation'

    campaign_id = fields.Many2one(
        'ngo.campaign',
        string=_("Campaign"),
        required=True
    )

    ngo_donation_id = fields.Many2one(
        'ngo.donation',
        string=_("Fundraising donation")
    )

    def _prepare_ngo_donation_vals(self):
        vals = {}
        vals['amount'] = self.amount
        vals['campaign_id'] = self.campaign_id.id

        payment_mode_id = self.env['ir.config_parameter'].get_param(PAYMENT_MODE_ID_CONF, None)
        journal_id = self.env['ir.config_parameter'].get_param(JOURNAL_ID_CONF, None)

        if not payment_mode_id or not journal_id:
            raise UserError(_("You must specify default payment mode and journal for donations  in settings"))

        vals['payment_mode_id'] = int(payment_mode_id)
        vals['journal_id'] = int(journal_id)
        vals['donationpoint_id'] = self.donationpoint_id.id
        vals['date_credit'] = self.date
        vals['date_done'] = self.date
        vals['is_anonymous'] = True

        return vals

    @api.model
    def create(self, vals):
        record = super(DonationpointsDonation, self).create(vals)

        donation_vals = record._prepare_ngo_donation_vals()
        donation_id = self.env['ngo.donation'].create(donation_vals)

        record.write({ 'ngo_donation_id': donation_id.id })

        return record