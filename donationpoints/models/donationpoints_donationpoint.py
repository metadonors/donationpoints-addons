# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime
import logging

log = logging.getLogger(__name__)


class Donationpoint(models.Model):

    _name = "donationpoints.donationpoint"
    _description = "Donationpoints Donationpoint"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string=_("Name"))
    code = fields.Char(string=_("Code"))
    date_deadline = fields.Date(default=lambda s: fields.Date.context_today(s))

    active = fields.Boolean(string=_("Active"), default=True)

    location_id = fields.Many2one(
        "donationpoints.location", string=_("Location"), required=True
    )

    address1 = fields.Char(string=_("Address"), related="location_id.address1", store=True)
    phone = fields.Char(string=_("Phone"), related="location_id.phone", store=True)
    email = fields.Char(string=_("Email"), related="location_id.email", store=True)
    city = fields.Char(string=_("City"), related="location_id.city", store=True)
    postal_code = fields.Char(string=_("Postal Code"), related="location_id.postal_code", store=True)
    country_state_id = fields.Many2one("res.country.state", string=_("Province"), related="location_id.country_state_id", store=True)
    country_id = fields.Many2one("res.country", string=_("Country"), related="location_id.country_id", store=True)

    location_owner_id = fields.Many2one(
        string=_("Owner"),
        related=("location_id.owner_partner_id"),
        store=True,
        readonly=True,
    )

    donationbox_id = fields.Many2one(
        "donationpoints.donationbox", string=_("Donation Box"), required=True
    )

    donationbox_theme_id = fields.Many2one(
        "donationpoints.donationbox.theme",
        related="donationbox_id.theme_id",
        string=_("Donation Box Theme"),
        readonly=True,
    )

    state = fields.Selection(
        selection=[
            ("active", _("Active")),
            ("suspended", _("Suspended")),
            ("closed", _("Closed")),
        ],
        string=_("Activity State"),
        default="active",
    )

    start_date = fields.Date(string_="Date start")
    end_date = fields.Date(string_="Date end")
    note = fields.Text(string=_("Note"))

    donation_amount = fields.Float(
        string=_("Total donation"), compute="_compute_total_donation",
    )

    visits_count = fields.Integer(
        string=_("Visit Count"), compute="_compute_visit_count"
    )

    visit_ids = fields.One2many(
        "donationpoints.visit", "donationpoint_id", string=_("Vists")
    )



    @api.onchange("location_id")
    def create_donationpoint_name(self):
        if self.location_id:
            name = self.location_id.name
            if self.location_id.location_type_id and self.location_id.location_type_id.name:
                name = "{} - {}".format(name, self.location_id.location_type_id.name)

            if self.location_id.owner_partner_id and self.location_id.owner_partner_id.name:
                name = "{} - {}".format(name, self.location_id.owner_partner_id.name)

            self.name = name
        else:
            self.name = False

    @api.onchange("state")
    def _calculate_date(self):
        if self.state == "active":
            self.start_date = datetime.now().date()
            self.end_date = False
        elif self.state == "closed":
            self.end_date = datetime.now().date()

    def _compute_visit_count(self):
        for record in self:
            total_visits = self.env["donationpoints.visit"].search(
                [("donationpoint_id", "=", record.id)]
            )
            record.visits_count = len(total_visits)

    def _compute_total_donation(self):
        for record in self:
            total_donations = self.env["donationpoints.donation"].search(
                [("donationpoint_id", "=", record.id)]
            )
            total_amount = 0
            for donation_id in total_donations:
                total_amount += donation_id.amount
            record.donation_amount = total_amount

    @api.multi
    def action_donation(self):
        return {
            "name": "Donationpoint Donations",
            "type": "ir.actions.act_window",
            "res_model": "donationpoints.donation",
            "view_mode": "tree",
            "res_id": False,  # used for Form View and pass fields value
            "domain": [("donationpoint_id", "=", self.id)],
            "target": "current",
            # "context": {"default_donataionpoint_id": self.donation_point.id},
        }

    @api.multi
    def action_visit(self):
        return {
            "name": "Donationpoint Visit",
            "type": "ir.actions.act_window",
            "res_model": "donationpoints.visit",
            "view_mode": "tree",
            "res_id": False,  # used for Form View and pass fields value
            "domain": [("location_id", "=", self.id)],
            "target": "current",
            # "context": {"default_donataionpoint_id": self.donation_point.id},
        }

    @api.multi
    def write(self, vals):
        ret = super(Donationpoint, self).write(vals)
        if vals.get("location_id", False):
            for record in self:
                self.env["donationpoints.donationbox"].search(
                    [("id", "=", record.donationbox_id.id)]
                ).write({"location_id": vals["location_id"]})

        return ret

    @api.model
    def create(self, vals):
        if not vals.get("code"):
            vals["code"] = self.env["ir.sequence"].next_by_code(
                "donationpoints.donationpoint.sequence"
            )

        if not vals.get("name"):
            location_id = self.env['donationpoints.location'].browse(vals['location_id'])
            vals['name'] = location_id.name
            if location_id.location_type_id and location_id.location_type_id.name:
                vals['name'] = "{} - {}".format(vals['name'], location_id.location_type_id.name)

            if location_id.owner_partner_id and location_id.owner_partner_id.name:
                vals['name'] = "{} - {}".format(vals['name'], location_id.owner_partner_id.name)

        if vals.get("donationbox_id", False) and self.env[
            "donationpoints.donationpoint"
        ].search([("donationbox_id", "=", vals["donationbox_id"])]):
            raise ValidationError(
                _("This Donationbox is already present on another donationpoint")
            )

        ret = super(Donationpoint, self).create(vals)
        self.env["donationpoints.donationbox"].search([("id", "=", vals["donationbox_id"])]).write({"location_id": vals["location_id"]})
        return ret

    def action_create_visit(self):
        return {
            "name": "Create Donationbox Visit",
            "type": "ir.actions.act_window",
            "res_model": "donationpoints.visit",
            "view_mode": "form",
            "res_id": False,  # used for Form View and pass fields value
            "target": "current",
            "context": {
                "default_donationpoint_id": self.id,
                "visit_date":self.date_deadline
            },
        }
