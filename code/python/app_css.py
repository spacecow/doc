application: <username>
version: 1
runtime: python27
api_version: 1
threadsafe: true

handlers:
- url: /static/
  static_dir: static

- url: /.*
  script: asciichan.app
