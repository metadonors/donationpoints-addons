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

        log.error('-------write----')
        log.error('-------write----')
        log.error('-------write----')
        log.error(vals)
        if vals.get('condition_id', False):
            vals.donationpoint_id.donationbox_id.condition_id.write({'condition_id':vals.condition_id.id})

        if vals["amount"] and vals["amount"] > 0:
            existing_donation_id = self.env["donationpoints.donation"].search(
                [("visit_id", "=", self.id)]
            )
            if existing_donation_id:
                existing_donation_id.write({"amount": vals['amount']})
        return ret

    @api.model
    def create(self, vals):
        ret = super(DonationpointsVisit, self).create(vals)

        log.error('^^^^^^^^^^^^^^^^^^^^^^^')
        log.error('^^^^^^^^^^^^^^^^^^^^^^^')
        log.error('^^^^^^^^^^^^^^^^^^^^^^^')
        log.error('^^^^^^^^^^^^^^^^^^^^^^^')
        log.error(vals)
        log.error(ret)
        if ret.condition_id:
            ret.donationpoint_id.donationbox_id.condition_id.write({'condition_id':ret.condition_id.id})
        self.env["donationpoints.donation"].create(
            {
                "donationpoint_id": ret.donationpoint_id.id,
                "location_id": ret.location_id.id,
                "date": ret.visit_date,
                "amount": ret.amount,
                "user_id": ret.user_id.id,
                "donation_type": "cash",
                "visit_id": ret.id,
            }
        )
        return ret
