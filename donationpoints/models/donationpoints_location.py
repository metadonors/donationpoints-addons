# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from datetime import datetime


class DonationpointsLocation(models.Model):

    _name = "donationpoints.location"
    _description = "Donationpoints Location"  # TODO
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string=_("Name"), required=True)
    active = fields.Boolean(string=_("Active"), default=True)
    address1 = fields.Char(string=_("Address"))
    phone = fields.Char(string=_("Phone"))
    email = fields.Char(string=_("Email"))
    city = fields.Char(string=_("City"))
    postal_code = fields.Char(string=_("Postal Code"))
    country_state_id = fields.Many2one("res.country.state", string=_("Province"))
    country_id = fields.Many2one("res.country", string=_("Country"))
    location_type_id = fields.Many2one(
        "donationpoints.location.type", string=_("Type"), required=True
    )
    owner_partner_id = fields.Many2one(
        "res.partner", string=_("Owner")
    )  # Proprietario negozio
    owner_partner_email_id = fields.Char(
        string=_("Owner Email"), related="owner_partner_id.email"
    )
    owner_partner_phone_id = fields.Char(
        string=_("Owner Phone"), related="owner_partner_id.phone"
    )
    owner_partner_mobile_id = fields.Char(
        string=_("Owner Mobile"), related="owner_partner_id.mobile"
    )
    responsable_partner_id = fields.Many2one(
        "res.partner", string=_("Responsable")
    )  # Contatto per il negozio
    responsable_partner_email_id = fields.Char(
        string=_("Responsable Email"), related="responsable_partner_id.email"
    )
    responsable_partner_phone_id = fields.Char(
        string=_("Responsable Phone"), related="responsable_partner_id.phone"
    )
    responsable_partner_mobile_id = fields.Char(
        string=_("Responsable Mobile"), related="responsable_partner_id.mobile"
    )
    note = fields.Text(string=_("Note"))

    donation_amount = fields.Float(
        string=_("Total donation"), compute="_compute_total_donation",
    )
    activation_date = fields.Date(string=_('Activation Date'), default=datetime.now().date())

    visits_count = fields.Integer(
        string=_("Visit Count"), compute="_compute_visit_count"
    )

    def _compute_visit_count(self):
        total_visits = self.env["donationpoints.visit"].search(
            [("location_id", "=", self.id)]
        )
        self.visits_count = len(total_visits)

    def _compute_total_donation(self):
        total_donations = self.env["donationpoints.donation"].search(
            [("location_id", "=", self.id)]
        )
        total_amount = 0
        for donation_id in total_donations:
            total_amount += donation_id.amount
        self.donation_amount = total_amount

    @api.multi
    def action_donation(self):
        return {
            "name": "Location Donations",
            "type": "ir.actions.act_window",
            "res_model": "donationpoints.donation",
            "view_mode": "tree",
            "res_id": False,  # used for Form View and pass fields value
            "domain": [("donationpoint_id.location_id", "=", self.id)],
            "target": "current",
            # "context": {"default_donataionpoint_id": self.donation_point.id},
        }

    @api.multi
    def action_visit(self):
        return {
            "name": "Location Visit",
            "type": "ir.actions.act_window",
            "res_model": "donationpoints.visit",
            "view_mode": "tree",
            "res_id": False,  # used for Form View and pass fields value
            "domain": [("location_id", "=", self.id)],
            "target": "current",
            # "context": {"default_donataionpoint_id": self.donation_point.id},
        }
