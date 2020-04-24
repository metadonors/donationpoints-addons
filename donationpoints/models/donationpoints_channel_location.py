# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsChannelLocation(models.Model):

    _name = 'donationpoints.channel.location'
    _description = 'Donationpoints Channel Location'  # TODO

    #code = fields.Char(string=_("Code"))
    channel_id = fields.Many2one('donationpoints.channel', string=_('Channel'))
    location_id = fields.Many2one('donationpoints.location', string=_('Location'))
    location_owner_id = fields.Many2one(string=_('Owner'), related=('location_id.owner_partner_id'), readonly=True) #AUTOMATICO??
    donationbox_id = fields.Many2one('donationpoints.donationbox', string=_('Donationbox'), domain=[("location_id","=",location_id)])
    activity_state = fields.Selection([('active',_('Active')),
                                       ('suspended',_('Suspended')),
                                       ('closed',_('Closed')),
                                       ('retired',_('Retired')),
                                       ('denied',_('Denied'))],
                                       string=_('Activity State'))
    start_date = fields.Date(string=_('Start Date'))
    end_date = fields.Date(string=_('End Date'))
    # contact_history Many2Many donationpoints.contact_history # Queste diventano note/appuntamenti sulle location
    contact_result = fields.Text(string=_('Contact Result'))
    note = fields.Text(string=_('Note'))

    #@api.model
    #def create(self, vals):
    #    if vals.get("code", "REL") == "REL":
    #        vals["code"] = self.env["ir.sequence"].next_by_code("donationpoints.channel.location") or "REL"
    #        record = super(DonationpointsChannelLocation, self).create(vals)
    #        return record
