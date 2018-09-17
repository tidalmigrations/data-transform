# Signup at https://get.tidalmg.com

# Go to https://get.tidal.sh

curl https://get.tidal.sh/unix | bash

# Get credentials for both Tidal and vSphere

tidal login
tidal login vsphere

# Load up app at your_domain.tidalmg.com and see the server inventory

tidal sync vsphere

# Load up app and see the newly syncd vsphere data
# Create fields for the next step

tidal get vsphere | ./scripts/vsphere_transform.rb | tidal sync servers

# Load up app and see the newly syncd vsphere data

./scripts/csv_transform.rb < data/apps.csv | tidal sync apps

# Load up app and see sync apps
