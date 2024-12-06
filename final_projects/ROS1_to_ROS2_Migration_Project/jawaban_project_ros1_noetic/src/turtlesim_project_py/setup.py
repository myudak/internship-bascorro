from setuptools import setup

package_name = 'turtlesim_project_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ed',
    maintainer_email='ed@todo.todo',
    description='Python nodes for turtlesim project',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_controller = turtlesim_project_py.turtle_controller:main',
        ],
    },
)
