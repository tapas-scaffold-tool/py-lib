import pkg_resources

__version__ = pkg_resources.resource_string(__name__, '{{module_name}}.version').decode('utf-8').strip()

