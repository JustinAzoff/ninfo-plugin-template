from setuptools import setup, find_packages

setup(name='ninfo-plugin-template',
    description="PasteScript template to create ninfo plugins",
    version='0.1.0',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "Paste",
        "PasteScript",
    ],
    entry_points="""
        [paste.paster_create_template]
        ninfo_plugin=ninfo_plugin:NinfoPluginTemplate
    """,
)
