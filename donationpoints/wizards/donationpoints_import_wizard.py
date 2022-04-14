# Copyright 2019 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
import base64

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import datetime
from tablib import Dataset

_logger = logging.getLogger(__name__)

class DonationpointsImportWizard(models.TransientModel):

    _name = 'donationpoints.import.wizard'

    file = fields.Binary(
        string=_("CSV File")
    )

    def _prepare_donationbox_vals(self, data):
        vals = {}
        return vals

    def _prepare_location_vals(self, data):
        vals = {}
        vals['name'] = data['NEGOZIO'].title()
        vals['address1'] = "%s" % data['INDIRIZZO'].title()
        vals['city'] = data['CITTA']
        vals['phone'] = data['TELEFONO']
        vals['postal_code'] = data['CAP']

        type_ids = self.env['donationpoints.location.type'].search([
            ('name', '=', data['TIPO'].title())
        ])
        if type_ids:
            vals['location_type_id'] = type_ids[0].id
        else:
            type_id = self.env['donationpoints.location.type'].create({
                'name': data['TIPO'].title()
            })
            vals['location_type_id'] = type_id.id

        if data['GESTORE ASSEGNATO'] and data['GESTORE ASSEGNATO'] != 'SEDE':
            partner_ids = self.env['res.partner'].search([
                ('name', '=', data['GESTORE ASSEGNATO'].title())
            ])
            if partner_ids:
                vals['responsable_partner_id'] = partner_ids[0].id
            else:
                partner_id = self.env['res.partner'].create({
                    'name': data['GESTORE ASSEGNATO'].title()
                })
                vals['responsable_partner_id'] = partner_id.id
        
        vals['note'] = data['Note']

        return vals

    def _prepare_donationpoint_vals(self, data, location_id, dbox_id):
        vals = {}

        vals['location_id'] = location_id.id
        vals['donationbox_id'] = dbox_id.id
        vals['state'] = 'active'

        if data['DATA ATTIVAZIONE']:
            try:
                d = datetime.strptime(data['DATA ATTIVAZIONE'], "%d/%m/%Y")
                vals['start_date'] = d
            except: 
                pass

        return vals

    def _import_row(self, data):

        # crea la dbox
        dbox_vals = self._prepare_donationbox_vals(data)
        donationbox_id = self.env['donationpoints.donationbox'].create(dbox_vals)

        # crea la location
        location_vals = self._prepare_location_vals(data)
        location_id = self.env['donationpoints.location'].create(location_vals)

        # crea il dpoint
        donationpoint_vals = self._prepare_donationpoint_vals(data, location_id, donationbox_id)
        donationpoint_id = self.env['donationpoints.donationpoint'].create(donationpoint_vals)

        return donationpoint_id

    def _import_file(self, data):
        imported = []
        for row in data.dict:
            donationpoint_id = self._import_row(row)
            imported.append(donationpoint_id.id)

        return imported

    def doit(self):
        for wizard in self:
            if not self.file:
                raise UserError("Devi inserire un file per l'importazione")

            data = base64.decodestring(self.file)
            try:
                dataset = Dataset().load(data.decode('utf-8'), format='csv')
                imported_ids = self._import_file(dataset)
            except Exception as e: 
                raise e
                raise UserError("Tipo di file non valido")

        action = {
            'type': 'ir.actions.act_window',
            'name': 'Donation Points',
            'res_model': 'donationpoints.donationpoint',
            'domain': [('id', 'in', imported_ids)],
            'view_mode': 'tree',
        }
        return action
