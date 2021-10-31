class User(object):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', "")
        self.password = kwargs.get('password', "")
        self.phone_number = kwargs.get('phone_number', "")
        self.occupation = kwargs.get('occupation', "")
        self.vaccination = kwargs.get('vaccination', "")
        self.covid_status = kwargs.get('covid_status', "")
        self.vaccine_status = kwargs.get('vaccine_status', "")
        self.vacc_apt_date1 = kwargs.get('vacc_apt_date1', "")
        self.vacc_apt_date2 = kwargs.get('vacc_apt_date2', "")
        self.vacc_apt_location = kwargs.get('vacc_apt_location', "")
