"""Core data models for Heureka XML field definitions."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class FieldType(Enum):
    """Field data types."""

    STRING = "string"
    DECIMAL = "decimal"
    INTEGER = "integer"
    BOOLEAN = "boolean"


class ArchetypeType(Enum):
    """Field architecture patterns."""

    SIMPLE = "simple"
    COMPLEX_CONDITIONAL = "complex_conditional"
    ATTRIBUTE_BASED = "attribute_based"


@dataclass
class Field:
    """Base field model."""

    name: str
    field_type: FieldType
    archetype: ArchetypeType
    description: str
    required: bool = False
    multiple: bool = False
    max_occurs: int | None = None
    display_name: str | None = None
    category: str | None = None
    deprecated: bool = False
    deprecation_note: str | None = None
    max_length: int | None = None
    min_length: int | None = None
    pattern: str | None = None
    min_value: float | None = None
    max_value: float | None = None
    enum_values: list[str] | None = None
    examples: list[dict[str, Any]] | None = None
    related_fields: list[dict[str, str]] | None = None
    validation_rules: list[dict[str, Any]] | None = None
    conditional_validation: str | None = None
    child_elements: list["Field"] | None = None
    attributes: list["Field"] | None = None
    has_text_content: bool = False
    content_max_length: int | None = None

    def get_example_xml(self) -> list[str]:
        """Generate XML examples for this field."""
        if self.archetype == ArchetypeType.SIMPLE:
            return self._get_simple_examples()
        elif self.archetype == ArchetypeType.COMPLEX_CONDITIONAL:
            return self._get_complex_examples()
        elif self.archetype == ArchetypeType.ATTRIBUTE_BASED:
            return self._get_attribute_examples()
        return []  # type: ignore[unreachable]

    def _get_simple_examples(self) -> list[str]:
        """Generate simple field examples."""
        examples = []
        if self.examples:
            for example in self.examples:
                value = example.get("value", "example")
                examples.append(f"<{self.name}>{value}</{self.name}>")
        else:
            examples.append("No examples available")
        return examples

    def _get_complex_examples(self) -> list[str]:
        """Generate complex conditional field examples."""
        examples = []

        if self.child_elements:
            # Collect all possible example combinations
            child_examples = []
            has_any_examples = False

            for child in self.child_elements:
                if child.examples:
                    has_any_examples = True
                    for example in child.examples:
                        value = example.get("value", "example")
                        child_examples.append(f"  <{child.name}>{value}</{child.name}>")
                else:
                    # Include children without examples with placeholder
                    child_examples.append(f"  <{child.name}>example_value</{child.name}>")

            if has_any_examples and child_examples:
                examples.append(f"<{self.name}>\n" + "\n".join(child_examples) + f"\n</{self.name}>")
            elif child_examples:
                # Has children but no examples
                examples.append("No examples available")
        else:
            examples.append("No examples available")

        return examples

    def _get_attribute_examples(self) -> list[str]:
        """Generate attribute-based field examples."""
        examples = []
        has_any_examples = False

        if self.attributes:
            # Collect all attribute examples
            attr_combinations = []

            for attr in self.attributes:
                if attr.examples:
                    has_any_examples = True
                    for example in attr.examples:
                        value = example.get("value", "example_value")
                        attr_combinations.append(f'{attr.name}="{value}"')
                else:
                    # Include attributes without examples with placeholder
                    attr_combinations.append(f'{attr.name}="example_value"')

            if attr_combinations:
                attr_str = " " + " ".join(attr_combinations)

                if self.has_text_content:
                    # Use field's own examples for text content
                    text_content_values = []
                    if self.examples:
                        has_any_examples = True
                        for example in self.examples:
                            text_content_values.append(example.get("value", "example_text_content"))
                    else:
                        text_content_values.append("example_text_content")

                    if has_any_examples:
                        for text_content in text_content_values:
                            examples.append(f"<{self.name}{attr_str}>{text_content}</{self.name}>")
                    else:
                        examples.append("No examples available")
                else:
                    if has_any_examples:
                        examples.append(f"<{self.name}{attr_str}/>")
                    else:
                        examples.append("No examples available")
            else:
                examples.append("No examples available")
        else:
            examples.append("No examples available")

        return examples


@dataclass
class FieldCollection:
    """Collection of fields with utility methods."""

    fields: list[Field] = field(default_factory=list)
    version: str = "1.0"
    last_updated: str | None = None
    description: str | None = None

    def get_required_fields(self) -> list[Field]:
        """Get all required fields."""
        return [f for f in self.fields if f.required]

    def get_simple_fields(self) -> list[Field]:
        """Get all simple fields."""
        return [f for f in self.fields if f.archetype == ArchetypeType.SIMPLE]

    def get_complex_fields(self) -> list[Field]:
        """Get all complex conditional fields."""
        return [f for f in self.fields if f.archetype == ArchetypeType.COMPLEX_CONDITIONAL]

    def get_attribute_fields(self) -> list[Field]:
        """Get all attribute-based fields."""
        return [f for f in self.fields if f.archetype == ArchetypeType.ATTRIBUTE_BASED]

    def get_field_by_name(self, name: str) -> Field | None:
        """Get field by name."""
        for field_item in self.fields:
            if field_item.name == name:
                return field_item
        return None
