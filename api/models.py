# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class KeyValue(models.Model):
    key = models.CharField(max_length=50,primary_key=True)
    value = models.CharField(max_length=50)

    class Meta:
        db_table = 'key_value'

class Competitions(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=50)
    cityname = models.CharField(db_column='cityName', max_length=50)  # Field name made lowercase.
    countryid = models.CharField(db_column='countryId', max_length=50)  # Field name made lowercase.
    information = models.TextField(blank=True, null=True)
    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField()
    day = models.PositiveSmallIntegerField()
    endmonth = models.PositiveSmallIntegerField(db_column='endMonth')  # Field name made lowercase.
    endday = models.PositiveSmallIntegerField(db_column='endDay')  # Field name made lowercase.
    eventspecs = models.CharField(db_column='eventSpecs', max_length=256, blank=True,
                                  null=True)  # Field name made lowercase.
    wcadelegate = models.TextField(db_column='wcaDelegate', blank=True, null=True)  # Field name made lowercase.
    organiser = models.TextField(blank=True, null=True)
    venue = models.CharField(max_length=240)
    venueaddress = models.CharField(db_column='venueAddress', max_length=120, blank=True,
                                    null=True)  # Field name made lowercase.
    venuedetails = models.CharField(db_column='venueDetails', max_length=120, blank=True,
                                    null=True)  # Field name made lowercase.
    external_website = models.CharField(max_length=200, blank=True, null=True)
    cellname = models.CharField(db_column='cellName', max_length=45)  # Field name made lowercase.
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Competitions'


class Continents(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    recordname = models.CharField(db_column='recordName', max_length=3)  # Field name made lowercase.
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    zoom = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Continents'


class Countries(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    continentid = models.CharField(db_column='continentId', max_length=50)  # Field name made lowercase.
    iso2 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Countries'


class Events(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=54)
    rank = models.IntegerField()
    format = models.CharField(max_length=10)
    cellname = models.CharField(db_column='cellName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Events'


class Formats(models.Model):
    id = models.CharField(max_length=1, primary_key=True)
    name = models.CharField(max_length=50)
    sort_by = models.CharField(max_length=255)
    sort_by_second = models.CharField(max_length=255)
    expected_solve_count = models.IntegerField()
    trim_fastest_n = models.IntegerField()
    trim_slowest_n = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Formats'


class Persons(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    subid = models.IntegerField()
    name = models.CharField(max_length=80, blank=True, null=True)
    countryid = models.CharField(db_column='countryId', max_length=50)  # Field name made lowercase.
    gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Persons'


class Ranksaverage(models.Model):
    personid = models.CharField(db_column='personId', max_length=10)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventId', max_length=6)  # Field name made lowercase.
    best = models.IntegerField()
    worldrank = models.IntegerField(db_column='worldRank')  # Field name made lowercase.
    continentrank = models.IntegerField(db_column='continentRank')  # Field name made lowercase.
    countryrank = models.IntegerField(db_column='countryRank')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RanksAverage'


class Rankssingle(models.Model):
    personid = models.CharField(db_column='personId', max_length=10)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventId', max_length=6)  # Field name made lowercase.
    best = models.IntegerField()
    worldrank = models.IntegerField(db_column='worldRank')  # Field name made lowercase.
    continentrank = models.IntegerField(db_column='continentRank')  # Field name made lowercase.
    countryrank = models.IntegerField(db_column='countryRank')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RanksSingle'


class Results(models.Model):
    competitionid = models.CharField(db_column='competitionId', max_length=32)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventId', max_length=6)  # Field name made lowercase.
    roundtypeid = models.CharField(db_column='roundTypeId', max_length=1)  # Field name made lowercase.
    pos = models.SmallIntegerField()
    best = models.IntegerField()
    average = models.IntegerField()
    personname = models.CharField(db_column='personName', max_length=80, blank=True,
                                  null=True)  # Field name made lowercase.
    personid = models.CharField(db_column='personId', max_length=10)  # Field name made lowercase.
    personcountryid = models.CharField(db_column='personCountryId', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
    formatid = models.CharField(db_column='formatId', max_length=1)  # Field name made lowercase.
    value1 = models.IntegerField()
    value2 = models.IntegerField()
    value3 = models.IntegerField()
    value4 = models.IntegerField()
    value5 = models.IntegerField()
    regionalsinglerecord = models.CharField(db_column='regionalSingleRecord', max_length=3, blank=True,
                                            null=True)  # Field name made lowercase.
    regionalaveragerecord = models.CharField(db_column='regionalAverageRecord', max_length=3, blank=True,
                                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Results'


class Roundtypes(models.Model):
    id = models.CharField(max_length=1, primary_key=True)
    rank = models.IntegerField()
    name = models.CharField(max_length=50)
    cellname = models.CharField(db_column='cellName', max_length=45)  # Field name made lowercase.
    final = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'RoundTypes'


class Rounds(models.Model):
    sorry_message = models.CharField(max_length=172)

    class Meta:
        managed = False
        db_table = 'Rounds'


class Scrambles(models.Model):
    scrambleid = models.PositiveIntegerField(db_column='scrambleId')  # Field name made lowercase.
    competitionid = models.CharField(db_column='competitionId', max_length=32)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventId', max_length=6)  # Field name made lowercase.
    roundtypeid = models.CharField(db_column='roundTypeId', max_length=1)  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=3)  # Field name made lowercase.
    isextra = models.IntegerField(db_column='isExtra')  # Field name made lowercase.
    scramblenum = models.IntegerField(db_column='scrambleNum')  # Field name made lowercase.
    scramble = models.TextField()

    class Meta:
        managed = False
        db_table = 'Scrambles'


class Championships(models.Model):
    id = models.IntegerField(primary_key=True)
    competition_id = models.CharField(max_length=191)
    championship_type = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'championships'


class EligibleCountryIso2SForChampionship(models.Model):
    id = models.BigIntegerField(primary_key=True)
    championship_type = models.CharField(max_length=191)
    eligible_country_iso2 = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'eligible_country_iso2s_for_championship'
