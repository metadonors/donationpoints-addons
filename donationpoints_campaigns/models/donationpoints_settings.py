import logging 

from openerp import models, fields, api, _

_logger = logging.getLogger(__name__)

PAYMENT_MODE_ID_CONF = "donationpoints.payment_mode_id"
JOURNAL_ID_CONF = "donationpoints.journal_id"


class DonationpointsSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    payment_mode_id = fields.Many2one(
        'account.payment.mode',
        string=_('Default Account Payment Mode')
    )

    journal_id = fields.Many2one(
        'account.journal',
        string=_('Default Journal')
    )

    @api.model
    def set_values(self):
        super(DonationpointsSettings, self).set_values()
        self.ensure_one()

        _logger.error("===========SET")
        _logger.error(self.payment_mode_id.id)
        
        if self.payment_mode_id:
            self.env['ir.config_parameter'].set_param(PAYMENT_MODE_ID_CONF, self.payment_mode_id.id)
        
        if self.journal_id:
            self.env['ir.config_parameter'].set_param(JOURNAL_ID_CONF, self.journal_id.id)

    def get_values(self):
        res = super(DonationpointsSettings, self).get_values()
        
        p_id = self.env['ir.config_parameter'].get_param(PAYMENT_MODE_ID_CONF, None)

        _logger.error("===========GET")
        _logger.error(p_id)
        if p_id:
            # res['payment_mode_id'] = self.env['account.payment.mode'].browse(int(p_id[0]))
            res['payment_mode_id'] = int(p_id[0])
        
        j_id = self.env['ir.config_parameter'].get_param(JOURNAL_ID_CONF, None)
        if j_id:
            # res['journal_id'] = self.env['account.journal'].browse(int(j_id[0]))
            res['journal_id'] = int(j_id[0])

        return res
