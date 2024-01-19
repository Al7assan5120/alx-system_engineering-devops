#!/usr/bin/pup
# Installs flask, version 2.1.0

package { 'python3-pip':
  ensure => Installs,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require => package['python3-pip'],
}

package { 'werkeug':
  ensure   => '2.1.0',
  provider => 'pip3',
  require => package['python3-pip'],
}
