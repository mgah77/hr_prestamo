# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{ 'name': 'HR Prestamos',
'summary': "Prestamos",
'author': "Mauricio Gah",
'license': "AGPL-3",
'application': "True",
'version': "2.0",
'data': ['security/groups.xml',
         'security/ir.model.access.csv',     
         'views/prestamo.xml',
        
],

'depends': ['base' , 'contacts' , 'hr' , 'parches'],
'installable': True,
'application': True,
}
