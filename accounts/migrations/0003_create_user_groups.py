from django.db import migrations


def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    renters, _ = Group.objects.get_or_create(name='Renters')
    renter_perms = Permission.objects.filter(codename__in=[
        'add_reservation',
        'view_reservation',
        'change_reservation',
        'delete_reservation',
        'add_review',
        'view_review',
        'change_review',
        'delete_review',
        'view_item',
    ])
    renters.permissions.set(renter_perms)

    owners, _ = Group.objects.get_or_create(name='Owners')
    owner_perms = Permission.objects.filter(codename__in=[
        'add_item',
        'view_item',
        'change_item',
        'delete_item',
        'view_reservation',
        'add_review',
        'view_review',
        'change_review',
        'delete_review',
    ])
    owners.permissions.set(owner_perms)


def delete_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=['Renters', 'Owners']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.RunPython(create_groups, delete_groups),
    ]

