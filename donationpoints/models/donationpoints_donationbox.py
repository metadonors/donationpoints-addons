# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsDonationbox(models.Model):

    _name = 'donationpoints.donationbox'
    _description = 'Donationpoints Donationbox'  # TODO
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string=_('Name'), required=True)
    description = fields.Text(string=_('Description'))
    code = fields.Char(string=_('Serial Code'))
    type_id = fields.Many2one('donationpoints.donationbox.donationboxtype', string=_('Type'))
    location_id = fields.Many2one('donationpoints.donationbox.location', string=_('Location'))
    history_ids = fields.One2many('donationpoints.donationbox.visit', 'donationbox_id', string=_('Visits'))
    condition_id = fields.Many2one('donationpoints.donationbox.condition',
                                    string=_("Conditions"))
    note = fields.Text(string=_('Notes'))

