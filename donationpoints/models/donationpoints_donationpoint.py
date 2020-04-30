# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError 
import logging
log = logging.getLogger(__name__)


class DonationpointsChannelLocation(models.Model):

    _name = 'donationpoints.donationpoint'
    _description = 'Donationpoints Donationpoint'  # TODO

    name = fields.Char(string=_("Name"))
    #channel_id = fields.Many2one('donationpoints.channel', string=_('Channel'))
    location_id = fields.Many2one('donationpoints.location', string=_('Location'))
    location_owner_id = fields.Many2one(string=_('Owner'), related=('location_id.owner_partner_id'), store=True, readonly=True) #AUTOMATICO??
    donationbox_id = fields.Many2one('donationpoints.donationbox', string=_('Donationbox'))
    activity_state = fields.Selection([('active',_('Active')),
                                       ('suspended',_('Suspended')),
                                       ('closed',_('Closed'))],
                                       string=_('Activity State'))
    #start_date = fields.Date(string=_('Start Date'))
    #end_date = fields.Date(string=_('End Date'))
    # contact_history Many2Many donationpoints.contact_history # Queste diventano note/appuntamenti sulle location
    note = fields.Text(string=_('Note'))

        

