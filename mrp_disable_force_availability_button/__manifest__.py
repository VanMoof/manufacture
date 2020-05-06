# Copyright 2020 Vanmoof B.V.
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "MRP Disable force availability button",
    "version": "12.0.1.0.0",
    "summary": "Disable force availability button in manufacturing orders.",
    "development_status": "Mature",
    "author": "Eficent, Odoo Community Association (OCA), Vanmoof B.V.",
    "website": "http://www.odoomrp.com",
    "category": "Manufacturing",
    "license": "AGPL-3",
    "application": False,
    "depends": ["mrp"],
    "data": [
        "security/mrp_disable_force_availability_button_security.xml",
        "views/mrp_operation_view.xml",
    ],
}

