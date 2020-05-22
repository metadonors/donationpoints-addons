# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsLocationType(models.Model):

    _name = "donationpoints.location.type"
    _description = "Donationpoints Location Type"  # TODO

    name = fields.Char(string=_("Name"))
