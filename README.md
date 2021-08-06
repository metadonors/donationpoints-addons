# Come lavorare sugli addons

Clonare il progetto base ti odoo 

```bash
git clone -b 12.0 git@bitbucket.org:metadonors/odoo-base-project.docker.git dboxtest.docker
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







