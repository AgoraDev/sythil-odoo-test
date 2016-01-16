{
    'name': "Website Help Desk / Support Ticket",
    'version': "1.1",
    'author': "Sythil",
    'category': "Tools",
    'summary': "A helpdesk / support ticket system for your website",
    'license':'GPL-3',
    'data': [
        'website_support_ticket.xml',
        'website_support_ticket_categories.xml',
        'website_support_ticket_states.xml',
        'res_partner.xml',
        'website_support_help_groups.xml',
        'website.support.ticket.states.csv',
        'website.support.ticket.categories.csv',
        'website.menu.csv',
        'views/website_support_ticket.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'depends': ['web', 'crm', 'website'],
    'images':['static/description/1.jpg'],
    'installable': True,
}