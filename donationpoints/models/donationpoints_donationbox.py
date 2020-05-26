# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsDonationbox(models.Model):

    _name = "donationpoints.donationbox"
    _description = "Donationpoints Donationbox"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string=_("Name"), required=True)

    active = fields.Boolean(string=_("Active"), default=True)
    donation_count = fields.Integer(string=_('Total donation'), compute='_compute_total_donation')

    description = fields.Text(string=_("Description"))

    code = fields.Char(string=_("Serial Code"))

    theme_id = fields.Many2one("donationpoints.donationbox.theme", string=_("Theme"))

    type_id = fields.Many2one("donationpoints.donationbox.type", string=_("Type"))

    location_id = fields.Many2one(
        "donationpoints.location", string=_("Location"), readonly=True
    )

    theme_id = fields.Many2one("donationpoints.donationbox.theme", string=_("Theme"))

    history_ids = fields.One2many(
        "donationpoints.visit", "donationbox_id", string=_("Visits"), readonly=True
    )

    condition_id = fields.Many2one(
        "donationpoints.donationbox.condition", string=_("Conditions")
    )
    note = fields.Text(string=_("Notes"))

    note = fields.Text(string=_("Notes"))

    #TODO
    def _compute_total_donation(self):
        return 100

    #TODO
    @api.multi
    def action_donation(self):
        pass

#        return {
#            'name':'Donationbox Donations',
#            'type':'ir.actions.act_window',
#            'res_model':'agreements.agreements',
#            'view_mode':'tree,form',
#            'res_id':False,
#            'domain': [(
#                'id', 'in', self
#            )],
#            'target':'current',
#            'context': {
#                'default_donataionpoint_id': self.donation_point.id
#            }
#        }
#

