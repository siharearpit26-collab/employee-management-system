from django.db import migrations


def seed_data(apps, schema_editor):
    Department = apps.get_model('emp_app', 'Department')
    Role = apps.get_model('emp_app', 'Role')

    departments = [
        ('Engineering', 'Floor 3'),
        ('Human Resources', 'Floor 1'),
        ('Finance', 'Floor 2'),
        ('Marketing', 'Floor 2'),
        ('Operations', 'Floor 4'),
        ('Sales', 'Floor 1'),
    ]
    for name, location in departments:
        Department.objects.get_or_create(name=name, defaults={'location': location})

    roles = [
        'Software Engineer',
        'Senior Software Engineer',
        'Product Manager',
        'HR Manager',
        'Accountant',
        'Marketing Specialist',
        'Sales Representative',
        'Operations Manager',
        'Data Analyst',
        'DevOps Engineer',
    ]
    for name in roles:
        Role.objects.get_or_create(name=name)


def unseed_data(apps, schema_editor):
    Department = apps.get_model('emp_app', 'Department')
    Role = apps.get_model('emp_app', 'Role')
    Department.objects.all().delete()
    Role.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_attendance'),
    ]

    operations = [
        migrations.RunPython(seed_data, unseed_data),
    ]
