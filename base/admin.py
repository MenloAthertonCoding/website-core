from django.contrib.admin import AdminSite, site

class BaseAdminSite(AdminSite):
    site_header = 'Menlo Atherton Coding'
    site_title = 'Menlo Atherton Coding'

    def __init__(self, *args, **kwargs):
        super(BaseAdminSite, self).__init__(*args, **kwargs)
        self._registry.update(site._registry)

admin_site = BaseAdminSite(name='MAC Admin')
