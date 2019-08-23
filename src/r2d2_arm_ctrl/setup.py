from setuptools import setup

package_name = 'r2d2_arm_ctrl'

setup(
    name=package_name,
    version='0.7.0',
    packages=[],
    py_modules=[
        'arm_ctrl_sub',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Mikael Arguedas',
    author_email='mikael@osrfoundation.org',
    maintainer='Mikael Arguedas',
    maintainer_email='mikael@osrfoundation.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Examples of minimal subscribers using rclpy.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'arm_ctrl_sub = arm_ctrl_sub:main',
        ],
    },
)