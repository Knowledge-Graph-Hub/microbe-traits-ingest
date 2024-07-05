"""microbe-traits-ingest package."""
from pathlib import Path

import importlib_metadata
from linkml.generators.pythongen import PythonGenerator
from linkml_runtime.utils.schemaview import SchemaView

try:
    __version__ = importlib_metadata.version(__name__)
except importlib_metadata.PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"  # pragma: no cover


# Define the path to the current file's directory
PWD = Path(__file__).parent
SCHEMA_DIR = PWD / "schema"
SCHEMA_YAML = SCHEMA_DIR / "traits.yaml"
SCHEMA_PYTHON = SCHEMA_DIR / "traits.py"

schema_view = SchemaView(SCHEMA_YAML)

# Generate the Python classes from the schema
python_generator = PythonGenerator(schema_view.schema)
python_code = python_generator.serialize()


# Write the generated Python code to the traits.py file within the kg_traits directory
with open(SCHEMA_PYTHON, "w") as f:
    f.write(python_code)
