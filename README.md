# Come lavorare sugli addons

Clonare il progetto base ti odoo 

```bash
git clone -b 12.0 --recurse-submodules git@bitbucket.org:metadonors/odoo.docker.git dboxtest.docker
```

Clonare il repository degli addons donationpoints

```bash
cd dboxtest.docker/addons

git clone git@bitbucket.org:metadonors/donationpoints-addons.git donationpoints
cd -
```

Aggiungere gli addons ai path di odoo 

```bash
vim conf/odoo_conf.yaml
```

in fondoo all'elenco degli _addons\_path_ aggiungere _/mnt/bundle-addons/donationpoints_

```
addons_path:
  - /mnt/bundle-addons/account-invoicing
  - /mnt/bundle-addons/connector
  - /mnt/bundle-addons/hr
  - /mnt/bundle-addons/muk_base
  - /mnt/bundle-addons/muk_misc
  - /mnt/bundle-addons/muk_web
  - /mnt/bundle-addons/l10n-italy
  - /mnt/bundle-addons/partner-contact
  - /mnt/bundle-addons/project
  - /mnt/bundle-addons/purchase-workflow
  - /mnt/bundle-addons/queue
  - /mnt/bundle-addons/rest-framework
  - /mnt/bundle-addons/server-tools
  - /mnt/bundle-addons/server-ux
  - /mnt/bundle-addons/web
  - /mnt/bundle-addons/website
  - /mnt/bundle-addons/donationpoints
```

Inizializzare il db

```bash 
docker-compose run odoo upgrade base
```

Lanciare odoo

```bash
docker-compose up
```

Andare su [http://localhost](http://localhost)

Tra le app selezionare il modulo Donationpoints e installarlo






