# Copyright 2019 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class NgoDonation(models.Model):

    _inherit = 'ngo.donation'

    donationpoint_id = fields.Many2one(
        'donationpoints.donationpoint',
        string=_("Donation Point")
    )