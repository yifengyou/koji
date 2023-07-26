from __future__ import absolute_import

import mock
import pprint
from six.moves import StringIO

from koji_cli.commands import anon_handle_show_groups
from . import utils


class TestShowGroups(utils.CliTestCase):

    def setUp(self):
        self.maxDiff = None
        self.options = mock.MagicMock()
        self.session = mock.MagicMock()
        self.ensure_connection_mock = mock.patch('koji_cli.commands.ensure_connection').start()
        self.stderr = mock.patch('sys.stderr', new_callable=StringIO).start()
        self.stdout = mock.patch('sys.stdout', new_callable=StringIO).start()
        self.error_format = """Usage: %s show-groups [options] <tag>
(Specify the --help global option for a list of other help options)

%s: error: {message}
""" % (self.progname, self.progname)
        self.tag = 'test-tag'
        self.tag_groups = [
            {'grouplist': [],
             'packagelist': [],
             'description': None,
             'uservisible': True,
             'tag_id': 3,
             'is_default': None,
             'biarchonly': False,
             'exported': True,
             'blocked': True,
             'display_name': 'group-1',
             'name': 'group-1',
             'langonly': None,
             'group_id': 2},
            {'grouplist': [],
             'packagelist': [],
             'description': None,
             'uservisible': True,
             'tag_id': 5,
             'is_default': None,
             'biarchonly': False,
             'exported': True,
             'blocked': False,
             'display_name': 'group-2',
             'name': 'group-2',
             'langonly': None,
             'group_id': 3}
        ]

    def test_show_groups_incorrect_num_of_args(self):
        arguments = []
        self.assert_system_exit(
            anon_handle_show_groups,
            self.options, self.session, arguments,
            stdout='',
            stderr=self.format_error_message('Incorrect number of arguments'),
            exit_code=2,
            activate_session=None)
        self.ensure_connection_mock.assert_not_called()

    def test_show_groups_show_blocked_and_comps(self):
        arguments = ['--show-blocked', '--comps', self.tag]
        self.assert_system_exit(
            anon_handle_show_groups,
            self.options, self.session, arguments,
            stdout='',
            stderr=self.format_error_message(
                "--show-blocked doesn't make sense for comps/spec output"),
            exit_code=2,
            activate_session=None)
        self.ensure_connection_mock.assert_not_called()

    def test_show_groups_show_blocked_and_spec(self):
        arguments = ['--show-blocked', '--spec', self.tag]
        self.assert_system_exit(
            anon_handle_show_groups,
            self.options, self.session, arguments,
            stdout='',
            stderr=self.format_error_message(
                "--show-blocked doesn't make sense for comps/spec output"),
            exit_code=2,
            activate_session=None)
        self.ensure_connection_mock.assert_not_called()

    def test_show_groups_blocked(self):
        self.session.getTagGroups.return_value = self.tag_groups
        rv = anon_handle_show_groups(self.options, self.session, [self.tag, '--show-blocked'])
        self.assertEqual(rv, None)
        self.assert_console_message(self.stdout, pprint.pprint(self.tag_groups))
        self.assert_console_message(self.stderr, "")
        self.session.getTagGroups.assert_called_once_with(self.tag, incl_blocked=True)

    def test_show_groups_comps(self):
        expected_output = """<?xml version="1.0"?>
<!DOCTYPE comps PUBLIC "-//Red Hat, Inc.//DTD Comps info//EN" "comps.dtd">

<!-- Auto-generated by the build system -->
<comps>
  <group>
    <id>group-2</id>
    <name>group-2</name>
    <description>None</description>
    <default>false</default>
    <uservisible>true</uservisible>
    <packagelist>
    </packagelist>
  </group>
</comps>

"""
        self.session.getTagGroups.return_value = [self.tag_groups[1]]
        rv = anon_handle_show_groups(self.options, self.session, [self.tag, '--comps'])
        self.assertEqual(rv, None)
        self.assert_console_message(self.stdout, expected_output)
        self.assert_console_message(self.stderr, "")
        self.session.getTagGroups.assert_called_once_with(self.tag)

    def test_show_groups_comps_with_expand(self):
        expected_output = """<?xml version="1.0"?>
<!DOCTYPE comps PUBLIC "-//Red Hat, Inc.//DTD Comps info//EN" "comps.dtd">

<!-- Auto-generated by the build system -->
<comps>
  <group>
    <id>group-2</id>
    <name>group-2</name>
    <description>None</description>
    <default>false</default>
    <uservisible>true</uservisible>
    <packagelist>
    </packagelist>
  </group>
</comps>

"""
        self.session.getTagGroups.return_value = [self.tag_groups[1]]
        rv = anon_handle_show_groups(self.options, self.session, [self.tag, '--comps', '--expand'])
        self.assertEqual(rv, None)
        self.assert_console_message(self.stdout, expected_output)
        self.assert_console_message(self.stderr, "")
        self.session.getTagGroups.assert_called_once_with(self.tag)

    def test_show_groups_spec(self):
        expected_output = """#
# This specfile represents buildgroups for mock
# Autogenerated by the build system
#
Summary: The base set of packages for a mock chroot
Name: buildgroups
Version: 1
Release: 1
License: GPL
Group: Development/Build Tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

#package requirements
#MISSING GROUP: build

%description
This is a meta-package that requires a defined group of packages

%prep
%build
%install
%clean

%files
%defattr(-,root,root,-)
%doc

"""
        self.session.getTagGroups.return_value = [self.tag_groups[1]]
        rv = anon_handle_show_groups(self.options, self.session, [self.tag, '--spec'])
        self.assertEqual(rv, None)
        self.assert_console_message(self.stdout, expected_output)
        self.assert_console_message(self.stderr, "")
        self.session.getTagGroups.assert_called_once_with(self.tag)

    def test_show_groups_help(self):
        self.assert_help(
            anon_handle_show_groups,
            """Usage: %s show-groups [options] <tag>
(Specify the --help global option for a list of other help options)

Options:
  -h, --help      show this help message and exit
  --comps         Print in comps format
  -x, --expand    Expand groups in comps format
  --spec          Print build spec
  --show-blocked  Show blocked packages
""" % self.progname)
        self.ensure_connection_mock.assert_not_called()