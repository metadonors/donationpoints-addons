# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsVisitType(models.Model):

    _name = "donationpoints.visit.type"
    _description = "Donationpoints Visit Type"  # TODO

    name = fields.Char(string=_("Name"))
