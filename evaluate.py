#! /usr/bin/env python

# /// script
# dependencies = [
#   "requests",
#   "pyyaml"
# ]
# ///

# Copyright 2025 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Evaluate a charm for listing on Charmhub.

This script automates as much of the charm listing review process as possible,
providing the results to the review in a comment on the listing request GitHub
issue.

Not all checks for listing can be automated. This script provides a head-start
for the reviewer, and is also a way for charm publishers to check their charm
against the listing requirements before submitting a listing request.
"""

import pathlib
import shutil
import subprocess  # noqa: S404
import tempfile
import tomllib

import requests
import yaml


def evaluate(
    repository_url: str,
    linting_url: str,
    contribution_url: str,
    license_url: str,
    security_url: str,
) -> str:
    """Evaluate the charm for listing on Charmhub."""
    results = []
    repo_dir = _clone_repo(repository_url)
    try:
        results.append(coding_conventions(linting_url))
        results.append(contribution_guidelines(contribution_url))
        results.append(license_statement(license_url))
        results.append(security_doc(security_url))
        results.append(metadata_links(repo_dir))
        results.append(action_names(repo_dir))
        results.append(option_names(repo_dir))
        results.append(relations_includes_optional(repo_dir))
        results.append(charmcraft_tooling(repo_dir))
        results.append(charm_plugin_strict_dependencies(repo_dir))
        results.append(python_requires_version(repo_dir))
    finally:
        shutil.rmtree(str(repo_dir), ignore_errors=True)
    return '\n'.join(results)


def coding_conventions(linting_url: str) -> str:
    """Checks for coding conventions are reasonable and implemented in CI.

    The source code of the charm is accessible in the sense of approachability.
    Consistent source code style and formatting are also considered a sign of
    being committed to quality.
    """
    try:
        response = requests.get(linting_url, allow_redirects=True, timeout=5)
        if not response.ok:
            return '[ ] The charm implements coding conventions in CI.'
    except requests.RequestException:
        return '[ ] The charm implements coding conventions in CI.'
    content = response.text.lower()
    try:
        workflow = yaml.safe_load(content)
    except Exception:
        return '[ ] The charm implements coding conventions in CI.'
    keywords = ['make lint', 'just lint', 'tox -e lint']
    try:
        jobs = workflow.get('jobs', {})
        for job in jobs.values():
            steps = job.get('steps', [])
            for step in steps:
                run_cmd = step.get('run', '')
                if any(keyword in run_cmd for keyword in keywords):
                    return '[x] The charm implements coding conventions in CI.'
    except Exception:  # noqa: S110  We should add logging here later.
        pass
    return '[ ] The charm implements coding conventions in CI.'


def contribution_guidelines(contribution_url: str) -> str:
    """The documentation for contribution resolves with a 2xx status code.

    The documentation for contributing to the charm should be separate from the
    documentation for developing or using the charm.
    """
    # Ideally, this would also check that the content of the URL is actually a
    # reasonable contribution guide, but that is more difficult to automate.
    try:
        response = requests.head(contribution_url, allow_redirects=True, timeout=5)
        if response.ok:
            return '[x] The charm provides contribution guidelines.'
        return '[ ] The charm provides contribution guidelines.'
    except requests.RequestException:
        return '[ ] The charm provides contribution guidelines.'


def license_statement(license_url: str) -> str:
    """The charm's license statement resolves with a 2xx status code.

    For the charm shared, OSS or not, the licensing terms of the charm are
    clarified (which also implies an identified authorship of the charm).
    """
    try:
        response = requests.head(license_url, allow_redirects=True, timeout=5)
        if response.ok:
            return '[x] The charm provides a license statement.'
        return '[ ] The charm provides a license statement.'
    except requests.RequestException:
        return '[ ] The charm provides a license statement.'


def security_doc(security_url: str) -> str:
    """The charm's security documentation resolves with a 2xx status code.

    The charm's security documentation explains which versions are supported,
    and how to report security issues.
    """
    # Ideally, this would also check some of the content of the security doc,
    # like that it has a section on how to report security issues.
    try:
        response = requests.head(security_url, allow_redirects=True, timeout=5)
        if response.ok:
            return '[x] The charm provides a security statement.'
        return '[ ] The charm provides a security statement.'
    except requests.RequestException:
        return '[ ] The charm provides a security statement.'


def _clone_repo(charm_repo_url: str) -> pathlib.Path:
    """Clone the charm repository to a temporary directory."""
    temp_dir = tempfile.mkdtemp()
    try:
        subprocess.run(  # noqa: S603  We should validate the safety of the URL, but also: in CI.
            ['/usr/bin/git', 'clone', '--depth', '1', charm_repo_url, temp_dir],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return pathlib.Path(temp_dir)
    except subprocess.CalledProcessError:
        shutil.rmtree(temp_dir)
        raise


def _get_charmcraft_yaml(repo_dir: pathlib.Path) -> dict:
    charmcraft_path = repo_dir / 'charmcraft.yaml'
    if not charmcraft_path.is_file():
        return None
    try:
        with charmcraft_path.open() as f:
            return yaml.safe_load(f)
    except Exception:
        return None


def metadata_links(repo_dir: pathlib.Path) -> str:
    """charmcraft.yaml includes the name, title, summary, and description.

    A complete and consistent appearance of the charm is required.

    The repository contains a `charmcraft.yaml` file that includes fields for
    name, title, summary, and description that are not the default profile
    values. A links field includes fields for documentation, issues, source,
    and contact, which all resolve with a 2xx status code.
    """
    data = _get_charmcraft_yaml(repo_dir)
    default_desc = """A single sentence that says what the charm is, concisely and memorably.

