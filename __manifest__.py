{
    'name': 'My Test Module',
    'version': '1.0',
    'author': 'Your Name',
    'category': 'Test',
    'summary': 'A simple test module for Odoo 16.',
    'description': """
    This is a test module for learning purposes.
    """,
    'depends': ['base'],
    'data': [
        # Add your' XML files here if any
        'security/ir.model.access.csv',
       # 'views/add_site.xml',
        'views/support_call_menu.xml',
    ],
    # 'qweb': [
    #     'static/src/xml/my_nepali_datepicker_template.xml',
    #     # 'static/src/xml/nepali_datepicker_assets',
    # ],
     'assets': {
   'web.assets_backend': [

       '/support_call/static/src/js/my_nepali_datepicker_widget.js',
       '/support_call/static/src/js/nepaliDatePicker.js',
       '/support_call/static/src/css/nepaliDatePicker.css',
       '/support_call/static/src/xml/my_nepali_datepicker_template.xml',





   ],
},
    'installable': True,
    'auto_install': False,
    'application':True,
}
