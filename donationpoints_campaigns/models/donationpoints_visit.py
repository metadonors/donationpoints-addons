# Copyright 2019 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsVisit(models.Model):

    _inherit = 'donationpoints.visit'

    def _prepare_donation_vals(self):
        vals = super(DonationpointsVisit, self)._prepare_donation_vals()
        vals['campaign_id'] = self.donationpoint_id.campaign_id.id
        return vals
