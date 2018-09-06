from django.core.exceptions import ValidationError
import time
import re

def validate_year(value):

    """
        Validator function for model.IntegerField()
        * Validates a valid four-digit year.
        * Must be a current or past year.
        In your model:
        year = models.IntegerField(_(u'Year'), help_text=_(u'Current or past year in YYYY format.'), validators=[validate_year], unique=True)
    """

    # Matches any 4-digit number:
    year_re = re.compile('^\d{4}$')

    # If year does not match our regex:
    if not year_re.match(str(value)):
        raise ValidationError(u'%s is not a valid year.' % value)

    # Check not before this year:
    year = int(value)
    thisyear = time.localtime()[0]
    if year > thisyear:
        raise ValidationError(u'%s is a year in the future; please enter a current or past year.' % value)
