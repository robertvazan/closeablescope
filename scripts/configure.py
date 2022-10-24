# This script generates and updates project configuration files.

# We are assuming that project-config is available in sibling directory.
# Checkout from https://github.com/robertvazan/project-config
import pathlib
project_directory = lambda: pathlib.Path(__file__).parent.parent
config_directory = lambda: project_directory().parent/'project-config'
exec((config_directory()/'src'/'java.py').read_text())

project_script_path = __file__
repository_name = lambda: 'closeablescope'
pretty_name = lambda: 'CloseableScope'
pom_description = lambda: 'Unchecked version of AutoCloseable.'
inception_year = lambda: 2022
jdk_version = lambda: 11
has_website = lambda: False

def dependencies():
    use_junit()
    use_hamcrest()

generate()
