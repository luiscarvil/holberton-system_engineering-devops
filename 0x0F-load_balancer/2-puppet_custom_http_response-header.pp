#!/usr/bin/env bash
# creating a custom HTTP header response, but with Puppet

exec {'http header':
command  => "sudo apt update && sudo apt -y install nginx &&
             sudo sed -i '/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;' /etc/nginx/sites-available/default &&
             sudo service nginx restart",
provider => shell,
}
