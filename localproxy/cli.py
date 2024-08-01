import os

import click

from localproxy.proxy import ProxyConfig

CONFIG_FILE = os.path.expanduser("~/.local_proxy/proxy.toml")


@click.group()
def cli():
    """Local Proxy CLI"""
    pass


@cli.command()
def list():
    """Display existing proxy configuration"""
    config = ProxyConfig(CONFIG_FILE)
    proxies = config.load()
    if proxies:
        for protocol, address in proxies.items():
            click.echo(f"{protocol}: {address}")
    else:
        click.echo("No proxy configurations found.")


@cli.command()
@click.argument('protocol')
@click.argument('address')
def set(protocol, address):
    """Set a proxy configuration"""
    config = ProxyConfig(CONFIG_FILE)
    proxies = config.load()
    proxies[protocol] = address
    config.save(proxies)
    click.echo(f"Set {protocol} proxy to {address}")


@cli.command()
def clear():
    """Clear all proxy configurations"""
    config = ProxyConfig(CONFIG_FILE)
    config.save({})
    click.echo("Cleared all proxy configurations.")
