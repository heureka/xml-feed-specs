"""CLI entry point for Heureka documentation generator."""

import argparse
import sys
from pathlib import Path

from .generator import generate_documentation


def main() -> None:
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Generate MkDocs documentation from Heureka XML field definitions"
    )
    parser.add_argument(
        "--template-dir",
        type=Path,
        default="templates",
        help="Directory containing Jinja2 templates (default: templates)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default="docs",
        help="Output directory for generated documentation (default: docs)",
    )

    args = parser.parse_args()

    # Validate template directory exists
    if not args.template_dir.exists():
        print(f"Error: Template directory '{args.template_dir}' does not exist")
        sys.exit(1)

    # Check for required templates
    required_templates = ["field.md.j2", "index.md.j2"]
    missing_templates = []

    for template in required_templates:
        template_path = args.template_dir / template
        if not template_path.exists():
            missing_templates.append(template)

    if missing_templates:
        print(f"Error: Missing required templates: {', '.join(missing_templates)}")
        sys.exit(1)

    try:
        generate_documentation(args.template_dir, args.output_dir)
        print("Documentation generation completed successfully!")
    except Exception as e:
        print(f"Error generating documentation: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
