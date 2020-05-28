# Copyright 2020 Metadonors Srl

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import logging

log = logging.getLogger(__name__)


class DonationpointsVisit(models.Model):

    _name = "donationpoints.visit"
    _description = "Donationpoints Visit"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "code"
    _order = "visit_date DESC"

    name = fields.Char(string=_("Code"), readonly=True)
    active = fields.Boolean(string=_("Active"), default=True)
    visit_date = fields.Date(string=_("Visit Date"), required=True)
    visit_type_id = fields.Many2one("donationpoints.visit.type", string=_("Type"))
    user_id = fields.Many2one("res.users", string=_("User"), required=True)
    donationpoint_id = fields.Many2one(
        "donationpoints.donationpoint", string=_("Donation Point"), required=True
    )
    # donationbox_id related to one2many donationbox.history
    donationbox_id = fields.Many2one(
        "donationpoints.donationbox", related="donationpoint_id.donationbox_id"
    )
    condition_id = fields.Many2one(
        "donationpoints.donationbox.condition",
        string=_("Donationbox Condition"),
        store=True,
    )
    is_device = fields.Boolean(string=_("The donation box is a device"))
    location_id = fields.Many2one(
        "donationpoints.location", related="donationpoint_id.location_id",
    )
    amount = fields.Float(string=_("Amount"), store=True)

    note = fields.Text(string=_("Note"))

    @api.onchange("donationpoint_id")
    def _donationbox_condition_state(self):
        for record in self:
            record.condition_id = record.donationpoint_id.donationbox_id.condition_id
            record.is_device = (
                True
                if record.donationpoint_id.donationbox_id.type_id.model_type == "device"
                else False
            )

    @api.multi
    def write(self, vals):
        ret = super(DonationpointsVisit, self).write(vals)

        if vals.get("condition_id", False):
            self.donationpoint_id.donationbox_id.write(
                {"condition_id": vals["condition_id"]}
            )

        if vals.get("amount", False) and vals["amount"] > 0:
            existing_donation_id = self.env["donationpoints.donation"].search(
                [("visit_id", "=", self.id)]
            )
            if existing_donation_id:
                existing_donation_id.write({"amount": vals["amount"]})
            else:
                self.env["donationpoints.donation"].create(
                    {
                        "donationpoint_id": self.donationpoint_id.id,
                        "location_id": self.location_id.id,
                        "date": self.visit_date,
                        "amount": self.amount,
                        # "user_id": self.user_id.id,
                        "donation_type": "cash",
                        "visit_id": self.id,
                    }
                )
        return ret

    @api.model
    def create(self, vals):
        if not vals.get("code"):
            vals["code"] = self.env["ir.sequence"].next_by_code(
                "donationpoints.visit.sequence"
            )

        ret = super(DonationpointsVisit, self).create(vals)

        if ret.condition_id:
            ret.donationpoint_id.donationbox_id.write(
                {"condition_id": ret.condition_id.id}
            )
        if ret.amount > 0:
            self.env["donationpoints.donation"].create(
                {
                    "donationpoint_id": ret.donationpoint_id.id,
                    "location_id": ret.location_id.id,
                    "date": ret.visit_date,
                    "amount": ret.amount,
                    # "user_id": ret.user_id.id,
                    "donation_type": "cash",
                    "visit_id": ret.id,
                }
            )

        return ret
