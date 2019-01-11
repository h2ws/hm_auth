from setuptools import setup
setup(
        name='hm_auth',
        version='1.21',
        author='oyy', 
        author_email='oyy284688@gmail.com', 
        url='http://dadadakeai.com/hm_auth/index.html',
        license='GUN',
        packages=['hm_auth', 'hm_auth.config'],
        summary='黑马Portal命令认证工具',

        install_requires=['lluser>=1.20'],
        )
