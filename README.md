# django-oscar

## Running project

```bash
. ./oscar/bin/activate
cd eshop
./manage.py runserver
```

## Create new project

```bash
mkdir oscar
cd oscar
virtualenv oscar
. ./oscar/bin/activate
pip install django-oscar
django-admin startproject eshop
cd eshop/
```

## Install sorl

```bash
pip install sorl-thumbnail
python manage.py migrate
```

## Create superuser

```bash
./manage.py createsuperuser
```

## Create catalogue

```bash
./manage.py oscar_fork_app catalogue eshop
```

### Change `settings.py`

```bash
INSTALLED_APPS = [
    # ...
    
    'eshop.catalogue.apps.CatalogueConfig',
    # 'oscar.apps.catalogue.apps.CatalogueConfig',

    # ...
]
```

## Create dashboard

```bash
./manage.py oscar_fork_app dashboard eshop
```

## Create partners in dashboard

```bash
./manage.py oscar_fork_app partners_dashboard eshop
./manage.py migrate
```

### After change

```bash
./manage.py makemigrations [name_folder]
./manage.py migrate
```

## Example `settings.py`
```bash
INSTALLED_APPS = [
    #...
    
    'eshop.catalogue.apps.CatalogueConfig',
    'eshop.dashboard.apps.DashboardConfig',
    'eshop.dashboard.catalogue.apps.CatalogueDashboardConfig',
    'eshop.partner.apps.PartnerConfig',
    'eshop.dashboard.partners.apps.PartnersDashboardConfig',

    # 'oscar.apps.catalogue.apps.CatalogueConfig',
    # 'oscar.apps.partner.apps.PartnerConfig',
    # 'oscar.apps.dashboard.apps.DashboardConfig',
    # 'oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig',
    # 'oscar.apps.dashboard.partners.apps.PartnersDashboardConfig',

    #...
]
```