<#
.SYNOPSIS
Makefile

.DESCRIPTION
USAGE
    .\make.ps1 <command>

COMMANDS
    init              install Python build tools
    install-dev       install local package in editable mode
    update-deps       update the dependencies
    upgrade-deps      upgrade the dependencies
    lint              run `isort` and `black`
    test              run `pytest`
    build-dist        run `python -m build`
    clean             delete generated content
    help, -?          show this help message
#>
param(
    [Parameter(Position = 0)]
    [ValidateSet("init", "install-dev", "update-deps", "upgrade-deps", "lint", "test", "build-dist", "clean", "help")]
    [string]$Command
)

function Invoke-Help
{
    Get-Help $PSCommandPath
}

function Invoke-Init
{
    python -m pip install --upgrade pip wheel setuptools build
}

function Invoke-Install-Dev
{
    python -m pip install --upgrade --editable ".[dev, tests, docs]"
}

function Invoke-Update-Deps
{
    python -m pip install --upgrade --editable ".[dev, tests, docs]"
    python -m pip install --upgrade pip-tools
    pip-compile --no-emit-index-url requirements/requirements.in
    pip-compile --no-emit-index-url requirements/requirements-dev.in
    pip-compile --no-emit-index-url requirements/requirements-tests.in
    pip-compile --no-emit-index-url requirements/requirements-docs.in
}

function Invoke-Upgrade-Deps
{
    python -m pip install --upgrade pip-tools pre-commit
    pre-commit autoupdate
    pip-compile --upgrade --no-emit-index-url requirements/requirements.in
    pip-compile --upgrade --no-emit-index-url requirements/requirements-dev.in
    pip-compile --upgrade --no-emit-index-url requirements/requirements-tests.in
    pip-compile --upgrade --no-emit-index-url requirements/requirements-docs.in
}

function Invoke-Lint
{
    pre-commit run --all-files
    python -m black .
    python -m ruff --fix .
}

function Invoke-Test
{
    python -m pytest
}

function Invoke-Build-Dist
{
    python -m pip install --upgrade build
    python -m build
}

function Invoke-Clean
{
    $folders = @("build", "dist")
    foreach ($folder in $folders)
    {
        if (Test-Path $folder)
        {

            Write-Verbose "Deleting $folder"
            Remove-Item $folder -Recurse -Force
        }
    }
}

switch ($Command)
{
    "init"    {
        Invoke-Init
    }
    "install-dev" {
        Invoke-Install-Dev
    }
    "lint"  {
        Invoke-Lint
    }
    "update-deps"  {
        Invoke-Update-Deps
    }
    "upgrade-deps"  {
        Invoke-Upgrade-Deps
    }
    "test"    {
        Invoke-Test
    }
    "build-dist"    {
        Invoke-Build-Dist
    }
    "clean"    {
        Invoke-Clean
    }
    "help"  {
        Invoke-Help
    }
    default
    {
        Invoke-Init
        Invoke-Install-Dev
    }
}
