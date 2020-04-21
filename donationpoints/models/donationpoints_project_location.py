# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsChannelLocation(models.Model):

    _name = 'donationpoints.channel.location'
    _description = 'Donationpoints Channel Location'  # TODO

    channel_id = fields.Many2one('donationpoints.channel', string=_('Channel'))
    location_id = fields.Many2one('donationpoints.location', string=_('Location'))
    location_owner_id = fields.Many2one('donationpoints.location', string=_('Owner'), related=('location_id.owner_partner_id'), readonly=True) #AUTOMATICO??
    activity_state = fields.Slections([('active',_('Active')),
                                       ('suspended',_('Suspended')),
                                       ('closed',_('Closed')),
                                       ('retired',_('Retired')),
                                       ('denied',_('Denied'))],
                                       string=_('Activity State'))
    start_date = fields.Datetime(string=_('Start Date'))
    end_date = fields.Datetime(string=_('End Date'))
    # contact_history Many2Many donationpoint.contact_history # Queste diventano note/appuntamenti sulle location
    contact_result = fields.Text(string=_('Contact Result'))
    note = fields.Text(string=_('Note'))


