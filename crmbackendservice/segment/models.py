from django.db import models

class UserAttribute(models.Model):
    id = models.AutoField(primary_key=True)
    attribute_id = models.CharField(max_length=50, unique=True)
    data_type = models.CharField(max_length=20, choices=[('number', 'Number'), ('string', 'String'), ('date', 'Date'), ('boolean', 'Boolean')])
    type = models.CharField(max_length=20, choices=[('system', 'System'), ('custom', 'Custom')])
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('de-active', 'De-Active'), ('deleted', 'Deleted')])

class UserSegment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    segment_type = models.CharField(max_length=20, choices=[('static', 'Static'), ('dynamic', 'Dynamic')])
    customer_type = models.CharField(max_length=50, choices=[('new', 'New'), ('regular', 'Regular'), ('frequent_visitor', 'Frequent Visitor'), ('lapsed', 'Lapsed')])
    country_filter_operation = models.CharField(max_length=20, choices=[('any', 'Any'), ('none', 'None'), ('not_applicable', 'Not Applicable')])
    filtered_countries = models.ManyToManyField('Country', blank=True)
    user_attribute_filter_operation = models.CharField(max_length=20, choices=[('and', 'And'), ('or', 'Or')])
    user_attribute_filters = models.ManyToManyField('UserAttributeFilter', blank=True)
    user_ids_filter_condition = models.ForeignKey('UserFilterCondition', on_delete=models.SET_NULL, null=True, blank=True)
    activity_filters = models.ManyToManyField('ActivityFilter', blank=True)

class UserAttributeFilter(models.Model):
    id = models.AutoField(primary_key=True)
    attribute = models.ForeignKey('UserAttribute', on_delete=models.CASCADE)
    condition = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

class UserFilterCondition(models.Model):
    id = models.AutoField(primary_key=True)
    condition_id = models.CharField(max_length=50)
    applicable_data_types = models.ManyToManyField('DataType', blank=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('de-active', 'De-Active'), ('deleted', 'Deleted')])

class ActivityFilter(models.Model):
    id = models.AutoField(primary_key=True)
    users_did_events_operation = models.CharField(max_length=20, choices=[('and', 'And'), ('or', 'Or')])
    users_did_events = models.ManyToManyField('Event', blank=True)
    users_not_did_events_operation = models.CharField(max_length=20, choices=[('and', 'And'), ('or', 'Or')])
    users_not_did_events = models.ManyToManyField('Event', related_name='users_not_did_events', blank=True)

class Event(models.Model):

    pass

class DataType(models.Model):

    pass

class Country(models.Model):

    pass
