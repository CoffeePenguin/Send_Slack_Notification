from setuptools import find_packages, setup

setup(
    name='send_slack_notification',
    version='1.0',
    packages=find_packages(),
    install_requires=["requests"]
)