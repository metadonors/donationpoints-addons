# Copyright 2020 Metadonors Srl

from odoo import api, fields, models, _


class DonationImport(models.TransientModel):

    _name = "donation.import"

    name = fields.Char()
    date = fields.Datetime(string=_("Donation date"))
    cardease_reference = fields.Char(string=_("CardEase Reference"))
    distributor = fields.Char(string=_("Distributor"))
    client = fields.Char(string=_("Client"))
    terminal_group = fields.Char(string=_("Terminal Group"))
    terminal_id = fields.Many2one("donationpoints.donationbox", string=_("Terminal ID"))
    terminal_name = fields.Char(related="terminal_id.name", string=_("Terminal"))
    terminal_code = fields.Char(
        related="terminal_id.code", string=_("Machine Reference")
    )
    acquirer = fields.Char(string=_("Acquirer"))
    merchant = fields.Char(string=_("Merchant"))
    merchant_number = fields.Char(string=_("Merchant Number"))
    merchant_number_alternative = fields.Char(string=_("Merchant Number Alternative"))
    acquirer_tid = fields.Char(string=_("Acquirer TID"))
    user_id = fields.Char(
        string=_("User Reference")
    )  # fields.Many2one('res.user', string=_('User Reference'))
    cardholder = fields.Char(string=_("Cardholder"))
    email_address = fields.Char(string=_("Email Address"))
    card_reference = fields.Char(string=_("Card Reference"))
    batch_reference = fields.Char(string=_("Batch Reference"))
    creator_email_reference = fields.Char(string=_("Creator Email Address"))
    card_number_start = fields.Char(string=_("Card NUmber Start"))
    card_number_end = fields.Char(string=_("Card NUmber End"))
    card_expiring_date = fields.Date(string=_("Expiry Date"))
    start_date = fields.Date(string=_("Start Date"))
    issue_number = fields.Char(string=_("Issue Number"))
    card_scheme = fields.Char(string=_("Card Scheme"))
    card_type = fields.Char(string=_("Card type"))
    domestic_international = fields.Char(string=_("Domestic/International"))
    entry_type = fields.Char(string=_("Entry Type"))
    type = fields.Char(string=_("Type"))
    auth_code = fields.Char(string=_("Auth Code"))
    avs_address_result = fields.Char(string=_("AVS Address Result"))
    avs_zip_result = fields.Char(string=_("AVS Zip Result"))
    csc_result = fields.Char(string=_("CSC Result"))
    secure_3d_enrolled = fields.Char(string=_("3-D Secure Enrolled"))
    secure_3d_status = fields.Char(string=_("3-D Secure Status"))
    secure_3d_eci = fields.Char(string=_("3-D Secure ECI"))
    secure_3d_xid = fields.Char(string=_("3-D Secure XID"))
    fraud_profiler = fields.Char(string=_("Fraud Profiler"))
    fraud_state = fields.Char(string=_("Fraud State"))
    fraud_score = fields.Char(string=_("Fraud Score"))
    result = fields.Char(string=_("Result"))
    state = fields.Char(string=_("State"))
    settlement_state = fields.Char(string=_("Settlement State"))
    settlement_datetime = fields.Datetime(string=_("Settlement Date/Time"))
    currency = fields.Char(string=_("Currency"))
    amount_authorised = fields.Char(string=_("Amount Authorised"))
    amount = fields.Char(string=_("Amount"))
    latitude = fields.Char(string=_("Latitude"))
    longitude = fields.Char(string=_("Longitude"))
    accuracy = fields.Char(string=_("Accuracy"))
    amount_approved_online = fields.Char(string=_("Amount Approved Online"))
    amount_currency = fields.Char(string=_("Amount Currency"))
    amount_requested_authorisation = fields.Char(
        string=_("Amount Requested at Authorisation")
    )
    amount_final = fields.Char(string=_("Amount Final"))
    cashback_authorised = fields.Char(string=_("Cashback Authorised"))
    cashback_requested_authorisation = fields.Char(
        string=_("Cashback Requested at Authorisation")
    )
    tip_authorised = fields.Char(string=_("Tip Authorised"))

    tip_requested_at_authorization = fields.Char(
        string=_("Tip Requested at Authorisation")
    )
    transanction_fee = fields.Char(string=_("Transaction Fee"))
    transanction_merchant_name = fields.Char(string=_("Transaction Merchant Name"))
    transanction_merchant_address = fields.Char(
        string=_("Transaction Merchant Address")
    )
    user_data = fields.Char(string=_("User Data"))
    acquirer_response_code = fields.Char(string=_("Acquirer Response Code"))
    acquirer_response_code_address = fields.Char(
        string=_("Acquirer Response Code Description")
    )
    amount_currency_dcc = fields.Char(string=_("Amount Currency (DCC)"))
    amount_approved_online_dcc = fields.Char(string=_("Amount Approved Online (DCC)"))
    amount_requested_at_authorization_dcc = fields.Char(
        string=_("Amount Requested at Authorisation (DCC)")
    )
    amount_final_dcc = fields.Char(string=_("Amount Final (DCC)"))
    amount_type_dcc = fields.Char(string=_("Amount Type (DCC)"))
    cashback_authorised_dcc = fields.Char(string=_("Cashback Authorised (DCC)"))
    cashback_requested_at_authorization_dcc = fields.Char(
        string=_("Cashback Requested at Authorisation (DCC)")
    )
    tip_authorised_dcc = fields.Char(string=_("Tip Authorised (DCC)"))
    tip_requested_authorization_dcc = fields.Char(
        string=_("Tip Requested at Authorisation (DCC)")
    )
    transaction_fee_dcc = fields.Char(string=_("Transaction Fee (DCC)"))

    @api.multi
    def doit(self):
        pass

    #    for wizard in self:
    #    action = {
    #        'type': 'ir.actions.act_window',
    #        'name': 'Action Name',
    #        'res_model': 'result.model',  # TODO
    #        'domain': [('id', '=', result_ids)],  # TODO
    #        'view_mode': 'form,tree',
    #    }
    #    return action
