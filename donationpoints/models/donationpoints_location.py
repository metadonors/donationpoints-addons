# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class DonationpointsLocation(models.Model):

    _name = 'donationpoints.location'
    _description = 'Donationpoints Location'  # TODO
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string=_('Name'))
    address1 = fields.Char(string=_('Address'))
    address2 = fields.Char(string=_('Address 2'))
    city = fields.Char(string=_('City'))
    country_state_id = fields.Many2one('res.country.state',string=_('Province'))
    country_id = fields.Many2one('res.country',string=_('Country'))
    phone = fields.Char(string=_('Phone'))
    mobile = fields.Char(string=_('Mobile'))
    email = fields.Char(string=_('Email'))
    location_type_id = fields.Many2one('donationpoints.location.type',string=_('Type'))
    owner_partner_id = fields.Many2one('res.partner',string=_('Owner')) #Proprietario negozio
    owner_partner_email_id = fields.Char(string=_('Owner Email'), related='owner_partner_id.email')
    owner_partner_phone_id = fields.Char(string=_('Owner Phone'), related='owner_partner_id.phone')
    owner_partner_mobile_id = fields.Char(string=_('Owner Mobile'), related='owner_partner_id.mobile')
    contact_partner_id = fields.Many2one('res.partner',string=_('Contact')) #Contatto per il negozio
    contact_partner_email_id = fields.Char(string=_('Contact Email'), related='contact_partner_id.email')
    contact_partner_phone_id = fields.Char(string=_('Contact Phone'), related='contact_partner_id.phone')
    contact_partner_mobile_id = fields.Char(string=_('Contact Mobile'), related='contact_partner_id.mobile')
    note = fields.Text(string=_('Note'))