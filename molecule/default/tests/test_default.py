import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

PACKAGE = '1password'
PACKAGE_BINARY = '/usr/bin/1password'
REPO_DEBIAN_FILE = '/etc/apt/sources.list.d/1password.list'
REPO_EL_FILE = '/etc/yum.repos.d/1password.repo'


def test_1password_package_installed(host):
    """
    Tests if 1password package is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_1password_binary_exists(host):
    """
    Tests if 1password binary exists.
    """
    host.file(PACKAGE_BINARY).exists


def test_1password_binary_isfile(host):
    """
    Tests if 1password binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_symlink


def test_1password_binary_which(host):
    """
    Tests the output to confirm 1password's binary location.
    """
    assert host.check_output('which 1password') == PACKAGE_BINARY


def test_1password_repofile_exists(host):
    """
    Tests if 1password repo file exists.
    """
    assert host.file(REPO_DEBIAN_FILE).exists or \
        host.file(REPO_EL_FILE).exists


def test_1password_repofile_isfile(host):
    """
    Tests if 1password repo file is file type.
    """
    assert host.file(REPO_DEBIAN_FILE).is_file or \
        host.file(REPO_EL_FILE).is_file
