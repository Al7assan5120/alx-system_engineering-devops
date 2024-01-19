# Ensure Python is installed
include python

# Install Flask via pip
python::pip { 'flask':
 ensure  => '2.1.0',
 provider => 'pip',
}
