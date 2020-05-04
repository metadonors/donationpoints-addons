# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import logging
log = logging.getLogger(__name__)


class Donationpoint(models.Model):

    _name = 'donationpoints.donationpoint'
    _description = 'Donationpoints Donationpoint'

    name = fields.Char(string=_("Name"))
    location_id = fields.Many2one('donationpoints.location', string=_('Location'))
    location_owner_id = fields.Many2one(string=_('Owner'), related=('location_id.owner_partner_id'), store=True, readonly=True)
    donationbox_id = fields.Many2one('donationpoints.donationbox', string=_('Donationbox'))
    donationbox_theme_id = fields.Many2one('donationpoints.donationbox.theme', string=_("Donation Box Theme"), readonly=True)
    activity_state = fields.Selection([('active',_('Active')),
                                       ('suspended',_('Suspended')),
                                       ('closed',_('Closed'))],
                                        default='active',
                                       string=_('Activity State'))
    note = fields.Text(string=_('Note'))


    @api.onchange('donationbox_id')
    def donationbox_theme(self):
        for record in self:
            if record.donationbox_id:
                record.donationbox_theme_id = record.donationbox_id.id

    @api.model
    def write(self,vals):
        ret = super(Donationpoint, self).write(vals)
        vals['donationbox_id'].write({'location_id':vals['location_id']})
        return ret

    @api.model
    def create(self,vals):
        ret = super(Donationpoint, self).create(vals)
        self.env['donationpoints.donationbox'].search([('id', '=', vals['donationbox_id'])]).write({'location_id':vals['location_id']})
        return ret




