from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field
from editions.models import *
from places.models import *


class GenericFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.add_input(Submit('Filter', 'Filter'))
        self.layout = Layout(
            Fieldset(
            	'Basic search options',
            	'name',
            	'institution__name',
            	'manager__name',
            	'url',
            	'historical_period',
            	'language',
                'country_name',
            	css_id="basic_search_fields"),
            Fieldset(
            	'Advanced search options',
                'city_name',
            	'scholarly',
            	'digital',
            	'edition',
            	'prototype',
            	'writing_support',
            	'begin_date',
            	'end_date',
            	'audience',
            	'philological_statement',
            	'textual_variance',
            	'value_witnesses',
            	'tei_transcription',
            	'download',
            	'images',
            	'zoom_images',
            	'image_manipulation',
            	'text_image',
            	'source_translation',
            	'website_language',
            	'glossary',
            	'indices',
            	'search',
            	'advanced_search',
            	'cc_license',
            	'open_source',
            	'infrastructure',
            	'key_or_ocr',
            	'print_friendly',
            	css_id="advanced_search_fields"
            	),
        )

