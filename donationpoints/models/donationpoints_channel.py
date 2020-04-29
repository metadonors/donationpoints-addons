# Copyright 2020 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from datetime import datetime

class DonationpointsChannel(models.Model):

    _name = 'donationpoints.channel'
    _description = 'Donationpoints Channel'  # TODO

    name = fields.Char(string=_('Channel'))
    description = fields.Char(string=_('Description'))
    user_id = fields.Many2one('res.users', string=_('Responsible')) # follower
    state = fields.Selection([('active',_('Active')),
                              ('suspended',_('Suspended')),
                              ('cancelled',_('Cancelled')),
                              ('closed',_('Closed'))],string=_('State'),default='active')
    start_date = fields.Date(string=_('Start Date'))
    end_date = fields.Date(string=_('End Date'))
    note = fields.Text(string=_('Note'))

    @api.onchange('end_date')    
    def check_expitation_date(self):
        today = datetime.today()
        for record in self:
            if record.end_date and record.end_date < today:
                record.state = 'closed'
            else:
                record.state = 'active'





    