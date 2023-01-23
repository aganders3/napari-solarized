import importlib_resources
import pytest
from npe2.cli import app
from typer.testing import CliRunner

runner = CliRunner()


@pytest.fixture
def manifest_path():
    with importlib_resources.as_file(
        importlib_resources.files("napari_solarized") / "napari.yaml"
    ) as path:
        yield path


def test_manifest(manifest_path):
    result = runner.invoke(app, ["validate", str(manifest_path)])
    assert result.exit_code == 0
