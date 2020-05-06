# Copyright 2020 Metadonors Srl

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import logging

log = logging.getLogger(__name__)


class DonationpointsVisit(models.Model):

    _name = "donationpoints.visit"
    _description = "Donationpoints Visit"

    visit_date = fields.Date(string=_("Visit Date"), required=True)
    visit_type_id = fields.Many2one("donationpoints.visit.type", string=_("Type"))
    user_id = fields.Many2one("res.users", string=_("User"), required=True)
    donationpoint_id = fields.Many2one(
        "donationpoints.donationpoint", string=_("Donation Point"), required=True
    )
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
        "donationpoints.location", string=_("Location"), store=True, required=True
    )
    amount = fields.Monetary(
        currency_field="currency_id", string=_("Amount"), store=True
    )
    currency_id = fields.Many2one("res.currency", "Currency", readonly=True)
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
        self.create_donation(vals)
        return ret

    @api.model
    def create(self, vals):
        ret = super(DonationpointsVisit, self).create(vals)
        self.create_donation(vals)

        return ret

    def create_donation(self, vals):
        # Modifica lo stato della donationbox
        # crea la donazione
        for record in self:
            if (
                vals.get("condition_id", False)
                and vals["condition_id"] != record.condition_id
            ):
                self.env["donationpoints.donationbox"].search(
                    [("id", "=", record.donationbox_id)]
                ).write({"condition_id": vals["condition_id"]})

            if record.amount > 0:
                self.env["donationpoints.donation"].create(
                    {
                        "donationpoint_id": record.donationpoint_id.id,
                        "location_id": record.location_id.id,
                        "date": record.visit_date,
                        "amount": record.amount,
                        "user_id": record.user_id,
                        "donation_type": "cash",
                    }
                )
