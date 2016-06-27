from django.contrib.admin.sites import AdminSite


class McocoAdmin(AdminSite):
    pass

mcoco_admin = McocoAdmin(name="admin_mcoco")

