# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from datetime import datetime


class Donationpointsdonationbox_theme(models.Model):

    _name = "donationpoints.donationbox.theme"
    _description = "Donationpoints Donationbox Theme"  # TODO

    name = fields.Char(string=_("Name"))
