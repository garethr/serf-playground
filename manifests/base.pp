hiera_include('classes')

class { 'serf':
  version   => '0.4.1',
  bind      => $::ipaddress_eth1,
  advertise => $::ipaddress_eth1,
  protocol  => 3,
  rpc_addr  => '127.0.0.1:7373',
  join      => ['192.168.80.10'],
  event_handler => [
    '/vagrant/serf_handler/handler.py'
  ]
}

package { [
  'git-core',
  'python-pip',
]:
  ensure => installed,
}

package { [
  'serf_master',
  'serfclient',
]:
  ensure   => installed,
  provider => pip,
  require  => [
    Package['git-core'],
    Package['python-pip'],
  ],
}
