from import_export import resources, fields
from .models import (
    join_us_table,
share_experience_table,
ask_suggestion_table,
)
class JoinUsResources(resources.ModelResource):
    class Meta:
        model = join_us_table
        fields = ('id','name','age','gender','email_address','phone_number','pincode', 'address','city', 'state','country', 'profession','message','photograph','email_verfied','identity_verified')
class ShareExperienceResources(resources.ModelResource):
    class Meta:
        model = share_experience_table
        fields = ('id','name','age','gender','city', 'state','country','email_address','phone_number','disease', 'pathies', 'date_from','date_to','experience','show_name','preferred_communication','reports')
class AskSuggeestionsResources(resources.ModelResource):
    class Meta:
        model = ask_suggestion_table
        fields = ('id','name','age','gender','city', 'state','country','email_address','phone_number','disease', 'pathies','query','show_study','show_email','reports')