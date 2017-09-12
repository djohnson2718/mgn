from distutils.core import setup

try:
    from sage.env import SAGE_SRC, SAGE_VERSION
except ImportError:
    print "WARNING: This package only works with SageMath."

print "This is version 1.0.9"

with open("README.rst") as f:
    long_description = f.read()
    
setup(
    name='mgn',
    version='1.0.9',
    packages=['strataalgebra', 'topintersections'],
    url='https://github.com/uberparagon/mgn',
    download_url="https://github.com/uberparagon/mgn/releases/latest/",
    license='TODO',
    author='Drew Johnson',
    author_email='werd2.718@gmail.com',
    description='A Sage program for computing products, Faber-Zagier relations, and top intersections on the moduli space of stable curves.',
    long_description = long_description
)
