#!/usr/bin/env bash
# creating a custom HTTP header response, but with Puppet

exec {'http header':
command  => 'sudo apt update;
             sudo apt -y install nginx;
             sudo sed -i "/server_name _/a \\\tadd_header X-Served-By \$hostname;\n" /etc/nginx/nginx.conf;
             sudo service nginx restart',
provider => 'shell',
}
