# Copyright 2019 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsDonationpoint(models.Model):

    _inherit = 'donationpoints.donationpoint'

    campaign_id = fields.Many2one(
        'ngo.campaign',
        string=_("Campaign"),
        required=True
    )
