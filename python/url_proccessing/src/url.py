from urllib.parse import parse_qs, urlencode, urlparse, urlunparse


def make(url):
    """
    Make an URL representation from string
    """
    return urlparse(url)


def get_scheme(data):
    """
    Return a scheme of given URL
    """
    return data.scheme


def set_scheme(data, scheme):
    """
    Return a new URL with replaced host
    """
    return data._replace(scheme=scheme)


def get_host(data):
    """
    Return a host of given URL
    """
    return data.netloc


def set_host(data, host):
    """
    Return a new URL with replaced host
    """
    return data._replace(netloc=host)


def get_path(data):
    """
    Replace scheme of given URL
    """
    return data.path


def set_path(data, path):
    """
    Return a new URL with replaced path
    """
    return data._replace(path=path)


def get_query_param(data, key, default=None):
    """
    Return a value of named query parameter of given URL
    Function returns default value if named parameter is not present
    """
    return parse_qs(data.query).get(key, [default])[0]


def set_query_param(data, key, value):
    """
    Return a new URL with replaced query parameter
    """
    params = parse_qs(data.query)
    if value is None:
        params.pop(key, None)
    else:
        params[key] = value
    return data._replace(query=urlencode(params, doseq=True))


def to_string(data):
    """
    Return a string representation of given URL
    """
    return urlunparse(data)
