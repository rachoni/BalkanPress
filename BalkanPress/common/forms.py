from django import forms


class BootStrapModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            widget = field.widget

            # Skip checkboxes
            if not isinstance(widget, forms.CheckboxInput):
                css_class = widget.attrs.get("class", "")
                widget.attrs["class"] = f"{css_class} form-control".strip()


class ReadOnlyModelForm(forms.ModelForm):
    readonly_exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name not in self.readonly_exclude:
                field.disabled = True
                field.required = False

                css_class = field.widget.attrs.get("class", "")
                field.widget.attrs["class"] = f"{css_class} bg-light".strip()

                # Some widgets need explicit disabled attribute
                field.widget.attrs["disabled"] = True