A paragraph of one to three short sentences, that describe what the charm does.

A third paragraph that explains what need the charm meets.

Finally, a paragraph that describes whom the charm is useful for.\n"""
    required_fields = {
        'name': '',
        'title': 'Charm Template',
        'summary': 'A very short one-line summary of the charm.',
        'description': default_desc,
    }
    for field, default in required_fields.items():
        value = data.get(field, '')
        if not value or value == default:
            return '[ ] charmcraft.yaml includes required metadata.'

    links = data.get('links', {})
    link_fields = ['documentation', 'issues', 'source', 'contact']
    for field in link_fields:
        url = links.get(field)
        if not url:
            return '[ ] charmcraft.yaml includes required metadata.'
        try:
            resp = requests.head(url, allow_redirects=True, timeout=5)
            if not resp.ok:
                return '[ ] charmcraft.yaml includes required metadata.'
        except requests.RequestException:
            return '[ ] charmcraft.yaml includes required metadata.'

    return '[x] charmcraft.yaml includes required metadata.'


def _validate_action_or_config_name(name: str) -> bool:
    """Validate that the action or config name follows best practices."""
    if not name.islower():
        return False
    if not all(c.isalnum() or c == '-' for c in name):
        return False
    if '--' in name or name.startswith('-') or name.endswith('-'):
        return False
    return True


def action_names(repo_dir: pathlib.Path) -> str:
    """The charm's actions are named according to the best practices.

    The charm's actions are named using lowercase alphanumeric names, with
    hyphens (-) to separate words.

    The repository contains a `charmcraft.yaml` file that includes an actions
    field, and each action is named appropriately.
    """
    data = _get_charmcraft_yaml(repo_dir)
    if not data or 'actions' not in data:
        return "[ ] The charm's actions are named according to best practices."
    actions = data.get('actions', {})
    for name in actions:
        if not _validate_action_or_config_name(name):
            return "[ ] The charm's actions are named according to best practices."
    return "[x] The charm's actions are named according to best practices."


def option_names(repo_dir: pathlib.Path) -> str:
    """The charm's config options are named according to the best practices.

    The charm's config options are named using lowercase alphanumeric names,
    with hyphens (-) to separate words.

    The repository contains a `charmcraft.yaml` file that includes a config
    field, itself containing an options field, and each option is named
    appropriately.
    """
    data = _get_charmcraft_yaml(repo_dir)
    if not data or 'config' not in data:
        return "[ ] The charm's config options are named according to best practices."
    options = data.get('config', {}).get('options', {})
    for name in options:
        if not _validate_action_or_config_name(name):
            return "[ ] The charm's config options are named according to best practices."
    return "[x] The charm's config options are named according to best practices."


def relations_includes_optional(repo_dir: pathlib.Path) -> str:
    """The charm's relations include the optional key.

    Always include the ``optional`` key, rather than relying on the default
    value to indicate that the relation is required. Although this field is not
    enforced by Juju, including it makes it clear to users (and other tools)
    whether the relation is required.

    The charm's relations are defined in the `charmcraft.yaml` file, in requires
    and provides fields, and each relation includes the `optional` key.
    """
    data = _get_charmcraft_yaml(repo_dir)
    if not data:
        return "[ ] The charm's relations include the optional key."
    for section in ('requires', 'provides'):
        endpoints = data.get(section, {})
        for config in endpoints.values():
            if not isinstance(config, dict) or 'optional' not in config:
                return "[ ] The charm's relations include the optional key."
    return "[x] The charm's relations include the optional key."


def charmcraft_tooling(repo_dir: pathlib.Path) -> str:
    """The charm includes the expected tooling for linting and testing.

    The repository contains a Makefile, Justfile, or tox.ini that provides
    commands for formatting, linting, unit testing, and integration testing
    (other commands can also be included).
    """
    tooling_files = ['Makefile', 'Justfile', 'tox.ini']
    for filename in tooling_files:
        if (repo_dir / filename).is_file():
            break
    else:
        return '[ ] The charm includes expected tooling for linting and testing.'

    # Check for commands in the files
    commands = {'format', 'list', 'unit', 'integration'}
    found_commands = set()
    file_path = repo_dir / filename
    with file_path.open('r', encoding='utf-8') as f:
        content = f.read().lower()

    if filename == 'Makefile' or filename == 'Justfile':
        for command in commands:
            if f'{command}:' in content or f'{command} (' in content:
                found_commands.add(command)
    elif filename == 'tox.ini':
        for command in commands:
            if f'[testenv:{command}]' in content:
                found_commands.add(command)

    if all(command in found_commands for command in commands):
        return '[x] The charm includes expected tooling for linting and testing.'
    return '[ ] The charm includes expected tooling for linting and testing.'


def charm_plugin_strict_dependencies(repo_dir: pathlib.Path) -> str:
    """The charm plugin is configured with strict dependencies.

    When using the `charm` plugin with charmcraft, ensure that you set strict
    dependencies to true.

    The repository contains a `charmcraft.yaml` file that includes building the
    charm. If the charm uses the `charm` plugin, it should have a
    `strict-dependencies: true` field.
    """


def python_requires_version(repo_dir: pathlib.Path) -> str:
    """The charm's `pyproject.toml` specifies the required Python version.

    This ensures that tooling will detect any use of Python features not
    available in the versions you support.

    The repository contains a `pyproject.toml` file that includes a
    `requires-python` field with a version specifier.
    """
    pyproject_path = repo_dir / 'pyproject.toml'
    if not pyproject_path.is_file():
        return "[ ] The charm's pyproject.toml specifies the required Python version."
    try:
        with pyproject_path.open('rb') as f:
            data = tomllib.load(f)
    except Exception:
        return "[ ] The charm's pyproject.toml specifies the required Python version."
    requires_python = None
    if 'project' in data and 'requires-python' in data['project']:
        requires_python = data['project']['requires-python']
    elif 'tool' in data and 'poetry' in data['tool']:
        deps = data['tool']['poetry'].get('dependencies', {})
        requires_python = deps.get('python')
    if requires_python:
        return "[x] The charm's pyproject.toml specifies the required Python version."
    return "[ ] The charm's pyproject.toml specifies the required Python version."


if __name__ == '__main__':
    # For testing purposes.
    import argparse

    parser = argparse.ArgumentParser(description='Evaluate a charm for listing on Charmhub.')
    parser.add_argument('repository_url', help='The URL of the charm repository')
    parser.add_argument('linting_url', help='The URL of the linting configuration')
    parser.add_argument('contribution_url', help='The URL of the contribution guidelines')
    parser.add_argument('license_url', help='The URL of the license statement')
    args = parser.parse_args()

    print(evaluate(args.repository_url, args.linting_url, args.contribution_url, args.license_url))
