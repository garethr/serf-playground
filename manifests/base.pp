hiera_include('classes')

class { 'serf':
  bind     => $::ipaddress_eth1,
  rpc_addr => "${$::ipaddress_eth1}:7337",
  join     => [
    '192.168.80.10',
  ]
}
