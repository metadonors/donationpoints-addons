# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsDonationboxCondition(models.Model):

    _name = "donationpoints.donationbox.condition"
    _description = "Donationpoints Donationbox Condition"  # TODO

    name = fields.Char(string=_("Name"))
