#puppet install nginx
package { 'nginx':
  ensure => installed,
  name   => 'nginx',
}

file { 'index.html':
  content => 'Holberton School',
  path    => '/var/www/html/index.html'
}
exec {'/usr/bin/env sed -i "/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default': }

service { 'nginx':
ensure  => running,
require => Package['nginx'],
}
