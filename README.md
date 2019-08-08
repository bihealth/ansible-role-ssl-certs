# Installation / Creation of SSL Certificates

This Ansible role creates certificate files into `/etc/ssl/{private,certs}` for the `root` user.
The certificates and keys can either be given through role variables or certificates can be generated as self-signed.

## Requirements

- Tested on CentOS 7 only.

## Role Variables

Namespace is `ssl_certs`.
Configuration example:

```yaml
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

## Open Issues

- copy resulting certificates somewhere else with given ownership and mode
