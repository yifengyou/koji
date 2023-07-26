from __future__ import absolute_import

import unittest

import mock
import six
import koji

from koji_cli.commands import anon_handle_mock_config
from . import utils


class TestMockConfig(utils.CliTestCase):

    # Show long diffs in error output...
    maxDiff = None

    def setUp(self):
        self.options = mock.MagicMock()
        self.options.debug = False
        self.session = mock.MagicMock()
        self.session.getAPIVersion.return_value = koji.API_VERSION
        self.gen_config_mock = mock.patch('koji.genMockConfig').start()
        self.ensure_connection_mock = mock.patch('koji_cli.commands.ensure_connection').start()
        self.maxDiff = None
        self.common_args = [
            '--distribution', 'fedora',
            '--topdir', '/top-dir',
            '--topurl', '/top-url',
            '--yum-proxy', '/yum-proxy'
        ]
        self.common_opts = {
            'distribution': 'fedora',
            'mockdir': '/var/lib/mock',
            'topdir': '/top-dir',
            'topurl': '/top-url',
            'yum_proxy': '/yum-proxy',
        }
        self.mock_output = """# Auto-generated by the Koji build system

config_opts['chroot_setup_cmd'] = 'groupinstall build'
config_opts['use_host_resolv'] = False
config_opts['root'] = 'fedora26-build-repo_1'
config_opts['yum.conf'] = '[main]\ncachedir=/var/cache/yum\ndebuglevel=1\nlogfile=/var/log/yum.log\nreposdir=/dev/null\nretries=20\nobsoletes=1\ngpgcheck=0\nassumeyes=1\nkeepcache=1\ninstall_weak_deps=0\nstrict=1\n\n# repos\n\n[build]\nname=build\nbaseurl=https://fedora.local/kojifiles/repos/fedora26-build/1/x86_64\n'
config_opts['rpmbuild_timeout'] = 86400
config_opts['chroothome'] = '/builddir'
config_opts['target_arch'] = 'x86_64'
config_opts['basedir'] = '/var/lib/mock'

config_opts['plugin_conf']['yum_cache_enable'] = False
config_opts['plugin_conf']['root_cache_enable'] = False
config_opts['plugin_conf']['ccache_enable'] = False

config_opts['macros']['%_rpmfilename'] = '%%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm'
config_opts['macros']['%_topdir'] = '/builddir/build'
config_opts['macros']['%packager'] = 'Koji'
config_opts['macros']['%_host'] = 'x86_64-koji-linux-gnu'
config_opts['macros']['%_host_cpu'] = 'x86_64'
config_opts['macros']['%vendor'] = 'Koji'
config_opts['macros']['%distribution'] = 'Koji Testing'
"""
        self.error_format = """Usage: %s mock-config [options]
(Specify the --help global option for a list of other help options)

%s: error: {message}
""" % (self.progname, self.progname)

    @mock.patch('sys.stdout', new_callable=six.StringIO)
    def test_handle_mock_config_buildroot_option(self, stdout):
        """Test anon_handle_mock_config buildroot options"""
        buildroot_info = {
            'repo_id': 101,
            'tag_name': 'tag_name',
            'arch': 'x86_64'
        }

        # Mock out the xmlrpc server
        self.session.getBuildroot.return_value = buildroot_info

        # Mock config
        self.gen_config_mock.return_value = self.mock_output

        # buildroot check
        arguments = ['--buildroot', 'root', self.progname]
        expected = self.format_error_message("Buildroot id must be an integer")
        self.assert_system_exit(
            anon_handle_mock_config,
            self.options, self.session, arguments,
            stderr=expected,
            exit_code=2,
            activate_session=None)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        arguments = self.common_args + ['--buildroot', '1', '--name', self.progname]
        opts = self.common_opts.copy()
        opts.update({
            'repoid': buildroot_info['repo_id'],
            'tag_name': buildroot_info['tag_name'],
            'tag_macros': {},
        })
        del opts['topurl']
        anon_handle_mock_config(self.options, self.session, arguments)
        self.assert_console_message(stdout, "%s\n" % self.gen_config_mock.return_value)
        self.gen_config_mock.assert_called_with(self.progname, buildroot_info['arch'], **opts)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        arguments = self.common_args + ['--buildroot', '1',
                                        '--name', self.progname,
                                        '--latest']
        opts['repoid'] = 'latest'
        anon_handle_mock_config(self.options, self.session, arguments)
        self.assert_console_message(stdout, "%s\n" % self.gen_config_mock.return_value)
        self.gen_config_mock.assert_called_with(self.progname, buildroot_info['arch'], **opts)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        # if buildroot is not existing
        buildroot_id = '999999'
        arguments = ['--buildroot', buildroot_id]
        self.session.getBuildroot.return_value = None
        expected = "No such buildroot: %s" % buildroot_id + "\n"
        self.assert_system_exit(
            anon_handle_mock_config,
            self.options, self.session, arguments,
            stderr=expected,
            exit_code=1,
            activate_session=None)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

    @mock.patch('sys.stdout', new_callable=six.StringIO)
    def test_handle_mock_config_task_option(self, stdout):
        """Test  anon_handle_mock_config task options"""
        task_id = 1001
        self.session.listBuildroots.return_value = ''

        # Mock config
        self.gen_config_mock.return_value = ''

        arguments = ['--task', 'task']
        expected = self.format_error_message("Task id must be an integer")
        self.assert_system_exit(
            anon_handle_mock_config,
            self.options, self.session, arguments,
            stderr=expected,
            exit_code=2,
            activate_session=None)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        arguments = ['--task', str(task_id)]
        expected = "No buildroots for task %s (or no such task)\n" % str(task_id)
        self.assert_system_exit(
            anon_handle_mock_config,
            self.options, self.session, arguments,
            stderr=expected,
            exit_code=1,
            activate_session=None)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        multi_broots = [
            {'id': 1101, 'repo_id': 101, 'tag_name': 'tag_101', 'arch': 'x86_64'},
            {'id': 1111, 'repo_id': 111, 'tag_name': 'tag_111', 'arch': 'x86_64'},
            {'id': 1121, 'repo_id': 121, 'tag_name': 'tag_121', 'arch': 'x86_64'}
        ]
        self.session.listBuildroots.return_value = multi_broots
        anon_handle_mock_config(self.options, self.session, arguments)
        expected = "Multiple buildroots found: %s" % [br['id'] for br in multi_broots]
        self.assert_console_message(stdout, "%s\n\n" % expected)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        opts = self.common_opts.copy()
        opts.update({
            'repoid': 'latest',
            'tag_name': multi_broots[0]['tag_name'],
            'tag_macros': {},
        })
        del opts['topurl']
        arguments = self.common_args + ['--task', str(task_id),
                                        '--name', self.progname,
                                        '--latest']
        self.session.listBuildroots.return_value = [multi_broots[0]]
        self.gen_config_mock.return_value = self.mock_output
        anon_handle_mock_config(self.options, self.session, arguments)
        self.assert_console_message(stdout, "%s\n" % self.gen_config_mock.return_value)
        self.gen_config_mock.assert_called_with(self.progname, multi_broots[0]['arch'], **opts)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

    @mock.patch('sys.stderr', new_callable=six.StringIO)
    @mock.patch('sys.stdout', new_callable=six.StringIO)
    def test_handle_mock_config_tag_option(self, stdout, stderr):
        """Test anon_handle_mock_config with tag option"""
        tag = {'id': 201, 'name': 'tag', 'arch': 'x86_64'}
        self.session.getTag.return_value = None
        self.session.getBuildConfig.return_value = None
        self.session.getRepo.return_value = None

        arguments = ['--tag', tag['name']]
        expected = "Please specify an arch\n"
        self.assert_system_exit(
            anon_handle_mock_config,
            self.options, self.session, arguments,
            stderr=expected,
            exit_code=1,
            activate_session=None)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        arguments = ['--tag', tag['name'], '--arch', tag['arch']]
        expected = self.format_error_message("No such tag: %s" % tag['name'])
        self.assert_system_exit(
            anon_handle_mock_config,
            self.options, self.session, arguments,
            stderr=expected,
            exit_code=2,
            activate_session=None)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        # return tag info
        self.session.getTag.return_value = tag
        expected = "Could not get config info for tag: %(name)s\n" % tag
        self.assert_system_exit(
            anon_handle_mock_config,
            self.options, self.session, arguments,
            stderr=expected,
            exit_code=1,
            activate_session=None)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        # return build config
        self.session.getBuildConfig.return_value = {
            'id': 301,
            'extra': {
                'rpm.macro.random_macro1': 'random_macro_content1',
                'rpm.macro.random_macro2': 'random_macro_content2',
                'mock.package_manager': 'yum',
                'mock.yum.module_hotfixes': 1,
                'mock.forcearch': True,
                'mock.yum.best': 10,
                'mock.bootstrap_image': 'bootstrap_image_content',
                'mock.use_bootstrap': True,
                'mock.module_setup_commands': 'module_setup_commands_content',
                'mock.releasever': 'releasever_content',
            },
            'arches': 'x86_64',
        }
        expected = "Could not get a repo for tag: %(name)s\n" % tag
        self.assert_system_exit(
            anon_handle_mock_config,
            self.options, self.session, arguments,
            stderr=expected,
            exit_code=1,
            activate_session=None)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        # return repo
        self.session.getRepo.return_value = {'id': 101}
        self.gen_config_mock.return_value = self.mock_output
        anon_handle_mock_config(self.options, self.session, arguments)
        self.assert_console_message(stdout, "%s\n" % self.gen_config_mock.return_value)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        arguments = self.common_args + ['--tag', tag['name'],
                                        '--arch', tag['arch'],
                                        '--name', self.progname,
                                        '--latest']
        opts = self.common_opts.copy()
        opts.update({
            'repoid': 'latest',
            'tag_name': tag['name'],
            'tag_macros': {
                '%random_macro1': 'random_macro_content1',
                '%random_macro2': 'random_macro_content2',
            },
            'package_manager': 'yum',
            'module_hotfixes': 1,
            'bootstrap_image': 'bootstrap_image_content',
            'forcearch': 'x86_64',
            'module_setup_commands': 'module_setup_commands_content',
            'releasever': 'releasever_content',
            'use_bootstrap': True,
            'use_bootstrap_image': True,
            'yum_best': 10,
        })

        del opts['topurl']
        anon_handle_mock_config(self.options, self.session, arguments)
        self.assert_console_message(stdout, "%s\n" % self.gen_config_mock.return_value)
        self.gen_config_mock.assert_called_with(self.progname, tag['arch'], **opts)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        # return arch warning and config
        arch = 'test'
        warn_msg = '%s is not in the list of tag arches' % arch
        self.gen_config_mock.return_value = self.mock_output
        arguments = self.common_args + ['--tag', tag['name'], '--arch', arch,
                                        '--name', self.progname, '--latest']
        anon_handle_mock_config(self.options, self.session, arguments)
        self.assert_console_message(stdout, "%s\n" % self.gen_config_mock.return_value)
        self.assert_console_message(stderr, "%s\n" % warn_msg)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        # return warning that tag arch is empty
        self.session.getBuildConfig.return_value = {
            'id': 301,
            'extra': {
                'rpm.macro.random_macro1': 'random_macro_content1',
                'rpm.macro.random_macro2': 'random_macro_content2',
                'mock.package_manager': 'yum',
                'mock.yum.module_hotfixes': 1,
            },
            'arches': None,
        }
        arch = 'test'
        warn_msg = 'Tag %s has an empty arch list' % tag['name']
        self.gen_config_mock.return_value = self.mock_output
        arguments = self.common_args + ['--tag', tag['name'], '--arch', arch,
                                        '--name', self.progname, '--latest']
        anon_handle_mock_config(self.options, self.session, arguments)
        self.assert_console_message(stdout, "%s\n" % self.gen_config_mock.return_value)
        self.assert_console_message(stderr, "%s\n" % warn_msg)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

    @mock.patch('sys.stderr', new_callable=six.StringIO)
    @mock.patch('sys.stdout', new_callable=six.StringIO)
    @mock.patch('koji_cli.commands.open')
    def test_handle_mock_config_target_option(self, openf, stdout, stderr):
        """Test anon_handle_mock_config with target option"""
        arch = "x86_64"
        target = {'id': 1,
                  'name': 'target',
                  'dest_tag': 1,
                  'build_tag': 2,
                  'build_tag_name': 'target-build',
                  'dest_tag_name': 'target'}
        self.session.getBuildTarget.return_value = None
        self.session.getRepo.return_value = None

        arguments = ['--target', target['name']]
        expected = "Please specify an arch\n"
        self.assert_system_exit(
            anon_handle_mock_config,
            self.options, self.session, arguments,
            stderr=expected,
            exit_code=1,
            activate_session=None)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        arguments = ['--target', target['name'],
                     '--arch', arch]
        expected = self.format_error_message("No such build target: %s" % target['name'])
        self.assert_system_exit(
            anon_handle_mock_config,
            self.options, self.session, arguments,
            stderr=expected,
            exit_code=2,
            activate_session=None)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        self.session.getBuildTarget.return_value = target
        self.session.getBuildConfig.return_value = {'arches': 'x86_64', 'extra': {}}
        expected = "Could not get a repo for tag: %s\n" % target['build_tag_name']
        self.assert_system_exit(
            anon_handle_mock_config,
            self.options, self.session, arguments,
            stderr=expected,
            exit_code=1,
            activate_session=None)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        arguments = ['--distribution', 'fedora', '--topurl', '/top-url',
                     '--yum-proxy', '/yum-proxy', '--target', target['name'], '--arch', arch,
                     '--name', self.progname]
        opts = self.common_opts.copy()
        opts.update({
            'repoid': 101,
            'tag_name': target['build_tag_name'],
            'tag_macros': {},
        })
        del opts['topdir']
        self.session.getRepo.return_value = {'id': 101}
        self.gen_config_mock.return_value = self.mock_output
        anon_handle_mock_config(self.options, self.session, arguments)
        self.assert_console_message(stdout, "%s\n" % self.gen_config_mock.return_value)
        self.gen_config_mock.assert_called_with(self.progname, arch, **opts)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        # --latest and -o (output) test
        opts['repoid'] = 'latest'
        arguments.extend(['--latest', '-o', '/tmp/mock.out'])
        fobj = mock.MagicMock()
        openf.return_value.__enter__.return_value = fobj
        anon_handle_mock_config(self.options, self.session, arguments)
        openf.assert_called_once()
        fobj.write.assert_called_once_with(self.mock_output)
        self.gen_config_mock.assert_called_with(self.progname, arch, **opts)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        # return arch warning and config
        arch = 'test'
        arguments = self.common_args + ['--target', target['name'],
                                        '--arch', arch,
                                        '--name', self.progname]
        warn_msg = '%s is not in the list of tag arches' % arch
        self.gen_config_mock.return_value = self.mock_output
        anon_handle_mock_config(self.options, self.session, arguments)
        self.assert_console_message(stdout, "%s\n" % self.gen_config_mock.return_value)
        self.assert_console_message(stderr, "%s\n" % warn_msg)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

    def test_handle_mock_config_errors(self):
        """Test anon_handle_mock_config general error messages"""
        arguments = []

        # Run it and check immediate output
        # argument is empty
        expected = self.format_error_message(
            "Please specify one of: --tag, --target, --task, --buildroot")
        self.assert_system_exit(
            anon_handle_mock_config,
            self.options, self.session, arguments,
            stderr=expected,
            activate_session=None)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

        # name is specified twice case
        arguments = [self.progname, '--name', 'name']
        expected = self.format_error_message("Name already specified via option")
        self.assert_system_exit(
            anon_handle_mock_config,
            self.options, self.session, arguments,
            stderr=expected,
            activate_session=None)
        self.ensure_connection_mock.assert_called_once_with(self.session, self.options)
        self.ensure_connection_mock.reset_mock()

    def test_handle_mock_config_help(self):
        """Test anon_handle_mock_config help message full output"""
        self.assert_help(
            anon_handle_mock_config,
            """Usage: %s mock-config [options]
(Specify the --help global option for a list of other help options)

Options:
  -h, --help            show this help message and exit
  -a ARCH, --arch=ARCH  Specify the arch
  -n NAME, --name=NAME  Specify the name for the buildroot
  --tag=TAG             Create a mock config for a tag
  --target=TARGET       Create a mock config for a build target
  --task=TASK           Duplicate the mock config of a previous task
  --latest              use the latest redirect url
  --buildroot=BUILDROOT
                        Duplicate the mock config for the specified buildroot
                        id
  --mockdir=DIR         Specify mockdir
  --topdir=DIR          Specify topdir, topdir tops the topurl
  --topurl=URL          URL under which Koji files are accessible, when topdir
                        is specified, topdir tops the topurl
  --distribution=DISTRIBUTION
                        Change the distribution macro
  --yum-proxy=YUM_PROXY
                        Specify a yum proxy
  -o FILE               Output to a file
""" % self.progname)


if __name__ == '__main__':
    unittest.main()