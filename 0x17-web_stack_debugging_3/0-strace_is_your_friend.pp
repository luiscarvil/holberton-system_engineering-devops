# fix error - replace extension .phpp to .php
exec { 'puppet-lint':
    command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
    path    => ['/usr/bin', '/usr/sbin', '/usr/local/bin', '/usr/local/sbin'],
}
	