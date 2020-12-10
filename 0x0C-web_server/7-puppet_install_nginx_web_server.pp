#puppet install nginx
package { 'nginx':
ensure => installed,
}

file { '/var/www/html/index.html':
content => 'Holberton School',
}
exec {"/usr/bin/env ufw allow 'Nginx HTTP'":
}

file_line { 'redirect_me, 301':
ensure => 'present',
path   => '/etc/nginx/sites-available/default',
after  => 'listen 80 default_server',
line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
ensure  => running,
require => Package['nginx'],
}
