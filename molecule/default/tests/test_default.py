import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ssl_dir(host):
    private = host.file('/etc/ssl/private')
    assert private.exists
    assert private.user == 'root'
    assert private.group == 'root'
    # TODO: test mode

    certs = host.file('/etc/ssl/certs')
    assert certs.exists
    assert certs.user == 'root'
    assert certs.group == 'root'
    # TODO: test mode

    for name in ("first.example.com", "second.example.com"):
        assert host.file("/etc/ssl/private/%s.key" % name).exists
        assert host.file("/etc/ssl/private/%s.csr" % name).exists
        assert host.file("/etc/ssl/certs/%s.crt" % name).exists
