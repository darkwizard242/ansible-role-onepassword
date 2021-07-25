[![build-test](https://github.com/darkwizard242/ansible-role-1password/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-1password/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-1password/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-1password/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/52607?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/52607?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/52607?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-1password&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-1password) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-1password&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-1password) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-1password&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-1password) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-1password&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-1password) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-1password?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-1password?color=orange&style=flat-square)

# Ansible Role: 1password

Role to install (_by default_) [1password](https://1password.com/) package for Debian based and EL based systems or uninstall (_if passed as var_) on **Debian** based and **EL** based systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
# Generic Variables
onepassword_app_name: 1password
onepassword_desired_state: present

# Debian Family Variables
onepassword_pre_reqs_debian:
  - gnupg2
onepassword_pre_reqs_debian_desired_state: present
onepassword_repo_debian_gpg_key_url: https://downloads.1password.com/linux/keys/1password.asc
onepassword_repo_debian_gpg_key_keyring: /usr/share/keyrings/1password-archive-keyring.gpg
onepassword_repo_debian: "deb [arch=amd64 signed-by={{ onepassword_repo_debian_gpg_key_keyring }}] https://downloads.1password.com/linux/debian/amd64 stable main"
onepassword_repo_debian_filename: "{{ onepassword_app_name }}"
onepassword_repo_debian_desired_state: present

# EL Family Variables
onepassword_repo_el_name: 1password
onepassword_repo_el_description: 1Password Stable Channel
onepassword_repo_el: https://downloads.1password.com/linux/rpm/stable/$basearch
onepassword_repo_el_gpg_key: https://downloads.1password.com/linux/keys/1password.asc
onepassword_repo_el_enabled: yes
onepassword_repo_el_filename: "{{ onepassword_app_name }}"
onepassword_repo_el_gpgcheck: yes
onepassword_repo_el_repogpgcheck: yes
onepassword_repo_el_desired_state: present
```

### Variables table:

Variable                                  | Description
----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
onepassword_app_name                      | Name of 1Password package to install by default i.e. `1password` . You may use other packages such as `1password-8-openj9`, `1password-15-hotspot` etc.. as well.
onepassword_desired_state                 | State of the 1password_app_name package (i.e. `1password` package itself.). Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
onepassword_pre_reqs_debian               | Package required by 1Password on Debain based systems.
onepassword_pre_reqs_debian_desired_state | State of the 1password_pre_reqs_debian_desired_state packages. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
onepassword_repo_debian_gpg_key_url       | 1Password GPG required on Debian based systems.
onepassword_repo_debian_gpg_key_keyring   | 1Password Keyring file to store GPG key in.
onepassword_repo_debian                   | Repository URL for Debian based systems.
onepassword_repo_debian_filename          | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems. Defaults to the variable value for "{{ 1password_app_name }}" which is `1password` by default.
onepassword_repo_debian_desired_state     | State of Debian family repository file for 1Password.
onepassword_repo_el_name                  | Repository name for 1Password on EL based systems.
onepassword_repo_el_gpg_key               | 1Password GPG required on EL based systems.
onepassword_repo_el_description           | Description to be added in EL based repository file for 1Password.
onepassword_repo_el                       | Repository `baseurl` for 1Password on EL based systems.
onepassword_repo_el_gpgcheck              | Boolean for whether to perform gpg check against 1Password on EL based systems.
onepassword_repo_el_repogpgcheck          | Boolean for whether to perform gpg signature check against on the repodata for 1Password on EL based systems.
onepassword_repo_el_enabled               | Boolean for whether to set 1Password repo as 'enabled' on EL based systems.
onepassword_repo_el_filename              | Name of the repository file that will be stored at `/etc/yum/sources.list.d/` on EL based systems. Defaults to the variable value for "{{ 1password_app_name }}" which is `1password` by default.
onepassword_repo_el_desired_state         | State of EL family repository file for 1Password.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **1password** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.1password
```

For customizing behavior of role (for e.g. installation of j9 jvm instead of hotspot, **1password-15-openj9** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.1password
  vars:
    onepassword_app_name: 1password
```

For customizing behavior of role (for e.g. un-installation of **1password** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.1password
  vars:
    onepassword_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-1password/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
