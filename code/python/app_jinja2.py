application: <username>
version: 1
runtime: python27
api_version: 1
threadsafe: true

libraries:
- name: jinja2
  version: latest

handlers:
- url: /.*
  script: asciichan.app
