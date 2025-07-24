"""Documentation generator using Jinja2 templates."""

from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader

from .fields import create_field_collection
from .models import Field, FieldCollection


def snake_to_title(text: str) -> str:
    """Convert snake_case to Title Case."""
    return text.replace("_", " ").title()


def truncate(text: str, length: int = 100) -> str:
    """Truncate text to specified length."""
    if len(text) <= length:
        return text
    return text[:length].rstrip() + "..."


def format_examples(examples: list[dict[str, Any]]) -> str:
    """Format examples for display."""
    if not examples:
        return ""

    formatted = []
    for example in examples:
        if "value" in example:
            formatted.append(f"- `{example['value']}`")
        elif "description" in example:
            formatted.append(f"- {example['description']}")

    return "\n".join(formatted)


class DocumentationGenerator:
    """Generate MkDocs documentation from field definitions."""

    def __init__(self, template_dir: str | Path, output_dir: str | Path) -> None:
        """Initialize generator with template and output directories."""
        self.template_dir = Path(template_dir)
        self.output_dir = Path(output_dir)

        # Set up Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(str(self.template_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
        )

        # Add custom filters
        self.env.filters["snake_to_title"] = snake_to_title
        self.env.filters["truncate"] = truncate
        self.env.filters["format_examples"] = format_examples

        # Load templates
        self.field_template = self.env.get_template("field.md.j2")
        self.index_template = self.env.get_template("index.md.j2")

    def generate_all(self) -> None:
        """Generate all documentation files."""
        collection = create_field_collection()

        # Create output directories
        self.output_dir.mkdir(parents=True, exist_ok=True)
        fields_dir = self.output_dir / "fields"
        fields_dir.mkdir(exist_ok=True)

        # Generate field pages
        self._generate_field_pages(collection.fields, fields_dir)

        # Generate index page
        self._generate_index_page(collection, self.output_dir)

    def _generate_field_pages(self, fields: list[Field], output_dir: Path) -> None:
        """Generate individual field documentation pages."""
        for field in fields:
            content = self.field_template.render(field=field)
            filename = f"{field.name.lower()}.md"
            output_path = output_dir / filename

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"Generated {output_path}")

    def _generate_index_page(self, collection: FieldCollection, output_dir: Path) -> None:
        """Generate index page with overview."""
        content = self.index_template.render(collection=collection)
        output_path = output_dir / "index.md"

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Generated {output_path}")


def generate_documentation(
    template_dir: str | Path = "templates",
    output_dir: str | Path = "docs",
) -> None:
    """Generate documentation with default paths."""
    generator = DocumentationGenerator(template_dir, output_dir)
    generator.generate_all()
    print(f"Documentation generated in {output_dir}")


if __name__ == "__main__":
    generate_documentation()
