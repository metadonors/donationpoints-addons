# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsDonationbox(models.Model):

    _name = "donationpoints.donationbox"
    _description = "Donationpoints Donationbox"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string=_("Name"), required=True)

    description = fields.Text(string=_("Description"))

    code = fields.Char(string=_("Serial Code"))

    theme_id = fields.Many2one("donationpoints.donationbox.theme", string=_("Theme"))

    type_id = fields.Many2one("donationpoints.donationbox.type", string=_("Type"))

    location_id = fields.Many2one("donationpoints.location", string=_("Location"))

    theme_id = fields.Many2one("donationpoints.donationbox.theme", string=_("Theme"))

    history_ids = fields.One2many(
        "donationpoints.visit", "donationbox_id", string=_("Visits"), readonly=True
    )

    condition_id = fields.Many2one(
        "donationpoints.donationbox.condition", string=_("Conditions")
    )

    note = fields.Text(string=_("Notes"))
