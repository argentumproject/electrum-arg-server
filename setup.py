from setuptools import setup

setup(
    name="electrum-arg-server",
    version="1.0",
    scripts=['run_electrum_arg_server.py','electrum-arg-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0'],
    package_dir={
        'electrumargserver':'src'
        },
    py_modules=[
        'electrumargserver.__init__',
        'electrumargserver.utils',
        'electrumargserver.storage',
        'electrumargserver.deserialize',
        'electrumargserver.networks',
        'electrumargserver.blockchain_processor',
        'electrumargserver.server_processor',
        'electrumargserver.processor',
        'electrumargserver.version',
        'electrumargserver.ircthread',
        'electrumargserver.stratum_tcp'
    ],
    description="Argentum Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="https://github.com/argentumproject/electrum-arg-server/",
    long_description="""Server for the Electrum Lightweight Argentum Wallet"""
)
