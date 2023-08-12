"""Core utils."""


def set_bootstrap_class(fields):
    """Set Bootstrap classes for specific fields."""
    classes_dict = {
        'CharField': {
            'field': 'form-control',
            'label': '',
        },
        'IntegerField': {
            'field': 'form-control',
            'label': '',
        },
        'EmailField': {
            'field': 'form-control',
            'label': '',
        },
        'ChoiceField': {
            'field': 'form-control bs-select',
            'label': '',
        },
        'SlugField': {
            'field': 'form-control',
            'label': '',
        },
        'TypedChoiceField': {
            'field': 'form-control bs-select',
            'label': '',
        },
        'PasswordField': {
            'field': 'form-control',
            'label': '',
        },
        'SetPasswordField': {
            'field': 'form-control',
            'label': '',
        },
        'BooleanField': {
            'field': 'form-check-input',
            'label': '',
        },
        'ModelChoiceField': {
            'field': 'form-control bs-select',
            'label': '',
        },
        'RegexField': {
            'field': 'form-control',
            'label': '',
        },
        'TreeNodeChoiceField': {
            'field': 'form-control bs-select',
            'label': '',
        },
        'ModelMultipleChoiceField': {
            'field': 'bs-select',
            'label': '',
        },
        'ImageField': {
            'field': '',
            'label': '',
        },
        'FileField': {
            'field': '',
            'label': '',
        },
        'MoneyField': {
            'field': 'form-control',
            'label': '',
        },
        'DecimalField': {
            'field': 'form-control',
            'label': '',
        },
        'DateField': {
            'field': 'form-control custom-datepicker',
            'label': '',
        },
        'DateTimeField': {
            'field': 'form-control custom-datepicker',
            'label': '',
        },
        'DurationField': {
            'field': 'form-control',
            'label': '',
        },
        'SimpleArrayField': {
            'field': 'form-control',
            'label': '',
        },
        'URLField': {
            'field': 'form-control',
            'label': '',
        },
        'NullCharField': {
            'field': 'form-control',
            'label': '',
        },
        'MultipleFileField': {
            'field': '',
            'label': '',
        },
        'FloatField': {
            'field': 'form-control',
            'label': '',
        },
        'PhoneNumberField': {
            'field': 'form-control',
            'label': '',
        },
    }
    for _, field in fields.items():
        try:
            field.widget.attrs.update(
                {
                    'class': classes_dict[field.__class__.__name__]['field'],
                },
            )
        except KeyError:
            pass
