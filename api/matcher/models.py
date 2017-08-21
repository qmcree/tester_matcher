from django.db.models import CharField, Model, ForeignKey


class Device(Model):
    """
    List of all devices.
    """
    name = CharField(max_length=20)


class Country(Model):
    """
    List of all countries.
    """
    name = CharField(max_length=30)
    code_iso2 = CharField(max_length=2)


class Tester(Model):
    """
    List of all testers and their country of residence.
    """
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    country = ForeignKey(Country)


class TesterDevice(Model):
    """
    The devices belonging to a tester.
    """
    tester = ForeignKey(Tester)
    device = ForeignKey(Device)


class TesterBugReport(Model):
    """
    The bugs for a device reported by a tester.
    """
    tester = ForeignKey(Tester)
    device = ForeignKey(Device)
