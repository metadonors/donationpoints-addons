# Copyright 2019 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class DonationpointsImportWizard(models.TransientModel):

    _inherit = 'donationpoints.import.wizard'

    def _prepare_donationpoint_vals(self, data, location_id, dbox_id):
        vals = super(DonationpointsImportWizard, self)._prepare_donationpoint_vals(data, location_id, dbox_id)

        campaign_ids = self.env['ngo.campaign'].search([
            ('name', '=', data['CAMPAGNA'])
        ])

        if campaign_ids:
            vals['campaign_id'] = campaign_ids[0].id
        else:
            raise UserError("La campagna %s non esiste" % data['CAMPAGNA'])

        return vals