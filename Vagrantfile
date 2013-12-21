# vi: set ft=ruby :
# -*- mode: ruby -*-

nodes = {
  'lb' => {:ip => '192.168.80.10'},
  'web' => {:ip => '192.168.80.20'},
  'web2' => {:ip => '192.168.80.30'},
}

Vagrant.configure('2') do |config|
  config.vm.box = "puppet-precise64"
  config.vm.box_url = "http://puppet-vagrant-boxes.puppetlabs.com/ubuntu-server-1204-x64.box"

  config.vm.provision :puppet, :options => ["--debug", "--verbose", "--summarize", "--reports", "store"] do |puppet|
    puppet.manifests_path = "manifests"
    puppet.module_path    = "modules"
    puppet.manifest_file  = "base.pp"
    puppet.hiera_config_path = "hiera.yaml"
  end

  nodes.each do |node_name, node_opts|
    config.vm.define node_name do |conf|
      conf.vm.hostname = node_name
      conf.vm.network :private_network, ip: node_opts[:ip]
    end
  end

end
