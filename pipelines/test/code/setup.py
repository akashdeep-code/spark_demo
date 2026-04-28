from setuptools import setup, find_packages
setup(
    name = 'test',
    version = '1.0',
    packages = find_packages(include = ('test*', )) + ['prophecy_config_instances.test'],
    package_dir = {'prophecy_config_instances.test' : 'configs/resources/test'},
    package_data = {'prophecy_config_instances.test' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.16'],
    entry_points = {
'console_scripts' : [
'main = test.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
