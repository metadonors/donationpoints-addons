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

    code = fields.Char(string=_("Code"), readonly=True)
    active = fields.Boolean(string=_("Active"), default=True)
    visit_date = fields.Date(default=lambda s: fields.Date.context_today(s))
    visit_type_id = fields.Many2one("donationpoints.visit.type", string=_("Type"))
    date_deadline = fields.Date()
    user_id = fields.Many2one(
        "res.users", string=_("User"), required=True, default=lambda self: self.env.uid,
    )
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


    def _prepare_donation_vals(self):
        return {
                    "donationpoint_id": self.donationpoint_id.id,
                    "location_id": self.location_id.id,
                    "date": self.visit_date,
                    "amount": self.amount,
                    "donation_type": "cash",
                    "visit_id": self.id,
                }

    @api.multi
    def write(self, vals):
        ret = super(DonationpointsVisit, self).write(vals)

        for record in self:
            if vals.get("condition_id", False):
                record.donationpoint_id.donationbox_id.write(
                    {"condition_id": vals["condition_id"]}
                )

            if vals.get("amount", False) and vals["amount"] > 0:
                existing_donation_id = self.env["donationpoints.donation"].search(
                    [("visit_id", "=", record.id)]
                )
                if existing_donation_id:
                    existing_donation_id.write({"amount": vals["amount"]})
                else:
                    vals = record._prepare_donation_vals()
                    self.env["donationpoints.donation"].create(vals)

        return ret

    @api.one
    def _get_current_login_user(self):
        user_obj = self.env["res.users"].search([])
        for user_login in user_obj:
            current_login = self.env.user
            if user_login == current_login:
                self.processing_staff = current_login
            return

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
            vals = ret._prepare_donation_vals()
            self.env["donationpoints.donation"].create(vals)

        return ret
