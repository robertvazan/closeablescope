# This script generates and updates project configuration files.

# Run this script with rvscaffold in PYTHONPATH
import rvscaffold as scaffold

class Project(scaffold.Java):
    def script_path_text(self): return __file__
    def repository_name(self): return 'closeablescope'
    def pretty_name(self): return 'CloseableScope'
    def pom_description(self): return 'Unchecked version of AutoCloseable.'
    def inception_year(self): return 2022
    def project_status(self): return self.stable_status()
    
    def dependencies(self):
        yield from super().dependencies()
        yield self.use_junit()
        yield self.use_hamcrest()

Project().generate()
