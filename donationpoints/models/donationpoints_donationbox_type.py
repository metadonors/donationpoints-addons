# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsDonationboxType(models.Model):

    _name = 'donationpoints.donationbox.type'
    _description = 'Donationpoints Donationbox Type'  # TODO

    name = fields.Char(string=_('Name'))
    model_type = fields.Selection([('manual', _('Manual')),('device',_('Device'))],string=_('Model Type'), default='manual')
