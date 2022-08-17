class IPLock:
    from ipwhois import IPWhois

    locked_ips, locked_countries = [], []
    add_ips, add_countries = False, False

    def __init__(self, locked_ip_list=None, locked_countries_list=None):

        if locked_ip_list is not None:
            self.add_ips = True
            self.locked_ips = locked_ip_list

        if locked_countries_list is not None:
            self.add_countries = True
            self.locked_countries = locked_countries_list

    def is_locked(self, addr):
        is_locked_ = False
        if self.add_ips:
            if addr in self.locked_ips:
                is_locked_ = True
        if self.add_countries:
            country = self.ip_country(addr)
            if country in self.locked_countries:
                is_locked_ = True
        return is_locked_

    def ip_country(self, addr: str):
        return self.IPWhois(addr).lookup_whois()['asn_country_code']


class IPAllow:
    from ipwhois import IPWhois

    allowed_ips, allowed_countries = [], []
    add_ips, add_countries = False, False

    def __init__(self, allow_ips=None, allow_countries=None):
        if allow_ips is not None:
            self.add_ips = True
            self.allowed_ips = allow_ips
        if allow_countries is not None:
            self.add_countries = True
            self.allowed_countries = allow_countries

    def is_allowed(self, addr):
        is_allowed_ = False
        if self.add_ips:
            if addr in self.allowed_ips:
                is_allowed_ = True
        if self.add_countries:
            country = self.ip_country(addr)
            if country in self.allowed_countries:
                is_allowed_ = True
        return is_allowed_

    def ip_country(self, addr: str):
        return self.IPWhois(addr).lookup_whois()['asn_country_code']
