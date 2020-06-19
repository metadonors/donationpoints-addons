# Copyright 2019 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Donationpoints Campaigns',
    'description': """
        Donation Point Fundraising integration""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Metadonors Srl',
    'website': 'https://www.metadonors.it',
    'depends': [
        'donationpoints',
        'ngo_fundraising'
    ],
    'data': [
        'views/ngo_donation.xml',
        'views/donationpoints_donation.xml',
        'views/donationpoints_donationpoint.xml',
        'views/donationpoints_settings.xml',
    ],
    'demo': [
    ],
}
