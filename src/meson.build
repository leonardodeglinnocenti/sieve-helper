pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'sieve_helper'
gnome = import('gnome')

gnome.compile_resources('sieve-helper',
  'sieve-helper.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', get_option('prefix') / get_option('localedir'))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'sieve-helper.in',
  output: 'sieve-helper',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'r-xr--r--'
)

sieve_helper_sources = [
  '__init__.py',
  'main.py',
  'window.py',
]

install_data(sieve_helper_sources, install_dir: moduledir)
