[![Build Status](https://travis-ci.org/bihealth/ansible-role-ssl-certs.svg?branch=master)](https://travis-ci.org/bihealth/ansible-role-ssl-certs)

# Installation / Creation of SSL Certificates

This Ansible role creates certificate files into `/etc/ssl/{private,certs}` for the `root` user.
The certificates and keys can either be given through role variables or certificates can be generated as self-signed.

## Requirements

none

## Role Variables

The namespace prefix is `ssl_certs`.

- `ssl_certs_certs` is a list of dict with the required key `name` that gives the name token of the certificate/key file.
   Put the certificate (or chain) into the key `cert` and unencrypted key into `key`.
   If `cert` is given then the role will write the certificate and key to `/etc/ssl/{private,certs}/$name.{crt,key}`.
   Otherwise, a self-signed certificate will be created with an additional `.csr` in the `private` directory.

## Dependencies

none

## Example Playbook

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  roles:
    - role: bihealth.ssl_certs
  vars:
    ssl_ssl_certs:
      # Self-signed certificate for first.example.com.
      - name: first.example.com
        cert: null
      # Real certificate for second.example.com.  The certificate and key both come
      # from the password store lookup.
      - name: second.example.conf
        cert: "{{ lookup('passwordstore', 'certs/second.example.com.crt' }}"
        key: "{{ lookup('passwordstore', 'keys/second.example.com.key' }}"
```

## License

MIT

## Open Issues

- copy resulting certificates somewhere else with given ownership and mode

## Author Information

- Manuel Holtgrewe

Created with love at [CUBI](https://www.cubi.bihealth.org).
