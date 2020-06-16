# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
import logging

log = logging.getLogger(__name__)


class DonationpointsDonationbox(models.Model):

    _name = "donationpoints.donationbox"
    _description = "Donationpoints Donationbox"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string=_("Name"),
        default=lambda self: self.env["ir.sequence"].next_by_code(
            "donationpoints.donationbox.sequence"
        ),
    )
    active = fields.Boolean(string=_("Active"), default=True)
    donation_amount = fields.Float(
        string=_("Total donation"), compute="_compute_total_donation",
    )
    description = fields.Text(string=_("Description"))
    serial_code = fields.Char(string=_("Serial Code"))
    theme_id = fields.Many2one("donationpoints.donationbox.theme", string=_("Theme"))
    type_id = fields.Many2one("donationpoints.donationbox.type", string=_("Type"))
    location_id = fields.Many2one(
        "donationpoints.location", string=_("Location"), readonly=True
    )
    history_ids = fields.One2many(
        "donationpoints.visit", "donationbox_id", string=_("Visits"), readonly=True
    )
    condition_id = fields.Many2one(
        "donationpoints.donationbox.condition",
        string=_("Conditions"),
        default=lambda self: self.env["donationpoints.donationbox.condition"].browse(1),
    )
    note = fields.Text(string=_("Notes"))

    def _compute_total_donation(self):
        total_donations = self.env["donationpoints.donation"].search(
            [("donationpoint_id.donationbox_id", "=", self.id)]
        )
        total_amount = 0
        for donation_id in total_donations:
            total_amount += donation_id.amount
        self.donation_amount = total_amount

    @api.multi
    def action_donation(self):
        return {
            "name": "Donationbox Donations",
            "type": "ir.actions.act_window",
            "res_model": "donationpoints.donation",
            "view_mode": "tree",
            "res_id": False,  # used for Form View and pass fields value
            "domain": [("donationpoint_id.donationbox_id", "=", self.id)],
            "target": "current",
            # "context": {"default_donataionpoint_id": self.donation_point.id},
        }
