#!/usr/bin/env bash
# creating a custom HTTP header response, but with Puppet

exec {'http header':
command  => 'sudo apt update && 
             sudo apt -y install nginx && 
             sudo sed -i "/listen 80 default_server;/a\\\tadd_header X-Served-By \$hostname;\n" /etc/nginx/nginx.conf && 
             sudo service nginx restart',
provider => shell,
}
