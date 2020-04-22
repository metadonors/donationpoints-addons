# Copyright 2019 Metadonors Srl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Donationpoints',
    'description': """
        Donation Point Management""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Metadonors Srl',
    'website': 'https://www.metadonors.it',
    'application': True,
    'depends': ['base','mail'
    ],
    'data': [
        'security/donationpoints_donation.xml',
        'views/donationpoints_donation.xml',
        'security/donationpoints_channel_location.xml',
        'views/donationpoints_channel_location.xml',
        'security/donationpoints_channel.xml',
        'views/donationpoints_channel.xml',
        'security/donationpoints_donationbox_type.xml',
        'views/donationpoints_donationbox_type.xml',
        'security/donationpoints_location_type.xml',
        'views/donationpoints_location_type.xml',
        'security/donationpoints_location.xml',
        'views/donationpoints_location.xml',
        'security/donationpoints_visit_type.xml',
        'views/donationpoints_visit_type.xml',
        'security/donationpoints_visit.xml',
        'views/donationpoints_visit.xml',
        'security/donationpoints_donationbox_condition.xml',
        'security/donationpoints_donationbox.xml',
        'views/donationpoints_donationbox.xml',
        'views/donationpoints_donationbox_condition.xml',
        'views/donationpoints_menu.xml',
        'data/donationpoints_condition.xml',
        'data/ir_sequence_data.xml',
    ],
    'demo': [
    ],
    
}
