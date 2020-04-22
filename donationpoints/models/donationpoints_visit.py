# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsVisit(models.Model):

    _name = 'donationpoints.visit'
    _description = 'Donationpoints Visit'  # TODO

    visit_date = fields.Date(string=_("Visit Date"))
    visit_type_id = fields.Many2one('donationpoints.visit.type', string=_('Type'))
    channel_id = fields.Many2one('donationpoints.channel', string=_('Channel'))
    user_id = fields.Many2one('res.users', string=_('User'))
    donationbox_id = fields.Many2one('donationpoints.donationbox', string=_('Donation Box'))
    condition_id = fields.Many2one('donationpoints.donationbox.condition', string=_('Condition'), related='donationbox_id.condition_id.name', store=True) #store=salvabile
    location_id = fields.Many2one('donationpoints.donationbox.location', string=_('Location'), related='donationbox_id.location_id')
    amount = fields.Monetary(string=_('Amount')) #visibile sulla view in base alla donationbox_id.type (visibile solo per dispositivi manuali)
    name = fields.Char()

